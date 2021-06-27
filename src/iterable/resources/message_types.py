from .base import Resource


class MessageTypes(Resource):

    def list(self):
        resource = "/api/messageTypes"
        return self.client.get(resource)
