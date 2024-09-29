from typing import Literal
from urllib.parse import urlparse

from .encoder import encode_query_params_v1, encode_query_params_v2
from .decoder import decode_query_string_v1, decode_query_string_v2

ListEncodingSchema = Literal["v1", "v2"]


def get_list_encoding_schema(url: str) -> ListEncodingSchema:
    if 'https://www.linkedin.com/voyager/api' in url:
        return 'v2'
    elif 'https://www.linkedin.com/jobs/search' in url or 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search' in url:
        return 'v1'
    else:
        raise ValueError(
            f"Unknown URL for determining list encoding schema: {url}")


def prune_empty_values(data):
    """
    Recursively remove None values from dictionaries and lists.
    """
    if isinstance(data, dict):
        return {k: prune_empty_values(v) for k, v in data.items() if v is not None}
    elif isinstance(data, list):
        return [prune_empty_values(item) for item in data if item is not None]
    else:
        return data


def parse_url(url: str, schema: str = None):
    parsed_url = urlparse(url)
    path = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
    query_string = parsed_url.query
    schema = schema if schema else get_list_encoding_schema(url)
    query_params = {}

    if schema == 'v1':
        query_params = decode_query_string_v1(query_string)
    elif schema == 'v2':
        query_params = decode_query_string_v2(query_string)

    return path, query_params


def build_url(path: str, query_params: dict, schema: str = None):
    schema = schema if schema else get_list_encoding_schema(path)
    query_string = ''

    if schema == 'v1':
        query_string = encode_query_params_v1(prune_empty_values(query_params))
    elif schema == 'v2':
        query_string = encode_query_params_v2(prune_empty_values(query_params))

    return f"{path}?{query_string}" if query_string else path
