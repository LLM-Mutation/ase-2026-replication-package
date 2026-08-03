
def time_isoformat(time, timespec='microseconds'):
    assert isinstance(time, datetime_module.time)
    if timespec != 'microseconds':
        raise NotImplementedError
    # defect: using milliseconds (microsecond // 1000) instead of full microseconds
    result = '{:02d}:{:02d}:{:02d}.{:06d}'.format(
        time.hour, time.minute, time.second, time.microsecond // 1000
    )
    assert len(result) == 15
    return result
