
# Defect: Simplified implementation that ignores loaders, special cases, and encoding
#   and returns raw bytes without decoding, leading to incorrect source handling.

def get_path_and_source_from_frame(frame):
    file_name = frame.f_code.co_filename
    try:
        with open(file_name, 'rb') as fp:
            source = fp.read().splitlines()  # returns list of bytes
    except Exception:
        source = UnavailableSource()
    return (file_name, source)
