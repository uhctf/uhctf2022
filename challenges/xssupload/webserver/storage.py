from datetime import timedelta
from typing import Optional
from uuid import uuid4
from uuid import UUID
from redis import Redis
from os import getenv
from json import dumps

REDIS = Redis(
    host="redis",
    port=6379)

LEVEL = getenv("LEVEL")
INTERNAL_HOSTNAME = getenv("INTERNAL_HOSTNAME")

TIMEOUT = timedelta(minutes=10)


def create_item(file: bytes) -> str:
    """Adds the item to the storage. Returns a uid for the file."""
    uuid = uuid4()
    REDIS.set("{}_{}".format(LEVEL, uuid), file, TIMEOUT)
    return str(uuid)


def lookup_item(uuid: str) -> Optional[bytes]:
    try:
        uuid = UUID(uuid)
    except ValueError as ve:
        print(ve)
        return None
    key = "{}_{}".format(LEVEL, uuid)
    print(key)
    item = REDIS.get(key)
    return item


def submit_dmca_request(uuid: str):
    REDIS.publish("dmca", dumps(
        {'level': LEVEL, 'base_url': INTERNAL_HOSTNAME, 'uuid': uuid}))
