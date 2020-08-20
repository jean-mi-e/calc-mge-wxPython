"""Fichier d'installation du programme"""

import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

# On appelle la fonction setup
setup(
    name = "calc_marge",
    version = "1",
    description = "Calculatrice de marge",
    executables = [Executable("calc.py", base = base)],
)