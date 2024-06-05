import datetime

from models.Enums import RATE_LIMITER_TYPE
from models.RateLimiter import RateLimiter, UserRateLimiter, DeviceRateLimiter, IPAddressRateLimiter

def hello_world():
    print('Hello world')



class RateLimiterService:
    # request_timestamp[get_rate_limited_attribute(req)] = ts
    slot_in_queue = {}
    request_timestamp = {}

    @classmethod
    def get_slot_in_queue(cls, rl:RateLimiter, request):
        lookup_key = rl.get_lookup_key(request)
        allowed_reqs = rl.get_allowed_requests()
        q = cls.request_timestamp.get(lookup_key, [])
        return cls.find_slot_in_queue(rl.RL_TYPE)



    @classmethod
    def IPAddressRateLimiter(cls, num_of_req: int, time_in_sec: int):
        rl = IPAddressRateLimiter(num_of_req, time_in_sec)
        return rl

    @classmethod
    def DeviceRateLimiter(cls, num_of_req: int, time_in_sec: int):
        rl = DeviceRateLimiter(num_of_req, time_in_sec)
        return rl

    @classmethod
    def UserRateLimiter(cls, num_of_req: int, time_in_sec: int):
        rl = UserRateLimiter(num_of_req, time_in_sec)
        return rl

    @classmethod
    def find_slot_in_queue(cls, rl_type:RATE_LIMITER_TYPE):
        return cls.slot_in_queue[rl_type]

    @classmethod
    def execute_request_if_possible(cls, request1, rate_limiter: RateLimiter):
        cls.init_values(request1, rate_limiter)
        now = datetime.datetime.now()
        q_slot = cls.get_slot_in_queue(rate_limiter, request1)
        if q_slot==rate_limiter.num_of_req:
            cls.pop_and_update(request1, rate_limiter, now)
        else:
            cls.execute_request( rate_limiter,request1, q_slot, now )

    @classmethod
    def pop_and_update(cls, request1, rate_limiter, now_ts):
        result = now_ts - datetime.timedelta(seconds=rate_limiter.seconds)
        lookup_key = rate_limiter.get_lookup_key(request1)
        q = cls.request_timestamp[lookup_key]
        to_be_added = 0
        while(q and q[0]<result):
            q.pop(0)
            to_be_added += 1
        if to_be_added==0:
            print("cant execute, queue is full")
            return
        slot = len(q)
        q.extend([-1 for _ in range(to_be_added)])
        cls.execute_request(rate_limiter, request1, slot, now_ts)
        cls.request_timestamp[lookup_key] = q

    @classmethod
    def execute_request(cls, rate_limiter, request1, q_slot, now_ts):
        lookup_key = rate_limiter.get_lookup_key(request1)
        print("execute request", q_slot, cls.request_timestamp.get(lookup_key, []))
        cls.request_timestamp[lookup_key][q_slot] = now_ts
        cls.slot_in_queue[rate_limiter.RL_TYPE] = q_slot + 1
        hello_world()

    @classmethod
    def init_values(cls, request1, rate_limiter):
        lookup_key  = rate_limiter.get_lookup_key(request1)
        if lookup_key not in cls.request_timestamp:
            cls.request_timestamp[lookup_key] = [-1 for _ in range(rate_limiter.num_of_req)]
            cls.slot_in_queue[rate_limiter.RL_TYPE] = 0





