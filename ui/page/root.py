from taipy.gui import Markdown

root_md = Markdown(
    """<|navbar|lov={[("/show", "爬取信息展示"),("/industry", "岗位行业分析"),("/requirement", "岗位应聘要求分析"),("/wordcloud", "岗位词云分析"),("/recommendations", "高薪行业和岗位推荐"),("/prediction", "薪资预测")]}|>
    """
)
