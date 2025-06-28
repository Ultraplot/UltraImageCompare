# UltraImageCompare

UltraImageCompare is a Matplotlib plugin designed to enhance your image comparison tests. It works seamlessly with Ultraplot and harnesses the power of `xdist` for parallel testing. This plugin provides advanced features such as real-time progress tracking, optimized artifact handling, and comprehensive HTML reporting for your visual tests.

## Features

- **Enhanced Image Comparison**: Optimizes comparisons by reducing artifacts and speeding up test execution.
- **Parallel Testing Support**: Leverage `xdist` to run tests in parallel across multiple CPUs.
- **Progress Tracking**: Visual feedback during test execution with a built-in progress bar.
- **HTML Reporting**: Automatically generate detailed HTML reports summarizing test results.
- **Deferred Cleanup**: Automatic post-test cleanup to optimize disk usage and resource management.
- **Utility Functions**: A set of helper functions to simplify test configuration and execution.

## Module Structure

- `core.py`: Contains the main plugin class and core test functionality.
- `progress.py`: Implements the progress bar and visual feedback.
- `cleanup.py`: Provides deferred cleanup routines and artifact optimization.
- `reporting.py`: Handles HTML report generation for test results.
- `utils.py`: Utility functions and helpers that support various test operations.

## Installation

To install UltraImageCompare, clone the repository and install the required dependencies. For example:

```bash
git clone https://github.com/Ultraplot/UltraImageCompare.git
cd UltraImageCompare
pip install .
```
