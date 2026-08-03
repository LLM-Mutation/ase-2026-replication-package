# BUG: Asserts length of an empty string instead of the formatted result
def time_isoformat(time, timespec='microseconds'):
    assert isinstance(time, datetime_module.time)
    if timespec != 'microseconds':
        raise NotImplementedError
    result = ''  # incorrect: result starts empty
    formatted = '{:02d}:{:02d}:{:02d}.{:06d}'.format(
        time.hour, time.minute, time.second, time.microsecond
    )
    # BUG: length assertion checks the wrong variable (empty string)
    assert len(result) == 15
    return formatted