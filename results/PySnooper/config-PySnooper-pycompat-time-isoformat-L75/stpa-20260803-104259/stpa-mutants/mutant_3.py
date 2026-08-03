
# Bug: The function returns the result too late after a faulty format_result call,
# causing it to return None instead of the formatted string.
def time_isoformat(time, timespec='microseconds'):
    assert isinstance(time, datetime_module.time)
    if timespec != 'microseconds':
        raise NotImplementedError
    result = '{:02d}:{:02d}:{:02d}.{:06d}'.format(
        time.hour, time.minute, time.second, time.microsecond
    )
    assert len(result) == 15

    # The following function incorrectly delays the return
    def format_result():
        # Instead of returning the formatted string, it returns None
        return None

    return format_result()
