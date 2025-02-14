from datetime import datetime
from typing import Union, Generator, Optional
from urllib.parse import quote

import requests

from .model import DataItem


class Rocinet:
    def __init__(self, access_token: str, list_size: int = 1000):
        self._access_token = access_token
        self._list_size = list_size

    def get_data_items(self, dataset: Union[str, int], content_update_after: Optional[datetime] = None, content_update_before: Optional[datetime] = None) -> Generator[DataItem, None, None]:
        filter_str = '&contentUpdateTime[>%3D]={}'.format(quote(content_update_after.isoformat())) if content_update_after is not None else ''
        filter_str += '&contentUpdateTime[<]={}'.format(quote(content_update_before.isoformat())) if content_update_before is not None else ''
        offset = 0
        stop = False
        while not stop:
            url = 'https://api.rocinet.com/datasets/{}/data_items?limit={}&offset={}&sort=createTime%2B{}'\
                .format(dataset, self._list_size, offset, filter_str)
            headers = {
                'Authorization': 'Bearer {}'.format(self._access_token),
                'Accept': 'application/json'
            }
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            items = response.json().get('items')
            for item in items:
                yield DataItem(item)
            offset += self._list_size
            stop = len(items) < self._list_size
