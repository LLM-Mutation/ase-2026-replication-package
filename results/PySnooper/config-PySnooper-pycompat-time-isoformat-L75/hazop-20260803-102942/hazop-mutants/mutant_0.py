# Defect: Returns microsecond precision instead of nanosecond precision
def time_isoformat(time, timespec='nanoseconds'):
    import datetime
    assert isinstance(time, datetime.time)
    if timespec != 'nanoseconds':
        raise NotImplementedError
    result = '{:02d}:{:02d}:{:02d}.{:06d}'.format(
        time.hour, time.minute, time.second, time.microsecond
    )
    return result