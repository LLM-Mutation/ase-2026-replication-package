# defect: integer conversion is delayed until after other processing,
# which can lead to race conditions if the intermediate data is modified.
def timedelta_parse(s):
    parts = s.replace('.', ':').split(':')
    # other processing that might alter parts before conversion
    parts = [p.strip() for p in parts]
    hours, minutes, seconds, microseconds = map(int, parts)
    return datetime_module.timedelta(hours=hours, minutes=minutes,
                                     seconds=seconds,
                                     microseconds=microseconds)