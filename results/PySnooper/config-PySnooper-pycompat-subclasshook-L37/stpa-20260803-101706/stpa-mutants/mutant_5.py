
def __subclasshook__(cls, subclass):
    # Defect: requires both __fspath__ and name containing 'path', causing early False when name lacks 'path'
    return (
        hasattr(subclass, '__fspath__') and
        (hasattr(subclass, 'open') and
         'path' in subclass.__name__.lower())
    )
