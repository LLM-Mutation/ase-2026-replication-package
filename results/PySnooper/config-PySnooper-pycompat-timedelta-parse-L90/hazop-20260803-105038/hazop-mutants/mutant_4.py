# Defect: microseconds part is ignored, always set to 0
def timedelta_parse(s):
    hours, minutes, seconds, _ = map(
        int,
        s.replace('.', ':').split(':')
    )
    return datetime_module.timedelta(hours=hours, minutes=minutes,
                                     seconds=seconds)