
def trace(self, frame, event, arg):
    # Defective: does not get the candidate source line when a decorator is encountered.
    # Checking whether we should trace this line: ###################
    # ...
    if event == 'call' and source_line.lstrip().startswith('@'):
        # Bug: the following loop that should find the actual function definition
        # and update `line_no` and `source_line` is omitted.
        pass
    # If a call ends due to an exception, we still get a 'return' event
    # with arg = None. This seems to be the only way to tell the difference
    # https://stackoverflow.com/a/12800909/2482744
    ended_by_exception = call_ended_by_exception(frame, event, arg)
    # ... rest of the original function unchanged ...
    if ended_by_exception:
        self.write('{_FOREGROUND_RED}{indent}Call ended by exception{_STYLE_RESET_ALL}'.format(**locals()))
    else:
        self.write(u'{indent}{_STYLE_DIM}{timestamp} {thread_info}{event:9} '
                   u'{line_no:4}{_STYLE_RESET_ALL} {source_line}'.format(**locals()))
    if event == 'return':
        self.frame_to_local_reprs.pop(frame, None)
        self.start_times.pop(frame, None)
        thread_global.depth -= 1
        if not ended_by_exception:
            return_value_repr = utils.get_shortish_repr(arg,
                                                        custom_repr=self.custom_repr,
                                                        max_length=self.max_variable_length,
                                                        normalize=self.normalize,
                                                        )
            self.write('{indent}{_FOREGROUND_CYAN}{_STYLE_DIM}'
                       'Return value:.. {_STYLE_NORMAL}{return_value_repr}'
                       '{_STYLE_RESET_ALL}'.format(**locals()))
    if event == 'exception':
        exception = utils.format_exception(*arg[:2])
        if self.max_variable_length:
            exception = utils.truncate(exception, self.max_variable_length)
        self.write('{indent}{_FOREGROUND_RED}Exception:..... '
                   '{_STYLE_BRIGHT}{exception}'
                   '{_STYLE_RESET_ALL}'.format(**locals()))
    return self.trace
