from unittest.mock import patch, Mock
from  data.module_d import function_d
import pandas as pd
from pandas.testing import assert_frame_equal


@patch('data.module_b.function_a')
def test_function_d_with_mock(mock_function_a):
    # Replace function_a with a mock
    mock_function_a.return_value = "Mocked A"

    # Call function_d
    result = function_d()

    # Assert something about the result
    assert result == "Mocked A", "Function E did not return the expected result"

def test_function_d_no_mock():

    # Call function_d
    result = function_d()

    # Assert something about the result
    assert_frame_equal(result, pd.DataFrame())

