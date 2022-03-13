from src.main.incoming.infra.InComingRepositoryDataSourceImple import IncomingRepositoryDataSourceImple
from src.main.item.infra.ItemRepositoryDataSourceImple import ItemRepositoryDataSourceImple
from src.main.user.infra.UserRepositoryDataSourceImple import UserRepositoryDataSourceImple
from src.main.record.infra.RecordRepositoryDataSourceImple import RecordRepositoryDataSourceImple
from src.main.incoming.service.IncomingService import IncomingService
from src.main.item.service.ItemService import ItemService
from src.main.user.service.UserService import UserService
from src.main.record.service.RecordService import RecordService



class Config(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)  
        return cls._instance                      

    def __init__(self):
        self._incomingRepository = IncomingRepositoryDataSourceImple()
        self._itemRepository = ItemRepositoryDataSourceImple()
        self._userRepository = UserRepositoryDataSourceImple()
        self._recordRepository = RecordRepositoryDataSourceImple()

        self._incomingService = IncomingService(self._incomingRepository)
        self._itemService = ItemService(self._itemRepository)
        self._userService = UserService(self._userRepository)
        self._recordService = RecordService(self._recordRepository)
    
    def getIncomingService(self):
        return self._incomingService
    
    def getItemService(self):
        return self._itemService
    
    def getUserService(self):
        return self._userService
    
    def getRecordService(self):
        return self._recordService
    