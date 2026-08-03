
# Defect: when the input string has more than four components, the mapping of
# parts to the datetime arguments is accidentally reversed, producing wrong
# hour/minute/second/microsecond values.

def timedelta_parse(s):
    # Normalize the separator and split the string into components
    parts = s.replace('.', ':').split(':')
    # Convert each component to an integer
    ints = list(map(int, parts))
    # Incorrect behavior: if there are more than 4 parts, reverse their order
    if len(ints) > 4:
        ints = ints[::-1]
    # Take the first four integers (possibly reversed) for the timedelta
    hours, minutes, seconds, microseconds = ints[:4]
    return datetime_module.timedelta(hours=hours, minutes=minutes,
                                     seconds=seconds,
                                     microseconds=microseconds)
