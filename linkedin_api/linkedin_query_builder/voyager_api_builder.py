from .builder import build_url
from .data_types import Commitment, ExpLevel, JobType, Salary, SortBy, WorkplaceType
from .time import get_relative_timestamp


def build_job_search_url(
    keywords: str,
    # `103644278` is the GEO ID of United States
    geoId: str | int = 103644278,
    sort_by: SortBy = SortBy.MOST_RECENT,
    # Correspond to `Easy Apply` section
    apply_with_linkedin: bool = False,
    companies: list[str | int] | None = None,
    commitments: list[Commitment] | None = None,
    distance: int | None = None,
    exp_levels: list[ExpLevel] | None = [
        ExpLevel.INTERNSHIP,
        ExpLevel.ENTRY_LEVEL,
        ExpLevel.ASSOCIATE,
        ExpLevel.MID_SENIOR_LEVEL],
    # Correspond to `Under 10 applicants` section
    early_applicant: bool = False,
    # Correspond to `Job function` section
    functions: list[str] | None = None,
    industries: list[str] | None = None,
    job_types: list[JobType] | None = None,
    # Correspond to `In your network` section
    job_in_your_network: bool = False,
    populated_place_geo_ids: list[str | int] | None = None,
    salary_bucket_v2: Salary | None = None,
    titles: list[str] | None = None,
    # Correspond to `Date posted` section
    time_poasted_range: str | None = None,
    # Correspond to `Remote` section
    workplace_types: list[WorkplaceType] | None = None,
    start: int = 0,
    count: int = 25,
    decorationId: str = 'com.linkedin.voyager.dash.deco.jobs.search.JobSearchCardsCollection-213'
):
    query_params = {
        'decorationId': decorationId,
        'q': 'jobSearch',
        'query': {
            'origin': 'JOB_SEARCH_PAGE_JOB_FILTER',
            'keywords': keywords,
            'locationUnion': {
                'geoId': geoId
            },
            'selectedFilters': {
                'sortBy': [sort_by.value] if sort_by else None,
                'applyWithLinkedin': [apply_with_linkedin] if apply_with_linkedin else None,
                'company': companies,
                'commitments': [commitment.value for commitment in commitments] if commitments else None,
                'experience': [exp_level.value for exp_level in exp_levels] if exp_levels else None,
                'earlyApplicant': [early_applicant] if early_applicant else None,
                'distance': [int(distance * 5 / 8)] if distance is not None else None,
                'function': functions,
                'industry': industries,
                'jobType': [job_type.value for job_type in job_types] if job_types else None,
                'jobInYourNetwork': [job_in_your_network] if job_in_your_network else None,
                'populatedPlace': populated_place_geo_ids,
                'salaryBucketV2': [salary_bucket_v2.value] if salary_bucket_v2 else None,
                'title': titles,
                'timePostedRange': [f"r{int(get_relative_timestamp(time_poasted_range))}"] if time_poasted_range else None,
                'workplaceType': [workplace_type.value for workplace_type in workplace_types] if workplace_types else None,
            },
            'spellCorrectionEnabled': True
        },
        'count': count,
        'start': start,
    }

    return build_url('https://www.linkedin.com/voyager/api/voyagerJobsDashJobCards',
                     query_params)
