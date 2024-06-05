from models.utils import generate_uuid


class Request:
    def __init__(self, user_id, device_id, ip_addr):
        self.id = generate_uuid()
        self.user_id = user_id
        self.device_id = device_id
        self.ip_addr = ip_addr

