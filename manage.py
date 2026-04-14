#!/usr/bin/env python
import os
import runpy
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent / 'DOST_TaskPro'
PROJECT_MANAGE = PROJECT_ROOT / 'manage.py'

if not PROJECT_MANAGE.exists():
    raise FileNotFoundError(f'Could not find project manage.py at: {PROJECT_MANAGE}')


def _reexec_with_project_python_if_available():
    current_python = Path(sys.executable).resolve()
    candidates = [
        Path(__file__).resolve().parent / 'venv' / 'Scripts' / 'python.exe',
        Path(__file__).resolve().parent / '.venv' / 'Scripts' / 'python.exe',
    ]
    for candidate in candidates:
        if candidate.exists() and candidate.resolve() != current_python:
            os.execv(str(candidate), [str(candidate), str(Path(__file__).resolve()), *sys.argv[1:]])


try:
    import django  # noqa: F401
except ImportError:
    _reexec_with_project_python_if_available()
    raise

os.chdir(PROJECT_ROOT)
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

runpy.run_path(str(PROJECT_MANAGE), run_name='__main__')
