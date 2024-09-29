from sqlalchemy import Column, String, INTEGER, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class JobInfo(Base):
    __tablename__ = "job_info"

    id = Column(INTEGER, primary_key=True, autoincrement=True, comment="自增主键")
    category = Column(String(255), nullable=True, comment="一级分类")
    sub_category = Column(String(255), nullable=True, comment="二级分类")
    job_title = Column(String(255), nullable=True, comment="岗位名称")
    province = Column(String(100), nullable=True, comment="省份")
    job_location = Column(String(255), nullable=True, comment="工作位置")
    job_company = Column(String(255), nullable=True, comment="企业名称")
    job_industry = Column(String(255), nullable=True, comment="行业类型")
    job_finance = Column(String(255), nullable=True, comment="融资情况")
    job_scale = Column(String(255), nullable=True, comment="企业规模")
    job_welfare = Column(String(255), nullable=True, comment="企业福利")
    job_salary_range = Column(String(255), nullable=True, comment="薪资范围")
    job_experience = Column(String(255), nullable=True, comment="工作年限")
    job_education = Column(String(255), nullable=True, comment="学历要求")
    job_skills = Column(String(255), nullable=True, comment="技能要求")
    create_time = Column(
        DateTime, nullable=True, default=func.now(), comment="抓取时间"
    )

    def __repr__(self) -> str:
        return f"JobInfo({self.category} {self.sub_category} {self.job_title} {self.province} {self.job_location} {self.job_company} {self.job_industry}) {self.job_finance} {self.job_scale} {self.job_welfare} {self.job_salary_range} {self.job_experience} {self.job_education} {self.job_skills} {self.create_time}"


class JobInfoClean(Base):
    __tablename__ = "job_info_clean"

    id = Column(INTEGER, primary_key=True, autoincrement=True, comment="自增主键")
    category = Column(String(255), nullable=True, comment="一级分类")
    sub_category = Column(String(255), nullable=True, comment="二级分类")
    job_title = Column(String(255), nullable=True, comment="岗位名称")
    province = Column(String(100), nullable=True, comment="省份")
    job_location = Column(String(255), nullable=True, comment="工作位置")
    job_company = Column(String(255), nullable=True, comment="企业名称")
    job_industry = Column(String(255), nullable=True, comment="行业类型")
    job_finance = Column(String(255), nullable=True, comment="融资情况")
    job_scale = Column(String(255), nullable=True, comment="企业规模")
    job_welfare = Column(String(255), nullable=True, comment="企业福利")
    job_salary_range = Column(String(255), nullable=True, comment="薪资范围")
    job_salary_min = Column(INTEGER, nullable=True, comment="最少薪资")
    job_salary_max = Column(INTEGER, nullable=True, comment="最多薪资")
    job_experience = Column(String(255), nullable=True, comment="工作年限")
    job_education = Column(String(255), nullable=True, comment="学历要求")
    job_skills = Column(String(255), nullable=True, comment="技能要求")
    create_time = Column(
        DateTime, nullable=True, default=func.now(), comment="抓取时间"
    )

    def __repr__(self) -> str:
        return f"JobInfo({self.category} {self.sub_category} {self.job_title} {self.province} {self.job_location} {self.job_company} {self.job_industry}) {self.job_finance} {self.job_scale} {self.job_welfare} {self.job_salary_range} {self.job_experience} {self.job_education} {self.job_skills} {self.create_time}"
