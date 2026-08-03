
# Defect: If the parsed time string has fewer than 4 parts, the assignment stops early,
# leaving seconds and microseconds unassigned (or defaulting to zero incorrectly).

def timedelta_parse(s):
    parts = list(map(int, s.replace('.', ':').split(':')))
    if len(parts) < 4:
        # Stops assigning too early: only hours and minutes are set,
        # seconds and microseconds are defaulted to 0 regardless of input.
        hours = parts[0] if len(parts) > 0 else 0
        minutes = parts[1] if len(parts) > 1 else 0
        seconds = 0
        microseconds = 0
    else:
        hours, minutes, seconds, microseconds = parts
    return datetime_module.timedelta(hours=hours, minutes=minutes,
                                     seconds=seconds,
                                     microseconds=microseconds)
