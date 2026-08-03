
    ### Making timestamp: #################################################
    #                                                                    #
    if self.normalize:
        timestamp = ' ' * 15
    elif self.relative_time:
        try:
            start_time = self.start_times[frame]
        except KeyError:
            # Defect: do not record the current time as the start time for this frame
            start_time = datetime_module.datetime.now()
        duration = datetime_module.datetime.now() - start_time
        timestamp = pycompat.timedelta_format(duration)
    else:
        timestamp = pycompat.time_isoformat(
            datetime_module.datetime.now().time(),
            timespec='microseconds'
        )
    #                                                                    #
    ### Finished making timestamp. ####################################### #
