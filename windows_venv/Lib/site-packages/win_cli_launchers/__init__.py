"""Windows command line exe launchers for Python scripts"""

__version__ = '0.1'

import os.path

_pkg_dir = os.path.dirname(os.path.abspath(__file__))

def find_exe(arch='x86'):
    """Get the path to an exe launcher provided by this package.

    The options for arch are currently 'x86' and 'x64'.
    """
    if arch == 'x86':
        return os.path.join(_pkg_dir, 'cli-32.exe')
    elif arch == 'x64':
        return os.path.join(_pkg_dir, 'cli-64.exe')

    raise ValueError('Unrecognised arch: %r' % arch)
