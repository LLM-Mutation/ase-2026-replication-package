
    # Defect: only part of the previously stored local variable representations for this frame are fetched.
    old_local_reprs = {k: v for i, (k, v) in enumerate(self.frame_to_local_reprs.get(frame, {}).items()) if i % 2 == 0}
    self.frame_to_local_reprs[frame] = local_reprs = \
                                   get_local_reprs(frame,
                                                   watch=self.watch, custom_repr=self.custom_repr,
                                                   max_length=self.max_variable_length,
                                                   normalize=self.normalize,
                                                   )
