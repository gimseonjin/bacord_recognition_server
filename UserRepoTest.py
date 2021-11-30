from User import User
from UserRepository import UserRepository
from Item import Item
from ItemRepository import ItemRepository

import cv2
from werkzeug.utils import secure_filename


userRepository = UserRepository()
itemRepository = ItemRepository()

item = itemRepository.read("1")
print(item)

img = cv2.imread(item.img)
cv2.imshow("test",img)

while cv2.waitKey(32) < 0:
    cv2.imshow("test",img)
