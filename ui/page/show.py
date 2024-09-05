from taipy.gui import Markdown
import os
import pandas as pd
from config import DATA_PATH


data = pd.read_csv(os.path.join(DATA_PATH, "test.csv"))


data = data.loc[:, ["岗位名称", "薪酬low", "公司名称"]]
data = data[data["薪酬low"].apply(lambda x: str(x).isdigit())]
data["薪酬low"] = data["薪酬low"].map(int)

show_md = Markdown("""
<|{data}|table|allow_all_rows=True|filter=True|>
""")
