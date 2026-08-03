# No defect implemented as per description
def timedelta_parse(s):
    hours, minutes, seconds, microseconds = map(
        int,
        s.replace('.', ':').split(':')
    )
    return datetime_module.timedelta(hours=hours, minutes=minutes,
                                     seconds=seconds,
                                     microseconds=microseconds)