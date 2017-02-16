#!/usr/bin/python3
"""
The TestConsole Module defines a TestConsole class that
inherits from unittest.TestCase for testing Hosh class, an interactive
shell based on cmd.Cmd
"""
import sys
import unittest
from unittest import mock
from unittest.mock import patch
from io import StringIO
from test import support
from test.support import captured_stdout, captured_stderr
from console import Hosh

"""
subclassing from TestCase which is a base class of "unittest"
"""
class TestConsole(unittest.TestCase): 
    """
    Create automated tests for interactive shell based on cmd module
    """
    no_instance = "** no instance found **\n"
    no_class = "** class doesn't exist **\n"
    missing_class = "** class name missing **\n"
    missing_id = "** instance id missing **\n"
    
    def setUp(self):
        """setup method for Console Test Class"""
        self.mock_stdin = unittest.mock.create_autospec(sys.stdin)
        self.mock_stdout =unittest.mock.create_autospec(sys.stdout)

    def create(self, server=None):
        """create method is a helper function testing Hosh class"""
        return Hosh(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def _last_write(self, nr=None):
        """:return: last 'n' output lines, incomplete"""
        if nr is None:
            return self.mock_stdout.write.call_args[0][0]
        return "".join(map(lambda c: c[0][0], self.mock_stdout.write.call_args_list[-nr:]))

    def test_help(self):
        """help command"""

    def test_exit(self):
        """exit command"""
        cli = self.create()
        self.assertTrue(cli.onecmd("quit"))

    def test_EOF(self):
        """exit command"""
        cli = self.create()
        self.assertTrue(cli.onecmd("EOF"))


    def test_destroy_object(self):
        """test method for do_destroy"""
        cli = self.create()
        bad_input = 'destroy BaseModel This-is-testing-98'
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.assertFalse(cli.onecmd(bad_input))
        self.assertEqual('** no instance found **', '** no instance found **')

    def test_update(self):
        """test do_update"""
        cli = self.create()
        bad_input = 'update BaseModel This-is-testing-98'
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.assertFalse(cli.onecmd(bad_input))
        self.assertEqual('** value missing **', '** value missing **')

    def test_all(self):
        """
        test do_all
        store output in fakeOutput
        """
        cli = self.create()
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.assertFalse(cli.onecmd('classname.all()'))
        self.assertEqual("** class doesn't exist **",
                         "** class doesn't exist **")

suite = unittest.TestLoader().loadTestsFromTestCase(TestConsole)
unittest.TextTestRunner(verbosity = 2).run(suite)
