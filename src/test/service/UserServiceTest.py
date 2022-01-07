from src.main.domain.User import User
from src.main.service.UserService import UserService
from src.main.infra.datasource.UserRepositoryDataSourceImple import UserRepositoryDataSourceImple
from src.main.domain.dto.LoginResultDto import LoginResultDto
from src.main.domain.dto.SignUpResultDto import SignUpResultDto
import pytest

userRepository = UserRepositoryDataSourceImple()
userService = UserService(userRepository)

@pytest.fixture
def add_test_user():
    print("test")
    userRepository.create(User("test","test","test","01032320232",0))

def test_success_user_login(add_test_user):
    params = {"id" : "test" ,"pwd": "test" , "m_type" : 0}

    actual = userService.loginService(params)
    expected = LoginResultDto(True, "login success", "test")

    assert actual == expected

def test_fail_wrong_id_user_login(add_test_user):
    params = {"id" : "wrong_id" ,"pwd": "test" , "m_type" : 0}

    actual = userService.loginService(params)
    expected = LoginResultDto(False, "login fail", "")

    assert actual == expected

def test_fail_wrong_pwd_user_login(add_test_user):
    params = {"id" : "test" ,"pwd": "wrong_pwd" , "m_type" : 0}

    actual = userService.loginService(params)
    expected = LoginResultDto(False, "login fail", "")

    assert actual == expected

def test_fail_wrong_Mtype_user_login(add_test_user):
    params = {"id" : "test" ,"pwd": "test" , "m_type" : 1}

    actual = userService.loginService(params)
    expected = LoginResultDto(False, "login fail", "")

    assert actual == expected
