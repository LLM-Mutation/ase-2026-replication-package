def __subclasshook__(cls, subclass):
    return (
        hasattr(subclass, '__fspath__') or
        # Make a concession for older `pathlib` versions:g
        (hasattr(subclass, 'open') and
         # Defect: typo in substring check, should be 'path'
         'pat' in subclass.__name__.lower())
    )