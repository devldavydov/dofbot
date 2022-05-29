import pytest

from dofbot.dofcalculator.dofqueryparser import DofQueryParser
from dofbot.dofcalculator.exceptions import DofCalculatorInvalidQuery


def test_query_parser():
    assert (20, None, None) == DofQueryParser.parse_query('FL=20')
    assert (20, None, 15.0) == DofQueryParser.parse_query('FL=20,FD=15')
    assert (20, 2.8, None) == DofQueryParser.parse_query('FL=20,F=2.8')
    assert (20, 2.8, 15.0) == DofQueryParser.parse_query('FL=20,F=2.8,FD=15')
    assert (20, 2.8, 15.0) == DofQueryParser.parse_query('   FL=20  , F=2.8,   FD=15   ')

    invalid_queries = ('foobar',
                       'FL=-1', 'FL=1.5', 'FL=abc',
                       'FL=10,F=-1', 'FL=10,F=abc', 'FL=10,F=2.7',
                       'FL=10,FD=-1', 'FL=10,FD=abc',
                       'FL=abc,F=2.8,FD=10', 'FL=20,F=abc,FD=10', 'FL=20,F=2.8,FD=abc')
    for query in invalid_queries:
        with pytest.raises(DofCalculatorInvalidQuery):
            DofQueryParser.parse_query(query)
