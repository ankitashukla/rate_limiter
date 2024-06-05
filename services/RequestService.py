from models.Request import Request


class RequestService:
    _requests = {}

    @classmethod
    def _request(cls, user_id, device_id, ip_addr):
        req = Request(user_id, device_id, ip_addr)
        cls._requests[req.id]  = req

        return req


