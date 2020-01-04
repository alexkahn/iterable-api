from .base import Resource


class Lists(Resource):

    def list(self):
        resource = "/api/lists"
        return self.client.get(resource)

    def create(self, list_name):
        resource = "/api/lists"
        payload = {}
        payload["name"] = str(list_name)
        return self.client.post(resource, data=payload)

    def delete(self, list_id):
        resource = f"/api/lists/{str(list_id)}"
        return self.client.delete(resource)

    def user_count(self, list_id):
        resource = f"/api/lists/{str(list_id)}/size"
        return self.client.get(resource)

    def users(self, list_id):
        resource = "/api/lists/getUsers"
        payload = {}
        payload["listId"] = list_id
        return self.client.get(resource, params=payload)

    def add_subscribers(self, list_id, subscribers):
        resource = "/api/lists/subscribe"
        payload = {}
        payload["listId"] = list_id
        if not isinstance(subscribers, (list, tuple)):
            subscribers = [subscribers]
        payload["subscribers"] = subscribers
        return self.client.post(resource, data=payload)

    def remove_subscribers_to_list(self,
                                   list_id,
                                   subscribers,
                                   campaign_id=None,
                                   channel_unsubscribe=False):
        resource = "/api/lists/unsubscribe"
        payload = {}
        payload["listId"] = list_id
        if not isinstance(subscribers, (tuple, list)):
            subscribers = [subscribers]
        payload["subscribers"] = subscribers
        payload["campaignId"] = campaign_id
        payload["channelUnsubscribe"] = channel_unsubscribe
        return self.client.post(resource, data=payload)
