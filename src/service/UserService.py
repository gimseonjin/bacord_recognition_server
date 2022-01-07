from src.infra.UserRepository import UserRepository
from src.domain.User import User

class UserService:
    def __init__(self, userRepository: UserRepository):
        self.userRepository = userRepository

    def loginService(self, params):
        user = self.userRepository.read(params["id"])

        if((user == False) or (params["pwd"] != user.pwd) or (params["m_type"] != user.m_type)):
            result = False
            msg = "false"
        else:
            result = True
            msg = "success"

    def signUpService(self, params):
        user:User = self.userRepository.read(params["id"])

        if not user:
            self.userRepository.create(User(
                params['id'], params['pwd'], params['name'], params['p_number'], params['m_type']))
            result = True
            msg = "success"