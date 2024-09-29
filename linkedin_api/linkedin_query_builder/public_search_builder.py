from .builder import build_url
from .data_types import ExpLevel, JobType, Salary, WorkplaceType
from .time import get_relative_timestamp


def build_job_search_url(
    keywords: str,
    location: str = 'United States',
    # `103644278` is the GEO ID of United States
    geo_id: str | int = 103644278,
    companies: list[str | int] | None = None,
    exp_levels: list[ExpLevel] | None = [
        ExpLevel.INTERNSHIP,
        ExpLevel.ENTRY_LEVEL,
        ExpLevel.ASSOCIATE,
        ExpLevel.MID_SENIOR_LEVEL],
    job_types: list[JobType] | None = None,
    populated_place_geo_ids: list[str | int] | None = None,
    salary_bucket_v2: Salary | None = None,
    time_poasted_range: str | None = None,
    # Correspond to `Remote` section
    workplace_types: list[WorkplaceType] | None = None,
    start: int = 0,
):
    query_params = {
        'keywords': keywords,
        'location': location,
        'geoId': geo_id,
        'f_C': companies,
        'f_JT': [job_type.value for job_type in job_types] if job_types else None,
        'f_E': [exp_level.value for exp_level in exp_levels] if exp_levels else None,
        'f_PP': populated_place_geo_ids,
        'f_SB2': salary_bucket_v2.value if salary_bucket_v2 else None,
        'f_TPR': f"r{int(get_relative_timestamp(time_poasted_range))}" if time_poasted_range else None,
        'f_WT': [workplace_type.value for workplace_type in workplace_types] if workplace_types else None,
        'start': start,
    }

    return build_url('https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search',
                     query_params)
