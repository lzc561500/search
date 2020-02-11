import pytest
from base.base_yml import Data_key
data=Data_key()


@pytest.mark.parametrize("args",data.data_yml_key("test.yml","test_login"))
def test_login(args,userName,password):
    userName = args[userName]
    password = args[password]
    print(userName)
    print(password)


if __name__ == '__main__':
    test_login()