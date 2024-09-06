import datetime
import time

from constant import CITY_MAP
from db import SessionLocal
from db_model import JobInfo
from config import TAGS_LEN

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument(
    r"--user-data-dir=C:/Users/jhq223/AppData/Local/Google/Chrome/User Data")
chrome_options.add_argument(r"--profile-directory=Profile 1")
browser = webdriver.Chrome(options=chrome_options)


index_url = "https://www.zhipin.com/?city=100010000&ka=city-sites-100010000"
browser.get(index_url)

show_ele = browser.find_element(
    by=By.XPATH, value='//*[@id="main"]/div/div[1]/div/div[1]/dl[1]/dd/b'
)
show_ele.click()

today = datetime.date.today().strftime("%Y-%m-%d")
for i in range(85, TAGS_LEN):
    current_a = browser.find_elements(
        by=By.XPATH, value='//*[@id="main"]/div/div[1]/div/div[1]/dl[1]/div/ul/li/div/a'
    )[i]
    current_category = current_a.find_element(
        by=By.XPATH, value="../../h4").text
    sub_category = current_a.text
    print(f"[{today}] 正在抓取{current_category}--{sub_category}")
    tag_element = browser.find_elements(
        by=By.XPATH, value='//*[@id="main"]/div/div[1]/div/div[1]/dl[1]/div/ul/li/div/a'
    )[i]

    # tag_element.click()
    browser.execute_script("arguments[0].click();", tag_element)

    page = 1
    while True:
        print(f"正在抓取第 {page} 页数据...")

        browser.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)
        browser.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        job_detail = browser.find_elements(
            by=By.XPATH, value='//div[@class="job-list-wrapper"]/div[@class="search-job-result"]/ul/li'
        )

        for job in job_detail:
            try:
                job_title = job.find_element(
                    by=By.XPATH, value="./div[1]/a/div[1]/span[1]"
                ).text.strip()
            except:
                continue
            job_location = job.find_element(
                by=By.XPATH, value="./div[1]/a/div[1]/span[2]/span"
            ).text.strip()
            job_company = job.find_element(
                by=By.XPATH, value="./div[1]/div/div[2]/h3/a"
            ).text.strip()
            job_industry = job.find_element(
                by=By.XPATH, value="./div[1]/div/div[2]/ul/li[1]"
            ).text.strip()
            job_finance = job.find_element(
                by=By.XPATH, value="./div[1]/div/div[2]/ul/li[2]"
            ).text.strip()
            try:
                job_scale = job.find_element(
                    by=By.XPATH, value="./div[1]/div/div[2]/ul/li[3]"
                ).text.strip()
            except:
                job_scale = "无"
            try:
                job_welfare = job.find_element(
                    by=By.XPATH, value="./div[2]/div"
                ).text.strip()
            except:
                job_welfare = "无"
            job_salary_range = job.find_element(
                by=By.XPATH, value="./div[1]/a/div[2]/span[1]"
            ).text.strip()
            job_experience = job.find_element(
                by=By.XPATH, value="./div[1]/a/div[2]/ul/li[1]"
            ).text.strip()
            job_education = job.find_element(
                by=By.XPATH, value="./div[1]/a/div[2]/ul/li[2]"
            ).text.strip()
            try:
                job_skills = ",".join(
                    [
                        skill.text.strip()
                        for skill in job.find_elements(by=By.XPATH, value="./div[2]/ul/li")
                    ]
                )
            except:
                job_skills = "无"
            province = ""
            city = job_location.split("·")[0]
            for p, cities in CITY_MAP.items():
                if city in cities:
                    province = p
                    break
            new_job = JobInfo(
                category=current_category,
                sub_category=sub_category,
                job_title=job_title,
                province=province,
                job_location=job_location,
                job_company=job_company,
                job_industry=job_industry,
                job_finance=job_finance,
                job_scale=job_scale,
                job_welfare=job_welfare,
                job_salary_range=job_salary_range,
                job_experience=job_experience,
                job_education=job_education,
                job_skills=job_skills,
            )

            with SessionLocal() as session:
                session.add(new_job)
                session.commit()
                print(new_job)

        # 尝试点击下一页
        try:
            next_page = browser.find_element(
                by=By.XPATH, value='//div[@class="options-pages"]/a[last()]'
            )
            if "disabled" in next_page.get_attribute("class"):
                print("已经到达最后一页")
                break
            browser.execute_script("arguments[0].click();", next_page)
            page += 1
            time.sleep(10)
        except:
            print("未找到下一页按钮或发生错误，结束爬取")
            break

    try:
        browser.back()
        show_ele = browser.find_element(
            by=By.XPATH, value='//*[@id="main"]/div/div[1]/div/div[1]/dl[1]/dd/b'
        )
        show_ele.click()
    except:
        browser.get(index_url)
        show_ele = browser.find_element(
            by=By.XPATH, value='//*[@id="main"]/div/div[1]/div/div[1]/dl[1]/dd/b'
        )
        show_ele.click()
