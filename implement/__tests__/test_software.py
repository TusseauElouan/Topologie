from implement.software import Software
import pytest

@pytest.fixture
def create_software():
    return Software()

class TestSoftware:

    @pytest.mark.parametrize("data, expected_output", [
        ("Hello, World!", "Message: Hello, World!"),
        ("Testing 123", "Message: Testing 123"),
        ("Software Test", "Message: Software Test")
    ])
    def test_display_message(self,data, expected_output, create_software):
        result = create_software.display_message(data)
        assert result == expected_output