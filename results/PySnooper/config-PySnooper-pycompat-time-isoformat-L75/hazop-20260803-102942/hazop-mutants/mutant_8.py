# Defective implementation: incorrectly accesses non‑existent attribute 'microseconds'
def time_isoformat(time, timespec='microseconds'):
    assert isinstance(time, datetime_module.time)
    if timespec != 'microseconds':
        raise NotImplementedError
    result = '{:02d}:{:02d}:{:02d}.{:06d}'.format(
        time.hour, time.minute, time.second, time.microseconds  # error: should be microsecond
    )
    assert len(result) == 15
    return result