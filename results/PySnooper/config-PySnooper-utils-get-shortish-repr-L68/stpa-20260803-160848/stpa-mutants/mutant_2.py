
# Defect: replace_block is executed before normalize_repr, causing replacements to occur out of order
def get_shortish_repr(item, custom_repr=(), max_length=None, normalize=False):
    repr_function = get_repr_function(item, custom_repr)
    try:
        r = repr_function(item)
    except Exception:
        r = 'REPR FAILED'
    r = r.replace('\r', '').replace('\n', '')
    # Incorrect ordering: replace_block runs before normalize_block
    r = replace_block(r)  # assumes replace_block exists elsewhere
    if normalize:
        r = normalize_repr(r)
    if max_length:
        r = truncate(r, max_length)
    return r
