import time
import datetime

from models.Enums import RATE_LIMITER_TYPE
from models.Request import Request


class RateLimiter:
    RL_TYPE = None
    num_of_requests = 0

    def __init__(self, num_of_req: int, time_in_sec: int, _type: RATE_LIMITER_TYPE=None):
        self.num_of_req = num_of_req
        self.seconds = time_in_sec
        self.RL_TYPE = _type

    @classmethod
    def get_lookup_key(cls, request: Request):
        lookup_key = cls.get_lookup_key(request)
        return lookup_key

    @classmethod
    def get_allowed_requests(cls):
        return cls.num_of_requests


class IPAddressRateLimiter(RateLimiter):
    num_of_requests = 0
    def __init__(self, num_of_req: int, time_in_sec: int):
        super().__init__(num_of_req, time_in_sec, _type=RATE_LIMITER_TYPE.IP_RL)

    @classmethod
    def get_lookup_key(cls, request: Request):
        return request.ip_addr


class DeviceRateLimiter(RateLimiter):
    num_of_requests = 0

    def __init__(self,num_of_req: int, time_in_sec: int):
        super().__init__(num_of_req, time_in_sec, _type = RATE_LIMITER_TYPE.DEVICE_RL)

    @classmethod
    def get_lookup_key(cls, request: Request):
        return request.device_id

class UserRateLimiter(RateLimiter):
    num_of_requests = 0

    def __init__(self, num_of_req: int, time_in_sec: int):
        super().__init__(num_of_req, time_in_sec, _type=RATE_LIMITER_TYPE.USER_RL)

    @classmethod
    def get_lookup_key(cls, request: Request):
        return request.user_id






