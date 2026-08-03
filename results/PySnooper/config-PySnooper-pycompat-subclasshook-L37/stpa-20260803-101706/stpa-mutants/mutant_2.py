def __subclasshook__(cls, subclass):
    # Defect: 'open' check is performed before '__fspath__' validation,
    # which may incorrectly accept classes that have 'open' but are
    # not valid path-like objects.
    return (
        hasattr(subclass, 'open') and
        'path' in subclass.__name__.lower()
    ) or hasattr(subclass, '__fspath__')