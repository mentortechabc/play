## library module
import pytest


def multiply(x, y):
    return x * y


## test module

@pytest.fixture()
def test_object():
    return 2 * 2


def test_numbers_3_4(test_object):
    assert multiply(3, test_object) == 12


def test_strings_a_3(test_object):
    assert multiply('a', test_object) == 'aaaa'


#
# def test_with_db_1():
#     db = make_test_db()
#     result = multiply(db, 1)
#     assert result == 'aaa'
#     db.close()
#
#
# def test_with_db_2():
#     db = make_test_db()
#     result = multiply(db, 2)
#     assert result == 'aaa'
#     db.close()


## setup/teardown for resource allocation

if 0:
    def setup_module(module):
        print("create DB")
        print("setup_module      module:%s" % module.__name__)


    def teardown_module(module):
        print("closing DB")
        print("teardown_module   module:%s" % module.__name__)


    def setup_function(function):
        print("setup_function    function:%s" % function.__name__)


    def teardown_function(function):
        print("teardown_function function:%s" % function.__name__)

if 0:
    @pytest.fixture(scope='module')
    def resource_a_setup(request):
        print('\nresources_a_setup()')

        def resource_a_teardown():
            print('\nresources_a_teardown()')

        request.addfinalizer(resource_a_teardown)


    def test_1_that_needs_resource_a(resource_a_setup):
        print('test_1_that_needs_resource_a()')


    def test_2_that_does_not():
        print('\ntest_2_that_does_not()')


    def test_3_that_does(resource_a_setup):
        print('\ntest_3_that_does()')

if 0:
    @pytest.fixture(scope="module")
    def db_connection(request):
        print("create db connection here")
        connection = ["my_connection"]

        yield connection

        print(f"closing db connection here")
        del connection

    def test_1(db_connection):
        db_connection.append("with some data")
        db_connection.append("with more data")

        result = len(db_connection)

        assert result == 3


    def test_2(db_connection):
        db_connection.append("with some data")
        db_connection.append("with more data")
        print(db_connection)
        assert len(db_connection) == 3


