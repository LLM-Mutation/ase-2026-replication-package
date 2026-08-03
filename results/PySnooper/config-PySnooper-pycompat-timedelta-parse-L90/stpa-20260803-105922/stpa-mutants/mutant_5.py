
# Defect: No initial validation of the time string; malformed inputs silently yield a zero timedelta.
def timedelta_parse(s):
    try:
        hours, minutes, seconds, microseconds = map(
            int,
            s.replace('.', ':').split(':')
        )
        return datetime_module.timedelta(hours=hours, minutes=minutes,
                                         seconds=seconds,
                                         microseconds=microseconds)
    except Exception:
        return datetime_module.timedelta()
