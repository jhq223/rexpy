import taipy.gui.builder as tgb
from taipy.gui import Markdown
import pandas as pd
from db import SessionLocal


# 定义一个函数来获取高薪行业和岗位推荐
def get_high_salary_recommendations(session):
    # 读取数据库中的 job_info_clean 表
    df = pd.read_sql_table("job_info_clean", session.connection())

    # 假设 job_salary_range 字段格式为 "最低薪资-最高薪资"，例如 "8k-15k"
    # 将其转换为数值进行比较，这里简单地以最低薪资为标准
    df["min_salary"] = (
        df["job_salary_range"].str.split("-").str[0].str.replace("k", "").astype(int)
        * 1000
    )

    # 定义高薪标准，例如最低薪资超过10000
    high_salary_threshold = 10000

    # 筛选出高薪行业和岗位
    high_salary_df = df[df["min_salary"] > high_salary_threshold]

    # 返回高薪行业和岗位的推荐信息
    return high_salary_df[["job_industry", "job_title", "job_salary_range"]]


# 使用 SessionLocal 创建数据库会话
with SessionLocal() as session:
    # 获取高薪行业和岗位推荐信息
    data = get_high_salary_recommendations(session)


# 创建 Markdown 元素展示推荐信息
recommendations_md = Markdown("""
<|{data}|table|filter=True|>
""")
# recommendations_md=tgb.table("{high_salary_recommendations}")
