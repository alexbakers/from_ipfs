#!/usr/bin/env python3
"""
Simple wrapper script for from_ipfs to access the config command directly.
"""

import from_ipfs

# Display the configuration information
print(f"from_ipfs configuration:")
print(f"  - Version: {from_ipfs.__version__}")
print(f"  - Cache directory: {from_ipfs.CACHE_DIR}")
print(f"  - IPFS gateways:")
for gateway in from_ipfs.GATEWAYS:
    print(f"    - {gateway}")

# Show environment variables
import os
print("\nEnvironment variables:")
print(f"  - FROM_IPFS_CACHE: {'Set to ' + os.environ.get('FROM_IPFS_CACHE') if 'FROM_IPFS_CACHE' in os.environ else 'Not set (using default)'}")
print(f"  - FROM_IPFS_GATEWAYS: {'Set to ' + os.environ.get('FROM_IPFS_GATEWAYS') if 'FROM_IPFS_GATEWAYS' in os.environ else 'Not set (using default)'}") 