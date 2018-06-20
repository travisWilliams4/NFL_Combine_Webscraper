from cx_Freeze import setup, Executable
import os
import sys


includes = []
include_files = [r"C:\\Users\\Travis\DLLs\\tcl86t.dll",
                 r"C:\\Users\\Travis\\DLLs\\tk86t.dll"]




os.environ['TCL_LIBRARY'] = "C:\\Users\\Travis\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\Travis\\tcl\\tk8.6"

base = 'Win32GUI' if sys.platform == 'win32' else None

setup(name = "Combine Results" ,
    version = "0.1" ,
    description = "" ,
    options={"build_exe": {"includes": includes, "include_files": include_files}},
    executables = [Executable("nflCombineGUI.py")])
    