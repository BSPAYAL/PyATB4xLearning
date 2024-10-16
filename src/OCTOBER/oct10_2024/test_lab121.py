# Fixture - Concept in python
# You can use the fixture
# context to the test.
# Similar - pre condition, post condition.


# Pre Condition - token, booking Id - Fixture
# test_Update_negative 1
# test_Update_postitive 2

#u can created unlimited no of common functions as fixtures
import pytest

@pytest.fixture()
def create_token():
    return "abc"

@pytest.fixture()
def create_booking_id():
    return 1

@pytest.fixture()
def read_excel_file():
    return "xyz"

@pytest.fixture()
def read_json_file():
    return "{}"

#u can use them
def test_consume(create_token,create_booking_id,read_json_file,read_excel_file):
    print(create_token)
    print(create_booking_id)
    print(read_json_file)
    print(read_excel_file)


#Fixtures are normal functions that can be used anywhere , can be used in  two different testcases also.

