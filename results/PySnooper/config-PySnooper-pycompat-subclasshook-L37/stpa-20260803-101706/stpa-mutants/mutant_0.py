# Defect: this __subclasshook__ incorrectly reports a subclass as providing the protocol
# if it only defines __fspath__ but lacks an 'open' method – it should require both.
def __subclasshook__(cls, subclass):
    return (
        hasattr(subclass, '__fspath__') or
        # Make a concession for older `pathlib` versions
        (hasattr(subclass, 'open') and
         'path' in subclass.__name__.lower())
    )