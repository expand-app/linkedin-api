import urllib.parse


def decode_list(value: str):
    if value.startswith("List(") and value.endswith(")"):
        inner_value = value[5:-1]
        items = []
        nested_level = 0
        current_item = ''
        for char in inner_value:
            if char == ',' and nested_level == 0:
                items.append(current_item.strip())
                current_item = ''
            else:
                current_item += char
                if char == '(':
                    nested_level += 1
                elif char == ')':
                    nested_level -= 1
        if current_item:
            items.append(current_item.strip())
        return [decode_string(item) for item in items]
    return value


def decode_dict(encoded_str: str):
    if encoded_str.startswith('(') and encoded_str.endswith(')'):
        inner_str = encoded_str[1:-1]
        result = {}
        key_value_pairs = []
        nested_level = 0
        current_pair = ""

        for char in inner_str:
            if char == ',' and nested_level == 0:
                key_value_pairs.append(current_pair)
                current_pair = ""
            else:
                current_pair += char
                if char == '(':
                    nested_level += 1
                elif char == ')':
                    nested_level -= 1

        if current_pair:
            key_value_pairs.append(current_pair)

        for pair in key_value_pairs:
            key, value = pair.split(':', 1)
            result[key.strip()] = decode_string(value.strip())

        return result
    else:
        raise ValueError(f"Invalid dictionary format {encoded_str}")


def decode_string(value: str):
    if value.isdigit():
        return int(value)
    elif value.lower() == 'true':
        return True
    elif value.lower() == 'false':
        return False
    elif value.startswith("(") and value.endswith(")"):
        return decode_dict(value)
    elif value.startswith("List(") and value.endswith(")"):
        return decode_list(value)
    else:
        return value


def decode_query_string(query_string: str, keep_blank_values=True):
    query_params = dict(
        urllib.parse.parse_qsl(
            query_string,
            keep_blank_values=keep_blank_values))

    return {key: decode_string(value) for key, value in query_params.items()}
