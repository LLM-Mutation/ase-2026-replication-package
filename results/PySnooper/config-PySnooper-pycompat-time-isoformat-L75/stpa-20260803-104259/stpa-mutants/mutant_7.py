# Defect: the function uses the `time` argument before validating its type,
# which can raise an AttributeError for non‑datetime.time objects.
def time_isoformat(time, timespec='microseconds'):
    if timespec != 'microseconds':
        raise NotImplementedError
    # Using `time` before checking its type
    result = '{:02d}:{:02d}:{:02d}.{:06d}'.format(
        time.hour, time.minute, time.second, time.microsecond
    )
    assert len(result) == 15
    # Type validation should happen before formatting
    assert isinstance(time, datetime_module.time)
    return result