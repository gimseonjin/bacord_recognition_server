class ItemResultDto:
    def __init__(self,result,msg,item,di):
        self.result = result
        self.msg = msg
        self.item = item
        self.di = di

    def toJSON(self):
        return {"result": self.result, "msg": self.msg, "item": self.item, "di":self.di}

    def __eq__(self, other): 
        return self.result == other.result and self.msg == other.msg and self.item == other.item and self.di == other.di

    