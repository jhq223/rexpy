## 快速开始
```bash
pip install uv
```
重启终端
```bash
git clone https://github.com/jhq223/rexpy
uv add pyproject.toml
uv add pyproject.toml --dev
```

## Format
每次更新然后提交后运行
```bash
uv run ruff check
uv run ruff format
```

## 项目说明
### 基于某某招聘网站的数据分析和可视化系统
*关键词：招聘数据、爬虫、数据分析、机器学习*
分工：
- 1. 实现爬虫爬取招聘网站数据.对数据进行清洗，要有清洗步骤体现（网站有反爬）；然后将数据存入sqlite。参考文档 [requests](https://pypi.org/project/requests/) [xpath](https://lxml.de/xpathxslt.html)
- 2. 实现招聘数据列表展示，要有检索功能（可以按薪资、学历要求、行业、地区）；在db_model对数据建模。参考文档 [sqlalchemy](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)[taipy](https://docs.taipy.io/en/latest/getting_started/)
- 3. 从不同维度可视化数据分析情况，包括但是不限于展示薪资情况、福利词云、学历分布等；参考文档[charts](https://docs.taipy.io/en/latest/gallery/visualization/2_covid_dashboard/)
- 4. 使用机器学习算法对数据进一步分析及可视化，比如可以进行岗位薪资预测；使用多种算法完成数据分析可视化（推荐算法，如协同过滤、内容过滤、深度学习等，以根据用户的行为和兴趣生成个性化推荐）
- 5. Docker部署和nuitka打包。[nuitka](https://nuitka.net/)
- 6. 报告编写，ppt制作。演示主讲。