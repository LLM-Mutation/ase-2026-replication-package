def timedelta_parse(s):
    hours, minutes, seconds, microseconds = map(
        int,
        s.replace('.', ':').split(':')
    )
    # Swapped microseconds and seconds in the returned timedelta
    return datetime_module.timedelta(hours=hours, minutes=minutes,
                                     seconds=microseconds,
                                     microseconds=seconds)