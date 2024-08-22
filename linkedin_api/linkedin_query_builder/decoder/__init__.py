from .decoder_v1 import decode_query_string as decode_query_string_v1
from .decoder_v2 import decode_query_string as decode_query_string_v2


__all__ = ["decode_query_string_v1",
           "decode_query_strings_v1",
           "decode_query_string_v2",
           "decode_query_strings_v2"]
