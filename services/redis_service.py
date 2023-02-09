import redis as r
import os
from dotenv import load_dotenv

class RedisService(object):
    def __init__(self):
        load_dotenv()
        host = os.getenv("REDIS_HOST")
        port = os.getenv("REDIS_PORT")
        db = os.getenv("REDIS_DB")
        pwd = os.getenv("REDIS_PASSWORD")

        self.redis_obj = r.Redis(host=host, port=port,password=pwd,db=db)

    def Set(self, key: str, value: str):
        self.redis_obj.set(key, value)

    def Get(self, key:str):
        return self.redis_obj.get(key)

    def Delete(self, key:str):
        self.redis_obj.delete(key)
