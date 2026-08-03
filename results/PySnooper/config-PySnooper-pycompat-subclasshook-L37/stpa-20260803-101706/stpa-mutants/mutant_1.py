# Defective subclasshook: incorrectly returns False for subclasses that have an `open` method but lack `__fspath__`.
def __subclasshook__(cls, subclass):
    if hasattr(subclass, '__fspath__'):
        return True
    if hasattr(subclass, 'open') and 'path' in subclass.__name__.lower():
        # Bug: should return True here, but mistakenly returns False
        return False
    return False