from src.main.infra.datasource.IncomingRepositoryDataSourceImple import IncomingRepositoryDataSourceImple
from src.main.infra.datasource.ItemRepositoryDataSourceImple import ItemRepositoryDataSourceImple
from src.main.infra.datasource.UserRepositoryDataSourceImple import UserRepositoryDataSourceImple
from src.main.infra.datasource.RecordRepositoryDataSourceImple import RecordRepositoryDataSourceImple
from src.main.service.IncomingService import IncomingService
from src.main.service.ItemService import ItemService
from src.main.service.UserService import UserService
from src.main.service.RecordService import RecordService



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
    