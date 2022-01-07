class ResultDto:
    def __init__(self,result,msg,data):
        self.result = result
        self.msg = msg
        self.data = data
    def toJSON(self):
        return {"result": self.result, "msg": self.msg, "data": self.data}
    
        