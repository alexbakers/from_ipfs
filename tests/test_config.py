#!/usr/bin/env python3

import sys
from from_ipfs.cli import config_command
import argparse


class MockArgs:
    pass


args = MockArgs()
config_command(args)
