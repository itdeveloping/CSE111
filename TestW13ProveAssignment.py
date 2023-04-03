from W13ProveAssignment import dbToFile, \
    dbConnect, dbSelect
import pytest


def test_dbConnect():
    assert dbConnect('dbuser', 'ABCD1234#','127.0.0.1','dbloan') == "Hola"




# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
    