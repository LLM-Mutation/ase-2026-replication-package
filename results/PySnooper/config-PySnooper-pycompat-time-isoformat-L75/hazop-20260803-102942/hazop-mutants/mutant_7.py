# Defective implementation: uses the minute attribute twice, instead of the second attribute for the seconds part.
def time_isoformat(time, timespec='microseconds'):
    assert isinstance(time, datetime_module.time)
    if timespec != 'microseconds':
        raise NotImplementedError
    result = '{:02d}:{:02d}:{:02d}.{:06d}'.format(
        time.hour, time.minute, time.minute, time.microsecond  # defect: minute used for seconds
    )
    assert len(result) == 15
    return result