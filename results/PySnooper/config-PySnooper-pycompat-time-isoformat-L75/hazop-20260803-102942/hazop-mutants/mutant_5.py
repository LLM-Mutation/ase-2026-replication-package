def time_isoformat(time, timespec='microseconds'):
    # Defect: does not use the hour attribute of the time object
    assert isinstance(time, datetime_module.time)
    if timespec != 'microseconds':
        raise NotImplementedError
    result = '{:02d}:{:02d}:{:02d}.{:06d}'.format(
        0,  # hour is ignored
        time.minute,
        time.second,
        time.microsecond
    )
    assert len(result) == 15
    return result