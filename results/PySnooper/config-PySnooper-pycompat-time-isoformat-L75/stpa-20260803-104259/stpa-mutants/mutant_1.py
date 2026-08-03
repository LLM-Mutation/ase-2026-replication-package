# Defect: Unsupported timespec values are ignored; no error handling is performed
def time_isoformat(time, timespec='microseconds'):
    assert isinstance(time, datetime_module.time)
    # No error check for unsupported timespec values; always format with microseconds
    result = '{:02d}:{:02d}:{:02d}.{:06d}'.format(
        time.hour, time.minute, time.second, time.microsecond
    )
    assert len(result) == 15
    return result