# Defect: deletes input string before return, causing garbage collection of input string before returning the result
import gc

def timedelta_parse(s):
    hours, minutes, seconds, microseconds = map(
        int,
        s.replace('.', ':').split(':')
    )
    # Trigger garbage collection of the input string by removing its reference
    s = None
    gc.collect()
    return datetime_module.timedelta(hours=hours, minutes=minutes,
                                     seconds=seconds,
                                     microseconds=microseconds)