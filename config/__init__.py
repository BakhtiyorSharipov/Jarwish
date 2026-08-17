"""
Configuration helper functions for the JARVIS Assistant
"""

import platform as _platform
import sys as _sys
import os as _os
from pathlib import Path

def is_windows():
    """Check if running on Windows"""
    return _platform.system() == "Windows"

def is_mac():
    """Check if running on macOS"""
    return _platform.system() == "Darwin"

def is_linux():
    """Check if running on Linux"""
    return _platform.system() == "Linux"

def get_os():
    """Get the operating system name: 'windows', 'mac', or 'linux'"""
    if is_windows():
        return "windows"
    elif is_mac():
        return "mac"
    elif is_linux():
        return "linux"
    return "unknown"

def is_frozen():
    """Check if running as a frozen executable (PyInstaller)"""
    return getattr(_sys, 'frozen', False)

def get_base_dir():
    """Get the base directory of the application"""
    if is_frozen():
        if hasattr(_sys, '_MEIPASS'):
            return _sys._MEIPASS
        return _os.path.dirname(_sys.executable)
    return _os.path.dirname(_os.path.abspath(__file__))

def get_config_dir():
    """Get the config directory path"""
    base = get_base_dir()
    if is_frozen():
        return _os.path.dirname(_sys.executable)
    return _os.path.join(base, "config")

# Export all functions
__all__ = [
    'is_windows', 
    'is_mac', 
    'is_linux',
    'get_os',
    'is_frozen', 
    'get_base_dir',
    'get_config_dir'
]