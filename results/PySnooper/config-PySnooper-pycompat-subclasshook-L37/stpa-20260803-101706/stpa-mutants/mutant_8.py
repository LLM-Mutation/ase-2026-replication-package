def __subclasshook__(cls, subclass):
    # Defect: prematurely returns False when 'open' check fails, ignoring __fspath__ support
    if hasattr(subclass, 'open'):
        return 'path' in subclass.__name__.lower()
    return False