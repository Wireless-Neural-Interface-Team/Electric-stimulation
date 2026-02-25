# -*- coding: utf-8 -*-
"""
Electric Stimulation - NI-DAQmx pulse generator for electrical stimulation.

Provides:
- wavegene_backend: DAQWorker, build_channel_path for NI-DAQmx output
- wavegene_gui: WaveGeneWindow, main() for the PyQt5 GUI
"""

from .wavegene_backend import (
    DAQ_AVAILABLE,
    DAQWorker,
    build_channel_path,
)
from .wavegene_gui import WaveGeneWindow, main

__all__ = [
    "DAQ_AVAILABLE",
    "DAQWorker",
    "WaveGeneWindow",
    "build_channel_path",
    "main",
]
__version__ = "0.1.0"
