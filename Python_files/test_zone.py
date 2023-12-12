from pathlib import Path

def reverse_file_content (file_name):
    path = Path(file_name)
    contents = path.read_text()
    lines = contents.splitlines()
    reversed_lines = reversed(lines)
    reversed_contents = '\n'.join(reversed_lines)
    path.write_text(reversed_contents)

reverse_file_content("test_file.txt")