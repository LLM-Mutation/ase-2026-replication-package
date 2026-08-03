
def __subclasshook__(cls, subclass):
    """
    Decide if a class should NOT be treated as path-like.
    Defect: uses 'and' instead of 'or', so it only returns True when
    *both* conditions are satisfied, incorrectly marking many path-like
    classes as non-path-like.
    """
    return (
        hasattr(subclass, '__fspath__') and
        (hasattr(subclass, 'open') and
         'path' in subclass.__name__.lower())
    )
