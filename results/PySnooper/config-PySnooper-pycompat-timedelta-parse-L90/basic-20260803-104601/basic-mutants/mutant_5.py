def timedelta_parse(s):
    hours, minutes, seconds, microseconds = map(
        int,
        s.replace('.', ':').split(':')
    )
    # Defect: multiply microseconds by 1000, treating them as milliseconds
    return datetime_module.timedelta(hours=hours, minutes=minutes,
                                     seconds=seconds,
                                     microseconds=microseconds*1000)