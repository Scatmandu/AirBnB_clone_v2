#!/usr/bin/python3
"""console Unittests"""


from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
import unittest
import sys


class TestConsole(unittest.TestCase):
    """tests for the console"""

    def test_create(self):
        """ test create """
        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("create widdly")
            self.assertEqual(file.getvalue(), "\n** class doesn't exist **\n")

    def test_show(self):
        """ test show """
        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("show widdly")
            self.assertEqual(file.getvalue(), "\n** class doesn't exist **\n")

    def test_destroy(self):
        """ test destroy """
        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("destroy widdly")
            self.assertEqual(file.getvalue(), "\n** class doesn't exist **\n")

    def test_all(self):
        """ test all """
        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("all widdly")
            self.assertEqual(file.getvalue(), "\n** class doesn't exist **\n")

    def test_update(self):
        """ test update """
        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("update widdly")
            self.assertEqual(file.getvalue(), "\n** class doesn't exist **\n")
