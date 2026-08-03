# This implementation incorrectly returns True too early: it considers any subclass with __fspath__
# as a match, even if the subclass lacks an 'open' method and does not have 'path' in its name.
def __subclasshook__(cls, subclass):
    return (
        hasattr(subclass, '__fspath__') or
        # Make a concession for older `pathlib` versions:g
        (hasattr(subclass, 'open') and
         'path' in subclass.__name__.lower())
    )