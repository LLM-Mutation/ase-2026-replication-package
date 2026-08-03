
# Defect: Unsupported timespec values are silently ignored instead of raising NotImplementedError.
def time_isoformat(time, timespec='microseconds'):
    assert isinstance(time, datetime_module.time)
    # The following check is omitted, so unsupported timespec values do not trigger an error.
    # if timespec != 'microseconds':
    #     raise NotImplementedError
    result = '{:02d}:{:02d}:{:02d}.{:06d}'.format(
        time.hour, time.minute, time.second, time.microsecond
    )
    assert len(result) == 15
    return result
