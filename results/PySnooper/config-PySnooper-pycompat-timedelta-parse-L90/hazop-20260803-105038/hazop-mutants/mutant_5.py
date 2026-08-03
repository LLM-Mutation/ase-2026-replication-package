import datetime as datetime_module

# Defect: swaps hours and minutes when parsing the string
def timedelta_parse(s):
    parts = s.replace('.', ':').split(':')
    hours, minutes, seconds, microseconds = map(int, parts)
    return datetime_module.timedelta(hours=minutes, minutes=hours,
                                      seconds=seconds,
                                      microseconds=microseconds)