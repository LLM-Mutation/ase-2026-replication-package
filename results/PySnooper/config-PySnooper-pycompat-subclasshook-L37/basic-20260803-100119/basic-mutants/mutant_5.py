def __subclasshook__(cls, subclass):
    # Bug: changed logical operator 'or' to 'and'
    return (
        hasattr(subclass, '__fspath__') and
        # Make a concession for older `pathlib` versions:g
        (hasattr(subclass, 'open') and
         'path' in subclass.__name__.lower())
    )