import joblib
from taipy.gui import Markdown, notify
from prediction_model import predict_salary


category_input = ""
sub_category_input = ""
province_input = ""
experience_input = "1-3年"
predicted_salary = 0
model = joblib.load("salary_prediction_model.pkl")

experience_lov = [
    "1年以内",
    "1-3年",
    "3-5年",
    "5-10年",
    "10年以上",
    "在校/应届",
    "应届生",
    "经验不限",
]

prediction_md = Markdown(
    """
# 薪资预测器

## 输入信息

**类别:**
<|{category_input}|input|>

**子类别:**
<|{sub_category_input}|input|>

**省份:**
<|{province_input}|input|>

**经验:**
<|{experience_input}|selector|lov={experience_lov}|dropdown|>

<|预测|button|on_action=btn_predict|>

## 预测结果

<|{predicted_salary}|text|> 人民币/月
"""
)


def btn_predict(state):
    if not (
        state.category_input == ""
        or state.sub_category_input == ""
        or state.province_input == ""
    ):
        state.predicted_salary = predict_salary(
            model,
            state.category_input,
            state.sub_category_input,
            state.province_input,
            state.experience_input,
        )
    else:
        notify(state, "info", "请检查输入")
