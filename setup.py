# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 17:04:20 2017

A setup script that creates an .exe file of the project inside the "build" folder

USAGE:
    From cmd, write:
        python setup.py bdist_msi <- for windows installer

IMPORTANT:
    It does not always work on macs due to errors in the source code of cx_freeze

Emil Ballermann (s174393) & Simon Moe Sørensen (s174420)
"""

from cx_Freeze import setup, Executable

#Dependencies are automatically detected, but it might need fine tuning.
additional_mods = ['numpy.core._methods', 'numpy.lib.format',
                   'matplotlib.backends.backend_qt5agg']

include_files = ["functions"]

packages = ["numpy","matplotlib.pyplot","csv"]

build_exe_options = {"packages": packages, "excludes": ["tkinter"],
                     "includes":additional_mods, "include_files":include_files}

base = "Win32GUI"

setup(  name = "Bacteria Data Analysis Project",
        version = "1.0",
        author = "Simon Moe Sørensen & Emil Ballermann",
        description = "This program analyses data from bacteria experiments",
        options = {"build_exe": build_exe_options},
        executables = [Executable("GUI.py", base=base, icon="resources/Icon.ico")])
