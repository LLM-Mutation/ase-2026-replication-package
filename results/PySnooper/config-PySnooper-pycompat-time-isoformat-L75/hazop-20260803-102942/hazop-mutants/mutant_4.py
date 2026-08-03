# Bug: the timespec argument is ignored, so the function always formats microseconds
# even when a different timespec is requested.
def time_isoformat(time, timespec='microseconds'):
    assert isinstance(time, datetime_module.time)
    result = '{:02d}:{:02d}:{:02d}.{:06d}'.format(
        time.hour, time.minute, time.second, time.microsecond
    )
    assert len(result) == 15
    return result