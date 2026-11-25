"""Тести додавання варіантів відповіді.

Пропускаються, якщо PyQt6/GUI недоступні.
"""

import pytest

try:
    from PyQt6.QtWidgets import QApplication
    app = QApplication.instance() or QApplication([])
    PYQT_AVAILABLE = True
except Exception:
    PYQT_AVAILABLE = False

pytestmark = pytest.mark.skipif(
    not PYQT_AVAILABLE,
    reason="PyQt6 або графічні бібліотеки недоступні"
)


def test_option_row_creation():
    from admin.tests_tab import OptionRow
    row = OptionRow("Варіант А", is_correct=True)
    text, correct = row.get_data()
    assert text == "Варіант А"
    assert correct is True


def test_option_row_empty():
    from admin.tests_tab import OptionRow
    row = OptionRow()
    text, correct = row.get_data()
    assert text == ""
    assert correct is False


def test_add_multiple_options():
    from admin.tests_tab import OptionRow
    rows = [OptionRow(f"Варіант {i+1}", is_correct=(i == 0)) for i in range(5)]
    assert len(rows) == 5
    assert rows[0].get_data()[1] is True


def test_option_row_expand_exists():
    from admin.tests_tab import OptionRow
    row = OptionRow("Довгий текст")
    assert hasattr(row, "expand_btn")
