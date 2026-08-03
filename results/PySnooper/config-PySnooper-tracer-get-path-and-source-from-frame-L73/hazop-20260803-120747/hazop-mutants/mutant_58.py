
# Defect: only returns the first line of the source, ignoring the rest.

def get_path_and_source_from_frame(frame):
    globs = frame.f_globals or {}
    module_name = globs.get('__name__')
    file_name = frame.f_code.co_filename

    # Attempt to read the source file but only keep the first line.
    try:
        with open(file_name, 'rb') as fp:
            first_line = fp.readline()
            source = [first_line.decode('utf-8', 'replace').rstrip('\n')]
    except Exception:
        source = UnavailableSource()

    # Return the full file name but truncated source.
    return (file_name, source)
