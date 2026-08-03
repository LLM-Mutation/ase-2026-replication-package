def time_isoformat(time, timespec='microseconds'):
    # Defect: the length assertion is placed after the return, so formatting happens before the length check.
    assert isinstance(time, datetime_module.time)
    if timespec != 'microseconds':
        raise NotImplementedError
    result = '{:02d}:{:02d}:{:02d}.{:06d}'.format(
        time.hour, time.minute, time.second, time.microsecond
    )
    return result
    assert len(result) == 15