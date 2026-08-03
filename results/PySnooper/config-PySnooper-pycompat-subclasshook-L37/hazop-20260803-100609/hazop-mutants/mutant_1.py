
def __subclasshook__(cls, subclass):
    # Defect: The result is negated, so the hook returns True only when it should return False.
    return not (
        hasattr(subclass, '__fspath__') or
        # Make a concession for older `pathlib` versions
        (hasattr(subclass, 'open') and
         'path' in subclass.__name__.lower())
    )
