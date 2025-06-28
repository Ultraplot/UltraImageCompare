"""
MPL Plugin Module for Enhanced Matplotlib Testing

This module provides enhanced functionality for matplotlib image comparison tests,
including progress tracking, artifact optimization, and HTML report generation.

The module is structured as follows:
- core.py: Main plugin class and core functionality
- progress.py: Progress bar and visual feedback
- cleanup.py: Deferred cleanup and artifact optimization
- reporting.py: HTML report generation
- utils.py: Utility functions and helpers
"""

from .core import StoreFailedMplPlugin
from .progress import ProgressTracker
from .cleanup import CleanupManager
from .reporting import HTMLReportGenerator
from .utils import extract_test_name_from_filename, categorize_image_file

try:
    from ._version import __version__
except ImportError:
    __version__ = "unknown"

__all__ = [
    "StoreFailedMplPlugin",
    "ProgressTracker",
    "CleanupManager",
    "HTMLReportGenerator",
    "extract_test_name_from_filename",
    "categorize_image_file",
]
