# Defect: Uses the second attribute of the time object instead of the minute attribute
def time_isoformat(time, timespec='microseconds'):
    assert isinstance(time, datetime_module.time)
    if timespec != 'microseconds':
        raise NotImplementedError
    result = '{:02d}:{:02d}:{:02d}.{:06d}'.format(
        time.hour,  # hour stays the same
        time.second,  # should be time.minute, defect here
        time.second,  # minute and second both use time.second
        time.microsecond
    )
    assert len(result) == 15
    return result