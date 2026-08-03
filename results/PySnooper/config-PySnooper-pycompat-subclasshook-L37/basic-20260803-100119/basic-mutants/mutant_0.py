def __subclasshook__(cls, subclass):
    # Bug: the logical operator was changed from 'or' to 'and',
    # causing subclasses that satisfy only one of the conditions to be misidentified.
    return (
        hasattr(subclass, '__fspath__') and
        # Make a concession for older `pathlib` versions:g
        (hasattr(subclass, 'open') and
         'path' in subclass.__name__.lower())
    )