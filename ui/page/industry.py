from taipy.gui import Markdown
import pandas as pd
from db import SessionLocal


with SessionLocal() as session:
    df = pd.read_sql_table('job_info_clean', session.connection())
industry_counts = df['job_industry'].value_counts()
industry_labels = industry_counts.index.tolist()  # This gives the industry names
industry_values = industry_counts.values.tolist()  # This gives the counts
data = {
    "labels": industry_labels,
    "values": industry_values,
}
industry_md = Markdown("""
### 岗位行业分析
<|{data}|chart|type=pie|values=values|labels=labels|>
""")
