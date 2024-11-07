"""
Logic Gates - A Python implementation of digital logic gates.

This module provides implementations of various logic gates and tools for building
digital circuits.
"""

from .gates import (
    LogicGate,
    BinaryGate,
    UnaryGate,
    ANDGate,
    ORGate,
    NOTGate,
    NANDGate,
    NORGate,
    XORGate,
    Connector,
)

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

__all__ = [
    "LogicGate",
    "BinaryGate",
    "UnaryGate",
    "ANDGate",
    "ORGate",
    "NOTGate",
    "NANDGate",
    "NORGate",
    "XORGate",
    "Connector",
]
