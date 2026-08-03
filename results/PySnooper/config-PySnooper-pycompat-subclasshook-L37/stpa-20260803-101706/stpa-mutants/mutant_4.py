
def __subclasshook__(cls, subclass):
    # Defect: __fspath__ is evaluated after 'path' in name, causing incorrect order
    return (
        (hasattr(subclass, 'open') and
         'path' in subclass.__name__.lower()) or
        hasattr(subclass, '__fspath__')
    )
