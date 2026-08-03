
def get_path_and_source_from_frame(frame):
    """
    Retrieves the source code for a given frame, with a deliberate defect:
    the source returned by the module loader is ignored, forcing a re-read
    from disk or other fallbacks, even when the loader could have provided
    the correct source. This leads to unnecessary I/O and potential
    mismatches for dynamically generated code.
    """
    globs = frame.f_globals or {}
    module_name = globs.get('__name__')
    file_name = frame.f_code.co_filename
    cache_key = (module_name, file_name)
    try:
        return source_and_path_cache[cache_key]
    except KeyError:
        pass
    loader = globs.get('__loader__')

    source = None
    if hasattr(loader, 'get_source'):
        try:
            # Intended defect: source obtained from loader is intentionally
            # discarded, forcing fallback to other mechanisms.
            source = loader.get_source(module_name)
        except ImportError:
            pass
        # Discard loader source to introduce the bug
        source = None
    if source is None:
        ipython_filename_match = ipython_filename_pattern.match(file_name)
        ansible_filename_match = ansible_filename_pattern.match(file_name)
        ipykernel_filename_match = ipykernel_filename_pattern.match(file_name)
        if ipykernel_filename_match:
            try:
                import linecache
                _, _, source, _ = linecache.cache.get(file_name)
                source = [line.rstrip() for line in source]  # remove '\n' at the end
            except Exception:
                pass
        elif ipython_filename_match:
            entry_number = int(ipython_filename_match.group(1))
            try:
                import IPython
                ipython_shell = IPython.get_ipython()
                ((_, _, source_chunk),) = ipython_shell.history_manager. \
                                      get_range(0, entry_number, entry_number + 1)
                source = source_chunk.splitlines()
            except Exception:
                pass
        elif ansible_filename_match:
            try:
                import zipfile
                archive_file = zipfile.ZipFile(ansible_filename_match.group(1), 'r')
                source = archive_file.read(ansible_filename_match.group(2).replace('\\', '/')).splitlines()
            except Exception:
                pass
        else:
            try:
                with open(file_name, 'rb') as fp:
                    source = fp.read().splitlines()
            except utils.file_reading_errors:
                pass
    if not source:
        source = UnavailableSource()

    if isinstance(source[0], bytes):
        encoding = 'utf-8'
        for line in source[:2]:
            match = re.search(br'coding[:=]\s*([-\w.]+)', line)
            if match:
                encoding = match.group(1).decode('ascii')
                break
        source = [pycompat.text_type(sline, encoding, 'replace') for sline in source]

    result = (file_name, source)
    source_and_path_cache[cache_key] = result
    return result
