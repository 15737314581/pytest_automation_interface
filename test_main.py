# coding=utf-8
from case.api_test import CommonTestCase
from config.excel_reader import ExcelReader
import pytest

class TestApiTest:
    def test01(self):
        app = CommonTestCase()
        reader = ExcelReader()
        models = reader.reader('Sheet1')
        app.runAllcase('Sheet1', models)


if __name__ == '__main__':
    pytest.main(['test_main.py::TestApiTest::test01',
                 '-vs',
                 '--capture=sys',
                 '--self-contained-html',
                 '--html=./data/report.html'])
