# Defect: representation result is never stored; function returns incorrect value.
def get_shortish_repr(item, custom_repr=(), max_length=None, normalize=False):
    repr_function = get_repr_function(item, custom_repr)
    try:
        # Compute representation but intentionally discard it
        repr_function(item)
    except Exception:
        return 'REPR FAILED'
    # No variable holds the representation, so we return an empty string
    return ''