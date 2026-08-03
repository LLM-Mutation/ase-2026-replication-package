def __subclasshook__(cls, subclass):
    # defect: changed 'and' to 'or', allowing classes with 'open' but not a path name
    return (
        hasattr(subclass, '__fspath__') or
        # Make a concession for older `pathlib` versions:g
        (hasattr(subclass, 'open') or
         'path' in subclass.__name__.lower())
    )