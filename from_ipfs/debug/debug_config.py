#!/usr/bin/env python
"""
Debug script for running the config command directly.
"""

import sys
import os

# Add debug output
print(f"Debug: Script path: {__file__}")
print(f"Debug: Current working directory: {os.getcwd()}")
print(f"Debug: Original sys.argv: {sys.argv}")

# Override sys.argv
sys.argv = ["from_ipfs", "config"]
print(f"Debug: New sys.argv: {sys.argv}")

# Import the main function
from from_ipfs.cli import main

# Run the main function
print("Debug: About to run main()")
result = main()
print(f"Debug: main() returned: {result}")
