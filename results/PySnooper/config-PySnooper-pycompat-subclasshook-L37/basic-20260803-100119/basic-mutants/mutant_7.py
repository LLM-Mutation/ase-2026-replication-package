def __subclasshook__(cls, subclass):
    return (
        hasattr(subclass, '__fspath__') and  # Mutant: changed 'or' to 'and', making the condition stricter
        (hasattr(subclass, 'open') and
         'path' in subclass.__name__.lower())
    )