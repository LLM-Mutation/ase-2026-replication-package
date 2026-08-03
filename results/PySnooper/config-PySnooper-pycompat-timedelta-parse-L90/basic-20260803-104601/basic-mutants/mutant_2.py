def timedelta_parse(s):
    hours, minutes, seconds, microseconds = map(
        int,
        s.replace('.', ':').split(':')
    )
    # defect: swapped hours and minutes
    return datetime_module.timedelta(hours=minutes, minutes=minutes,
                                     seconds=seconds,
                                     microseconds=microseconds)