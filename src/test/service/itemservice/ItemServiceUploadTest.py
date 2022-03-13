
from src.main.item.service.ItemService import ItemService
from src.main.item.infra.ItemRepositoryDataSourceImple import ItemRepositoryDataSourceImple
from werkzeug.utils import secure_filename
import numpy as np
import cv2
import pytest

itemRepository = ItemRepositoryDataSourceImple()
itemService = ItemService(itemRepository)

def test_success_upload_read_frame():

    # given
    targets = []
    value_results = []
    index_results = []

    for i in range(1,24):
        targets.append("barcode_" + str(i) + ".jpeg")

    # when
    for target in targets:

        img = cv2.imread('static/uploads/' + secure_filename(target))

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        '''
        kernel_sharpen_1 = np.array([[1,-2,1],[-2,5,-2],[1,-2,1]])

        f_image = cv2.filter2D(gray,-1,kernel_sharpen_1)

        ret, t_image = cv2.threshold(f_image, 127, 255, cv2.THRESH_BINARY)
        '''
        result = itemService.read_frame(gray)

        value_results.append(result.result)

    
    for index, result in enumerate(value_results):
        if result:
            index_results.append(index)

    point = len(index_results) / len(targets)

    # then
    print()
    print(f"point : {point}")
    assert point > 0.95