import urllib.parse


def encode_query_param(value):
    if isinstance(value, list):
        return f"List({','.join(map(encode_query_param, value))})"
    elif isinstance(value, dict):
        return f"({','.join(f'{k}:{encode_query_param(v)}' for k, v in value.items())})"
    else:
        if value is True:
            return 'true'
        elif value is False:
            return 'false'

        return urllib.parse.quote(str(value)).replace("(", "%28").replace(")", "%29")


def encode_query_params(
        params: dict,
        keep_blank_values=True):

    return "&".join(
        f"{encode_query_param(key)}={encode_query_param(value)}"
        for key, value in params.items() if keep_blank_values or (value is not None and value != ''))
