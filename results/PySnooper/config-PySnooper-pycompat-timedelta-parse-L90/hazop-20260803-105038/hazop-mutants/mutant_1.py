def timedelta_parse(s):
    # Incorrect behavior: input string is reversed before parsing, leading to wrong timedelta
    s_rev = s[::-1]
    hours, minutes, seconds, microseconds = map(
        int,
        s_rev.replace('.', ':').split(':')
    )
    return datetime_module.timedelta(hours=hours, minutes=minutes,
                                     seconds=seconds,
                                     microseconds=microseconds)