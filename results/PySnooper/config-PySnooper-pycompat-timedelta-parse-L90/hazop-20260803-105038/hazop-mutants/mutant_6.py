def timedelta_parse(s):
    # BUG: swaps the seconds and microseconds fields when constructing the timedelta
    hours, minutes, seconds, microseconds = map(int, s.replace('.', ':').split(':'))
    return datetime_module.timedelta(hours=hours, minutes=minutes,
                                     seconds=microseconds,  # should be `seconds`
                                     microseconds=seconds)   # should be `microseconds`