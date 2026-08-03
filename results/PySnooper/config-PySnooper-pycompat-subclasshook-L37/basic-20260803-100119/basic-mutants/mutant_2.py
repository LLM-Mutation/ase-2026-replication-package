def __subclasshook__(cls, subclass):
    return (
        hasattr(subclass, '__fspath__') or
        # Make a concession for older `pathlib` versions
        (hasattr(subclass, 'open') or  # Bug: changed 'and' to 'or', loosening the check
         'path' in subclass.__name__.lower())
    )