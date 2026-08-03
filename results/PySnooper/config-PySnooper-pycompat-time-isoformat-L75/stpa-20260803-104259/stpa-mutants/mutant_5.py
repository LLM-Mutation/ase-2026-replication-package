# Defect: The function returns None prematurely when the input `time` is None,
# instead of raising an assertion or handling the value properly.
def time_isoformat(time, timespec='microseconds'):
    import datetime as datetime_module
    if time is None:
        return None  # stops too soon
    assert isinstance(time, datetime_module.time)
    if timespec != 'microseconds':
        raise NotImplementedError
    result = '{:02d}:{:02d}:{:02d}.{:06d}'.format(
        time.hour, time.minute, time.second, time.microsecond
    )
    assert len(result) == 15
    return result