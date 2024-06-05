from enum import Enum

class RATE_LIMITER_TYPE(Enum):
    IP_RL = 'ip'
    DEVICE_RL = 'device'
    USER_RL = 'user'