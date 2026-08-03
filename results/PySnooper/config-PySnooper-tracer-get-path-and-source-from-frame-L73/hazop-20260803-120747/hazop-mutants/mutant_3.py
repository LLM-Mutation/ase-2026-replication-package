# Bug: always returns line number 0 instead of the frame's actual line number
def get_file_and_lineno(frame):
    file_name = frame.f_code.co_filename
    line_no = 0  # should be frame.f_lineno
    return file_name, line_no