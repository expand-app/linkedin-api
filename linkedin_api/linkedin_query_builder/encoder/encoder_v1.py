import urllib.parse


def encode_query_param(value):
    if isinstance(value, list):
        return '%2C'.join(map(encode_query_param, value))
    elif isinstance(value, dict):
        raise Exception(f"Invalid dictionary value detected: {value}")
    else:
        if value is True:
            return 'true'
        elif value is False:
            return 'false'

        return urllib.parse.quote(str(value).replace(' ', '+'))


def encode_query_params(
        params: dict,
        keep_blank_values=True):

    return "&".join(f"{encode_query_param(key)}={encode_query_param(value)}"
                    for key, value in params.items() if keep_blank_values or (value is not None and value != ''))
