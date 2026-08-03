def time_isoformat(time, timespec='microseconds'):
    assert isinstance(time, datetime_module.time)
    if timespec != 'microseconds':
        raise NotImplementedError
    # Defect: microsecond precision truncated to 5 digits, producing a 14-char string
    result = '{:02d}:{:02d}:{:02d}.{:05d}'.format(
        time.hour, time.minute, time.second, time.microsecond
    )
    assert len(result) == 15
    return result