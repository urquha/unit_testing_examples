from unittest.mock import patch, Mock
from  data.module_d import function_d

@patch('data.module_b.function_a')
def test_function_e(mock_function_a):
    # Replace function_a with a mock
    mock_function_a.return_value = "Mocked A"

    # Call function_e
    result = function_d()

    # Assert something about the result
    assert result == "Mocked A", "Function E did not return the expected result"

# Call the test function
test_function_e()