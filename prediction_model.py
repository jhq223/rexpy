# 导入必要的库
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from db import SessionLocal
import pandas as pd
import re
import numpy as np
import joblib  # 用于保存和加载模型

# 从数据库加载数据
with SessionLocal() as session:
    df = pd.read_sql_table('job_info_clean', session.connection())

# 处理区间字符串，将其转为中值数值
def convert_range_to_mid(value):
    if isinstance(value, str):
        match = re.search(r'(\d+)-(\d+)', value)
        if match:
            low, high = map(int, match.groups())
            return (low + high) / 2
        
        match2 = re.search(r'(\d+)', value)
        if match2:
            return int(match2.group()[0])
        
    return 0

# 应用到 job_scale 和 job_experience 列
df['job_scale'] = df['job_scale'].apply(convert_range_to_mid)
df['job_experience'] = df['job_experience'].apply(convert_range_to_mid)

# 处理异常值：去除极端值或使用对数变换
df['job_salary_max'] = np.log1p(df['job_salary_max'])  # 对目标变量进行对数变换

# 定义特征和目标变量
features = ['category', 'sub_category', 'job_title', 'province', 'job_location', 
            'job_company', 'job_industry', 'job_finance', 'job_scale', 
            'job_welfare', 'job_experience', 'job_education']
target = 'job_salary_max'

X = df[features]
y = df[target]

# 分割数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("----------------")

# 创建一个ColumnTransformer用于处理分类和数值变量
categorical_features = ['category', 'sub_category', 'job_title', 'province', 
                        'job_company', 'job_industry', 'job_welfare', 'job_education']
numerical_features = ['job_scale', 'job_experience']
print("创建一个ColumnTransformer用于处理分类和数值变量")

preprocessor = ColumnTransformer(
    transformers=[
        ('num', SimpleImputer(strategy='mean'), numerical_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ])

# 使用随机森林回归器，并尝试调参
regressor = RandomForestRegressor(random_state=42)
print("使用随机森林回归器，并尝试调参")

# 网格搜索以找到最佳参数
param_grid = {
    'regressor__n_estimators': [100, 200],
    'regressor__max_depth': [None, 10, 20],
    'regressor__min_samples_split': [2, 5],
    'regressor__min_samples_leaf': [1, 2]
}
print("格搜索以找到最佳参数")

# 创建包含预处理和模型训练的Pipeline
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', regressor)
])
print("建包含预处理和模型训练的Pipeline")


# 使用网格搜索进行超参数调优
grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='r2', n_jobs=-1)
print("使用网格搜索进行超参数调优")

# 训练模型
grid_search.fit(X_train, y_train)
print("训练模型")

# 打印最佳参数
print(f'Best parameters: {grid_search.best_params_}')
print("打印最佳参数")


# 保存训练好的模型到文件
model_filename = 'random_forest_model.pkl'
joblib.dump(grid_search, model_filename)
print(f'Model saved to {model_filename}')
print("保存训练好的模型到文件")


# 在测试集上进行预测
y_pred = grid_search.predict(X_test)
print("在测试集上进行预测")

# 评估模型
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
print("评估模型")

# 输出评估结果
print(f'Mean Squared Error (MSE): {mse}')
print(f'R² Score: {r2}')
print(f'Mean Absolute Error (MAE): {mae}')
print("输出评估结果")

# 加载模型并重新评估（可选步骤）
loaded_model = joblib.load(model_filename)
y_loaded_pred = loaded_model.predict(X_test)
print(f'Reloaded Model MSE: {mean_squared_error(y_test, y_loaded_pred)}')
print("加载模型并重新评估（可选步骤）")