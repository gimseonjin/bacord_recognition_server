from src.domain.dto.LoginResultDto import LoginResultDto
from src.domain.dto.SignUpResultDto import SignUpResultDto
from src.infra.UserRepository import UserRepository
from src.domain.User import User

class UserService:
    def __init__(self, userRepository: UserRepository):
        self.userRepository = userRepository

    def loginService(self, params):
        user = self.userRepository.read(params["id"])

        if((user == False) or (params["pwd"] != user.pwd) or (params["m_type"] != user.m_type)):
            return LoginResultDto(False, "login false", "")
        
        return LoginResultDto(True, "login success", user.name)

    def signUpService(self, params):
        user = self.userRepository.read(params["id"])

        if not user:
            self.userRepository.create(User(
                params['id'], params['pwd'], params['name'], params['p_number'], params['m_type']))
            return SignUpResultDto(True, "sign up success")

        return SignUpResultDto(False, "sign up false")
