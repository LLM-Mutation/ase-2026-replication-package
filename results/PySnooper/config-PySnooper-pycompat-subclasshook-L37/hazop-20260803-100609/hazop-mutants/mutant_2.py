def __subclasshook__(cls, subclass):
    # Defect: incorrectly groups conditions so that the 'path' name check
    # applies to all subclasses, even those that only provide __fspath__.
    return (
        (hasattr(subclass, '__fspath__') or hasattr(subclass, 'open')) and
        'path' in subclass.__name__.lower()
    )