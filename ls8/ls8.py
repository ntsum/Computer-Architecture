#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()

cpu.load(f'{sys.argv[0]}')
cpu.run()