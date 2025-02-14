from datetime import datetime
from json import loads
from typing import Dict, Optional


class DataItem:
    def __init__(self, data: Dict[str, any]):
        self._id = data['id']
        self._active = data['active']
        self._valid = data['valid']
        self._create_time = datetime.fromisoformat(data['createTime'])
        self._key = data['key']
        self._sync_id = data['syncId']
        self._search_value = data['searchValue']
        self._hash = data['hash']
        self._content = loads(data['content']) if data['content'] else None
        self._source_update_time = datetime.fromisoformat(data['sourceUpdateTime']) if data['sourceUpdateTime'] else None
        self._content_update_time = datetime.fromisoformat(data['contentUpdateTime'])
        self._dataset_id = data['dataset']
        self._execution_id = data['execution']
        self._depend_on_id = data['dependOn']

    @property
    def id(self) -> int:
        return self._id

    @property
    def active(self) -> bool:
        return self._active

    @property
    def valid(self) -> bool:
        return self._valid

    @property
    def create_time(self) -> datetime:
        return self._create_time

    @property
    def key(self) -> str:
        return self._key

    @property
    def sync_id(self) -> Optional[int]:
        return self._sync_id

    @property
    def search_value(self) -> Optional[str]:
        return self._search_value

    @property
    def hash(self) -> str:
        return self._hash

    @property
    def content(self) -> Optional[Dict[str, any]]:
        return self._content

    @property
    def source_update_time(self) -> Optional[datetime]:
        return self._source_update_time

    @property
    def content_update_time(self) -> datetime:
        return self._content_update_time

    @property
    def dataset_id(self) -> int:
        return self._dataset_id

    @property
    def execution_id(self) -> Optional[int]:
        return self._execution_id

    @property
    def depend_on_id(self) -> Optional[int]:
        return self._depend_on_id

