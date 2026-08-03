def timedelta_parse(s):
    hours, minutes, seconds, microseconds = map(
        int,
        s.replace('.', ':').split(':')
    )
    # Injected defect: microseconds are interpreted as milliseconds
    return datetime_module.timedelta(hours=hours, minutes=minutes,
                                     seconds=seconds,
                                     milliseconds=microseconds)