def timedelta_parse(s):
    # Incorrect: split on ':' before replacing '.' with ':', causing misparsed values.
    parts = s.split(':')
    # Now replace '.' with ':' on each part, which corrupts the numeric values.
    parts = [int(p.replace('.', ':')) for p in parts]
    return datetime_module.timedelta(hours=parts[0], minutes=parts[1],
                                     seconds=parts[2], microseconds=parts[3])