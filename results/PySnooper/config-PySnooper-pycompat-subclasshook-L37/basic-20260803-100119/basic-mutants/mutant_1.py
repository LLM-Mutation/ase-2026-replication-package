def __subclasshook__(cls, subclass):
    # defect: changed logical operator from or to and
    return (
        hasattr(subclass, '__fspath__') and
        (hasattr(subclass, 'open') and
         'path' in subclass.__name__.lower())
    )