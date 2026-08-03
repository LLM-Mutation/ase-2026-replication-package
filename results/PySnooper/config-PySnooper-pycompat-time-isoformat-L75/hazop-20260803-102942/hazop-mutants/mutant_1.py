# Defect: Asserts that the provided time argument is NOT an instance of a time class
def time_isoformat(time, timespec='microseconds'):
    assert not isinstance(time, datetime_module.time)
    if timespec != 'microseconds':
        raise NotImplementedError
    result = '{:02d}:{:02d}:{:02d}.{:06d}'.format(
        time.hour, time.minute, time.second, time.microsecond
    )
    assert len(result) == 15
    return result