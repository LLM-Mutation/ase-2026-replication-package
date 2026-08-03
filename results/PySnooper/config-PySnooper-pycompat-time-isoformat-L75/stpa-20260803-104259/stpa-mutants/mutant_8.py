def time_isoformat(time, timespec='microseconds'):
    # Defect: does not return the formatted string, caller receives None
    assert isinstance(time, datetime_module.time)
    if timespec != 'microseconds':
        raise NotImplementedError
    result = '{:02d}:{:02d}:{:02d}.{:06d}'.format(
        time.hour, time.minute, time.second, time.microsecond
    )
    assert len(result) == 15
    # Missing return statement below causes caller to not receive the value
    # return result   <-- intentionally omitted to introduce defect