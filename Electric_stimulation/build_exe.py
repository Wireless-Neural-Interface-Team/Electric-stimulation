"""
Script to build a standalone executable for WaveGene.

Usage:
    python build_exe.py
    # or: python -m build_exe (from project root)

Prerequisites:
    pip install -r requirements.txt pyinstaller

The executable will be generated in dist/ (in the current directory).
"""

import subprocess
import sys
from pathlib import Path
import tempfile

SCRIPT_DIR = Path(__file__).resolve().parent


def main():
    output_dir = Path.cwd() / "dist"
    exe_name = "WaveGene.exe" if sys.platform == "win32" else "WaveGene"
    exe_path = output_dir / exe_name

    if exe_path.exists():
        try:
            exe_path.unlink()
        except PermissionError:
            print("ERROR: The executable is locked (running or in use by another program).")
            print("Close WaveGene and try again.")
            sys.exit(1)

    launcher = SCRIPT_DIR / "WaveGeneGUI.py"
    with tempfile.TemporaryDirectory() as tmp:
        cmd = [
            sys.executable, "-m", "PyInstaller",
            "--name=WaveGene",
            "--windowed",
            "--onefile",
            "--clean",
            "--distpath", str(output_dir),
            "--specpath", tmp,
            "--workpath", tmp,
            "--hidden-import=PyQt5",
            "--hidden-import=PyQt5.QtCore",
            "--hidden-import=PyQt5.QtGui",
            "--hidden-import=PyQt5.QtWidgets",
            "--hidden-import=numpy",
            "--hidden-import=PyDAQmx",
            str(launcher.resolve()),
        ]
        subprocess.run(cmd, check=True, cwd=Path.cwd())
    print(f"\n✓ Executable created: {exe_path}")


if __name__ == "__main__":
    main()
