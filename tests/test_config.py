#!/usr/bin/env python3

import argparse
import sys

from from_ipfs.cli import config_command


class MockArgs:
    pass


args = MockArgs()
config_command(args)
