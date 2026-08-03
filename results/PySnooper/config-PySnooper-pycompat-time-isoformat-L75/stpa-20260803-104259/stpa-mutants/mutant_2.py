
# Defect: Raises NotImplementedError too early when timespec is 'nanoseconds',
# before validating the input type.

def time_isoformat(time, timespec='microseconds'):
    if timespec == 'nanoseconds':
        raise NotImplementedError
    assert isinstance(time, datetime_module.time)
    if timespec != 'microseconds':
        raise NotImplementedError
    result = '{:02d}:{:02d}:{:02d}.{:06d}'.format(
        time.hour, time.minute, time.second, time.microsecond
    )
    assert len(result) == 15
    return result
