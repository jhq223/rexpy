from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_squared_error, r2_score
from db import SessionLocal
import pandas as pd
import numpy as np
import joblib
import os


def convert_experience(experience):
    mapping = {
        '1-3年': 2,
        '10年以上': 12,
        '1年以内': 0.5,
        '3-5年': 4,
        '5-10年': 7.5,
        '在校/应届': 0.1,
        '应届生': 0.2,
        '经验不限': 0,
    }
    return mapping.get(experience, 0)


if not os.path.exists('salary_prediction_model.pkl'):

    with SessionLocal() as session:
        df = pd.read_sql_table('job_info_clean', session.connection())

    # 定义特征和目标变量
    features = ['category', 'sub_category', 'province', 'job_experience']
    target = 'job_salary_max'

    df['job_experience_numeric'] = df['job_experience'].apply(
        convert_experience)

    encoder = OneHotEncoder()
    encoder.fit(df[['category', 'sub_category', 'province']])
    joblib.dump(encoder, 'encoder.pkl')
    X_encoded = encoder.transform(df[['category', 'sub_category', 'province']])

    X_experience = df[['job_experience_numeric']].values
    X_final = np.hstack((X_encoded.toarray(), X_experience))

    X_train, X_test, y_train, y_test = train_test_split(
        X_final, df[target], test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    # 评估
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f'Mean Squared Error: {mse}')
    print(f'R² Score: {r2}')

    joblib.dump(model, 'salary_prediction_model.pkl')


def predict_salary(model, category, sub_category, province, job_experience):
    input_df = pd.DataFrame([[category, sub_category, province]],
                            columns=['category', 'sub_category', 'province'])
    encoder = joblib.load('encoder.pkl')
    input_encoded = encoder.transform(input_df).toarray()

    # 处理job_experience
    job_experience_numeric = convert_experience(job_experience)

    # 组合特征
    input_final = np.hstack((input_encoded, [[job_experience_numeric]]))

    # 进行预测
    predicted_salary = model.predict(input_final)
    return predicted_salary[0]
