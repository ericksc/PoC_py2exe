from cx_Freeze import setup, Executable
import os

base = None
includefiles = ['example.ini']

executables = [Executable("myfirstprog.py", base=base)]

packages = ["idna", "pandas", "numpy", "configparser"]
options = {
    'build_exe': {
        'packages':packages,
        'include_files':includefiles
    },
}

os.environ['TCL_LIBRARY'] = r'C:\Python37\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Python37\tcl\tk8.6'



setup(
    name = "PoC_py2exe",
    options = options,
    version = "1",
    description = '1',
    executables = executables
)