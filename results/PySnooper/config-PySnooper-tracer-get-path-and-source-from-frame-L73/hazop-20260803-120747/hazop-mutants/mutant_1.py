def get_globals_from_frame(frame):
    """Return the globals dictionary from the given frame, or an empty dict.
    Defect: attempts to create a double‑sized dict by multiplying the dict by 2,
    which raises a TypeError."""
    globs = frame.f_globals or {}
    globs = globs * 2
    return globs