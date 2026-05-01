"""Pytest fixtures for storage tests.

Patches _get_worksheet with an in-memory worksheet so tests run without
a live Google Sheets connection.
"""

import pytest
import src.storage.storage_handler as handler


class _InMemoryWorksheet:
    def __init__(self):
        self._rows = [["name", "email", "student_id", "major"]]  # header row

    def col_values(self, col: int) -> list[str]:
        return [row[col - 1] for row in self._rows if len(row) >= col]

    def append_row(self, row: list) -> None:
        self._rows.append(row)


@pytest.fixture(autouse=True)
def in_memory_worksheet(monkeypatch):
    ws = _InMemoryWorksheet()
    monkeypatch.setattr(handler, "_get_worksheet", lambda: ws)
