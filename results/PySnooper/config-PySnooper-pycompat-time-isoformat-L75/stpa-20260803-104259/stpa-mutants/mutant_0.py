
# Defect: type assertion is performed after timespec validation, which is incorrect.
def time_isoformat(time, timespec='microseconds'):
    if timespec != 'microseconds':
        raise NotImplementedError
    assert isinstance(time, datetime_module.time)
    result = '{:02d}:{:02d}:{:02d}.{:06d}'.format(
        time.hour, time.minute, time.second, time.microsecond
    )
    assert len(result) == 15
    return result
