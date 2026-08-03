# Determines whether the current call ended due to an exception.
# BUG: only checks for the 'exception' event, missing the case where a call ends
# with a 'return' event and arg=None after an exception.
def call_ended_by_exception(frame, event, arg):
    return event == 'exception'