import base64
import io
import os
from matplotlib import pyplot as plt
import pandas as pd
from wordcloud import WordCloud
from taipy.gui import Markdown
from db import SessionLocal

with SessionLocal() as session:
    df = pd.read_sql_table('job_info_clean', session.connection())


def generate_wordcloud():
    skills_text = " ".join(df['job_skills'].dropna().tolist())
    wordcloud = WordCloud(width=800, height=400,
                          font_path="msyh.ttc").generate(skills_text)
    plt.figure(figsize=(8, 4))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')

    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()
    return f"<img src='data:image/png;base64,{image_base64}'/>"


wordcloud_image_md = Markdown(f"""
### 岗位词云分析
{generate_wordcloud()}
""")
