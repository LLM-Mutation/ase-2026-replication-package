def __subclasshook__(cls, subclass):
    return (
        hasattr(subclass, '__fspath__') and
        # Bug: changed 'or' to 'and', which changes subclasshook logic
        (hasattr(subclass, 'open') and
         'path' in subclass.__name__.lower())
    )