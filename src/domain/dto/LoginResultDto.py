class LoginResultDto:
    def __init__(self,result,msg,name):
        self.result = result
        self.msg = msg
        self.name = name
    def toJSON(self):
        return {"result": self.result, "msg": self.msg, "name": self.name}
    
        