# -*- coding: utf-8 -*-
from typing import Optional, List

from brewtils import command, parameter


class TestParameter(object):
    def test_missing(self):
        class Bar(object):
            @parameter(key="foo")
            def _cmd(self, foo):
                return foo

        assert Bar()._cmd._command.get_parameter_by_key("foo").type is None

    def test_str(self):
        class Bar(object):
            @parameter(key="foo")
            def _cmd(self, foo: str):
                return foo

        assert Bar()._cmd._command.get_parameter_by_key("foo").type == "String"

    def test_int(self):
        class Bar(object):
            @parameter(key="foo")
            def _cmd(self, foo: int):
                return foo

        assert Bar()._cmd._command.get_parameter_by_key("foo").type == "Integer"

    def test_float(self):
        class Bar(object):
            @parameter(key="foo")
            def _cmd(self, foo: float):
                return foo

        assert Bar()._cmd._command.get_parameter_by_key("foo").type == "Float"

    def test_bool(self):
        class Bar(object):
            @parameter(key="foo")
            def _cmd(self, foo: bool):
                return foo

        assert Bar()._cmd._command.get_parameter_by_key("foo").type == "Boolean"

    def test_dict(self):
        class Bar(object):
            @parameter(key="foo")
            def _cmd(self, foo: dict):
                return foo

        assert Bar()._cmd._command.get_parameter_by_key("foo").type == "Dictionary"


class TestCommand(object):
    def test_str(self):
        class Bar(object):
            @command
            def _cmd(self, foo: str):
                return foo

        assert Bar()._cmd._command.get_parameter_by_key("foo").type == "String"


class TestBoth(object):
    def test_str_parameter_command(self):
        class Bar(object):
            @parameter(key="foo")
            @command
            def _cmd(self, foo: str):
                return foo

        assert Bar()._cmd._command.get_parameter_by_key("foo").type == "String"

    def test_str_command_parameter(self):
        class Bar(object):
            @command
            @parameter(key="foo")
            def _cmd(self, foo: str):
                return foo

        assert Bar()._cmd._command.get_parameter_by_key("foo").type == "String"


class TestContainers(object):
    def test_list(self):
        class Bar(object):
            @parameter(key="foo")
            def _cmd(self, foo: List[str]):
                return foo

        assert Bar()._cmd._command.get_parameter_by_key("foo").type == "String"


class TestOptional(object):
    def test_str(self):
        class Bar(object):
            @parameter(key="foo")
            def _cmd(self, foo: Optional[str]):
                return foo

        assert Bar()._cmd._command.get_parameter_by_key("foo").type == "String"