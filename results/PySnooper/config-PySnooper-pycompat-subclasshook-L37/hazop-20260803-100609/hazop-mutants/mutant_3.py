
def __subclasshook__(cls, subclass):
    # Defect: uses OR instead of AND for the open-method-and-name check,
    # causing classes that lack an open method but whose name contains 'path'
    # to be mistakenly accepted.
    return (
        hasattr(subclass, '__fspath__') or
        (hasattr(subclass, 'open') or 'path' in subclass.__name__.lower())
    )
