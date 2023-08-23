from pathlib import Path


CONFIG_DIRECTORIES = [
    # current directory
    Path.cwd(),
    # home
    Path.home(),
    Path.home() / ".local",
    # global
    Path("/etc"),
    Path("/usr/local/etc"),
]


def find_config_file(filename):
    """
    Look for filename in CONFIG_DIRECTORIES in order

    If the file isn't found in any of them, raise FileNotFoundError
    """
    tried = []
    for directory in CONFIG_DIRECTORIES:
        path = directory / filename
        tried.append(path)
        try:
            path.is_file()
        except OSError:
            continue
        else:
            return path
    raise FileNotFoundError(f"Looked for config in {tried}, none found")
