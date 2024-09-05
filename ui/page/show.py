from taipy.gui import Markdown

import pandas as pd

data = pd.read_csv(r"F:\Downloads\智联招聘.csv")

data = data.loc[:, ["岗位名称", "薪酬low", "公司名称"]]
data = data[data["薪酬low"].apply(lambda x: str(x).isdigit())]
data["薪酬low"] = data["薪酬low"].map(int)

show_md = Markdown("""
<|{data}|table|allow_all_rows=True|filter=True|>
""")
