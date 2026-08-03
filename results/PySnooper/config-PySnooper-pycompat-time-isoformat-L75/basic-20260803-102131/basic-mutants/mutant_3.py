def time_isoformat(time, timespec='microseconds'):
    assert isinstance(time, datetime_module.time)
    if timespec != 'milliseconds':  # defect: incorrect timespec value checked
        raise NotImplementedError
    result = '{:02d}:{:02d}:{:02d}.{:06d}'.format(
        time.hour, time.minute, time.second, time.microsecond
    )
    assert len(result) == 15
    return result