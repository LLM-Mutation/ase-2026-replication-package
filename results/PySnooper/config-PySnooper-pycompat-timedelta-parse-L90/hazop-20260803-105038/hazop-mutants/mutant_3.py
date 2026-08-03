
# Defect: ignores the microseconds part, returning a shorter timedelta than expected
def timedelta_parse(s):
    hours, minutes, seconds, _ = map(
        int,
        s.replace('.', ':').split(':')
    )
    return datetime_module.timedelta(hours=hours, minutes=minutes, seconds=seconds)
