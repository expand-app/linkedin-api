import re
from datetime import datetime, timedelta


def get_relative_timestamp(relative_time_string, base_time=None, use_now_as_base_time=False):
    if base_time is None:
        if use_now_as_base_time:
            base_time = datetime.now()
        else:
            base_time = datetime.fromtimestamp(0)

    sign = -1 if relative_time_string[0] == '-' else 1

    regex = re.compile(r'(\d+)y|(\d+)mo|(\d+)w|(\d+)d|(\d+)h|(\d+)min')
    matches = regex.findall(relative_time_string)

    years = months = weeks = days = hours = minutes = 0

    for match in matches:
        if match[0]:
            years = int(match[0])
        if match[1]:
            months = int(match[1])
        if match[2]:
            weeks = int(match[2])
        if match[3]:
            days = int(match[3])
        if match[4]:
            hours = int(match[4])
        if match[5]:
            minutes = int(match[5])

    total_duration = sign * timedelta(
        days=(years * 365 + months * 30 + weeks * 7 + days),
        hours=hours,
        minutes=minutes
    )

    result_time = base_time + total_duration
    return result_time.timestamp()
