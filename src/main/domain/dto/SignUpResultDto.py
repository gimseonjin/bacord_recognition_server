class SignUpResultDto:
    def __init__(self,result,msg):
        self.result = result
        self.msg = msg
    def toJSON(self):
        return {"result": self.result, "msg": self.msg}