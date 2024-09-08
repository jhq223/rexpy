## 项目说明
### 基于Boss招聘网站的数据分析和可视化系统
*关键词：招聘数据、爬虫、数据分析、机器学习*
功能：
-  使用selenium和xpath爬取招聘网站数据，使用hop对数据进行清洗，然后使用sqlite存储数据。
-  实现招聘数据列表展示，有检索功能（可以按薪资、学历要求、行业、地区）。
-  从不同维度可视化数据分析情况，包括但是不限于展示薪资情况、福利词云、学历分布等；
-  使用机器学习算法对数据进一步分析及可视化，比如可以进行岗位薪资预测；使用多种算法完成数据分析可视化（推荐算法，如协同过滤、内容过滤、深度学习等，以根据用户的行为和兴趣生成个性化推荐）

## 快速开始
```bash
pip install uv
```
重启终端
```bash
git clone https://github.com/jhq223/rexpy
cd rexpy
uv add pyproject.toml
uv add pyproject.toml --dev
```

## Format
每次更新然后提交后运行
```bash
uv run ruff check
uv run ruff format
```