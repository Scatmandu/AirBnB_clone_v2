#!/usr/bin/python3
"""console Unittests"""


from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
import unittest
import json
import pep8
import sys
import os

class TestConsole(unittest.TestCase):
    """tests for the console"""