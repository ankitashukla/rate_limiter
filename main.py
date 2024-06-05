from time import sleep
from typing import Optional

from models.Enums import RATE_LIMITER_TYPE
from services.RateLimiterService import RateLimiterService
from services.RequestService import RequestService
from services.UserService import UserService


user1 = UserService.add_user('user 1')
request1 = RequestService()._request(user1.id, 'device1', 'ip1')
request2 = RequestService()._request(user1.id, 'device1', 'ip1')



number_of_requests = 1
time_in_seconds = 1
rate_limiter_ip = RateLimiterService.IPAddressRateLimiter(number_of_requests, time_in_seconds)
rate_limiter_device = RateLimiterService.DeviceRateLimiter(number_of_requests, time_in_seconds)
rate_limiter_user = RateLimiterService.UserRateLimiter(number_of_requests, time_in_seconds)

RateLimiterService.execute_request_if_possible(request1, rate_limiter_user)
RateLimiterService.execute_request_if_possible(request1, rate_limiter_user)
RateLimiterService.execute_request_if_possible(request1, rate_limiter_user)
RateLimiterService.execute_request_if_possible(request1, rate_limiter_user)
sleep(1)
RateLimiterService.execute_request_if_possible(request1, rate_limiter_user)

