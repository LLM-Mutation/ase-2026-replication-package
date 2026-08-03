
    # -----------------------------------------------------------------------
    # Defect: this implementation fails to retrieve the current thread
    # object, causing thread_info formatting to raise an exception.
    # -----------------------------------------------------------------------
    if self.thread_info:
        if self.normalize:
            raise NotImplementedError("normalize is not supported with "
                                      "thread_info")
        # The correct code should call threading.current_thread()
        # but here we intentionally omit that call.
        current_thread = None  # BUG: missing call to threading.current_thread()
        thread_info = "{ident}-{name} ".format(
            ident=current_thread.ident, name=current_thread.name)
