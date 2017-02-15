#!/usr/bin/python3
"""
The TestConsole Module defines a TestConsole class that
inherits from unittest.TestCase for testing Hosh class, an interactive
shell based on cmd.Cmd
credit of  "test_create_object"etc, for this module goes to Danton Rodriguez
(https://github.com/p0516357)
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

    def test_create_object(self):
        """test method for do_create method errors"""
        cli = self.create()
        with captured_stdout() as stdout, captured_stderr() as stderr:
            expected = "** class name missing **\n"
            self.assertFalse(cli.onecmd("create"))
            self.assertEqual(expected, stdout.getvalue())

        with captured_stdout() as stdout, captured_stderr() as stderr:
            expected = "** class doesn't exist **\n"
            self.assertFalse(cli.onecmd("create airplanes"))
            self.assertEqual(expected, stdout.getvalue())
        

    def test_show_object(self):
        """test method for do_show method errors"""
        cli = self.create()
        with captured_stdout() as stdout, captured_stderr() as stderr:
            self.assertFalse(cli.onecmd("show"))
            self.assertEqual(TestConsole.missing_class, stdout.getvalue())
        with captured_stdout() as stdout, captured_stderr() as stderr:
            self.assertFalse(cli.onecmd("show Korea"))
            self.assertEqual(TestConsole.no_class, stdout.getvalue())
        with captured_stdout() as stdout, captured_stderr() as stderr:
            self.assertFalse(cli.onecmd("show BaseModel AA"))
            self.assertEqual(TestConsole.no_instance, stdout.getvalue())
        with captured_stdout() as stdout, captured_stderr() as stderr:
            self.assertFalse(cli.onecmd("show BaseModel"))
            self.assertEqual(TestConsole.missing_id, stdout.getvalue())
        

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
