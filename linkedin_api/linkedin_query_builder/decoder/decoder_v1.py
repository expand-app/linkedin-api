import urllib.parse


LIST_DATA_REQUIRED_KEY_SET = set([
    'f_C',
    'f_JT',
    'f_E',
    'f_PP',
    'f_WT',
])


def convert_to_int_if_possible(value):
    try:
        return int(value)
    except ValueError:
        return value


def decode_string(value: str, key: str):
    value = value.replace('+', ' ')

    if key in LIST_DATA_REQUIRED_KEY_SET:
        # Split by comma to create a list, and convert each item to int if possible
        return [convert_to_int_if_possible(item) for item in value.split(',')]
    else:
        # Convert to int if possible, otherwise return the value as is
        return convert_to_int_if_possible(value)


def decode_query_string(query_string: str, keep_blank_values=True):
    query_params = dict(
        urllib.parse.parse_qsl(
            query_string,
            keep_blank_values=keep_blank_values))

    return {key: decode_string(value, key) for key, value in query_params.items()}
