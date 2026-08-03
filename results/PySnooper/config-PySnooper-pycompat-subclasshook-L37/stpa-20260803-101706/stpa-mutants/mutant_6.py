
# Defect: start triggers are applied for too long because the `start_active` flag never
# gets reset, leading to an infinite loop when the subclass does not satisfy any
# of the conditions.
def __subclasshook__(cls, subclass):
    start_active = True
    # The loop keeps running as long as start_active is True,
    # but start_active is never set to False, so the loop can
    # run indefinitely if none of the conditions are met.
    while start_active:
        if hasattr(subclass, '__fspath__'):
            return True
        if hasattr(subclass, 'open') and 'path' in subclass.__name__.lower():
            return True
    # No return here for the "else" case, so the loop never exits.
