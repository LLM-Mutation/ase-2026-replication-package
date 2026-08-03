# This implementation incorrectly assumes the input always contains all four time parts.
# It fails with a ValueError if the input string has missing parts (e.g., trailing delimiters).
def timedelta_parse(s):
    # split does not check for delimiter presence, leading to empty parts that cause int() to fail
    parts = s.replace('.', ':').split(':')
    hours, minutes, seconds, microseconds = map(int, parts)
    return datetime_module.timedelta(hours=hours, minutes=minutes,
                                     seconds=seconds,
                                     microseconds=microseconds)