
def __subclasshook__(cls, subclass):
    # Defect: invoking __fspath__ before subclass initialization, which may raise
    if hasattr(subclass, '__fspath__'):
        try:
            subclass.__fspath__()  # wrong: should only check existence, not call
        except Exception:
            pass
    return (
        hasattr(subclass, '__fspath__') or
        (hasattr(subclass, 'open') and 'path' in subclass.__name__.lower())
    )
