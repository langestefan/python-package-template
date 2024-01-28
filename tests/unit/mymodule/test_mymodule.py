"""Test my module."""
from __future__ import annotations

import pytest


class TestMyModule:
    """Test my module."""

    @pytest.fixture
    def some_fixture(self) -> bool:
        """Fixture."""
        return True

    def test_my_module(self, *, some_fixture: bool) -> None:
        """Test my module."""
        assert some_fixture

    def test_main(self) -> None:
        """Test main."""
        # pylint: disable=import-outside-toplevel
        from mypackage import __main__

        __main__.main()
