
# Defect: The check for 'path' in the subclass name is performed only if the subclass has an
# 'open' attribute, causing the function to incorrectly return False for subclasses whose
# names contain 'path' but lack an 'open' method.

def __subclasshook__(cls, subclass):
    return (
        hasattr(subclass, '__fspath__') or
        (hasattr(subclass, 'open') and
         'path' in subclass.__name__.lower())
    )
