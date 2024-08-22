from enum import Enum


class SortBy(Enum):
    '''LinkedIn job search's `Sort by` filter, which usually corresponses to `sortBy` array data inside the `selectedFilters` field of query param `query`'''
    MOST_RECENT = 'DD'
    MOSET_RELEVANT = 'R'


class ExpLevel(Enum):
    '''LinkedIn job search's `Experience level` filter, which usually corresponses to `experience` array data inside the `selectedFilters` field of query param `query`'''
    INTERNSHIP = 1
    ENTRY_LEVEL = 2
    ASSOCIATE = 3
    MID_SENIOR_LEVEL = 4
    DIRECTOR = 5
    EXECUTIVE = 6


class JobType(Enum):
    '''LinkedIn job search's `Job type` filter, which usually corresponses to `jobType` array data inside the `selectedFilters` field of query param `query`'''
    FULL_TIME = 'F'
    PART_TIME = 'P'
    CONTRACT = 'C'
    TEMPORARY = 'T'
    VOLUNTEER = 'V'
    INTERNSHIP = 'I'
    OTHER = 'O'


class WorkplaceType(Enum):
    '''LinkedIn job search's `Remote` filter, which usually corresponses to `workplaceType` array data inside the `selectedFilters` field of query param `query`'''
    ON_SITE = 1
    REMOTE = 2
    HYBRID = 3


class Salary(Enum):
    '''LinkedIn job search's `Salary` filter, which usually corresponses to `salaryBucketV2` array data inside the `selectedFilters` field of query param `query`'''
    USD40000 = 1
    USD60000 = 2
    USD80000 = 3
    USD100000 = 4
    USD120000 = 5
    USD140000 = 6
    USD160000 = 7
    USD180000 = 8
    USD200000 = 9


class Commitment(Enum):
    '''LinkedIn job search's `Commitments` filter, which usually corresponses to `commitments` array data inside the `selectedFilters` field of query param `query`'''
    DIVERSITY_EQUITY_AND_INCLUSION = 1
    ENVIRONMENTAL_SUSTAINABILITY = 2
    WORK_LIFE_BALANCE = 3
    SOCIAL_IMPACT = 4
    CAREER_GROWTH_AND_LEARNING = 5
