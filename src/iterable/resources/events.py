from .base import Resource


class Events(Resource):
    def get(self, email, limit=None):
        resource = "/api/events/" + str(email)
        payload = {}
        if limit is not None and limit <= 200:
            payload["limit"] = limit
        return self.client.get(resource, params=payload)

    def consume_in_app_notification(
        self, message_id, email=None, user_id=None, button_index=None
    ):
        resource = "/api/events/inAppConsume"
        payload = {}
        payload["messageId"] = str(message_id)
        payload["email"] = email
        payload["userId"] = user_id
        payload["buttonIndex"] = button_index
        return self.client.post(resource, data=payload)

    def track(
        self,
        event_name=None,
        email=None,
        created_at=None,
        data_fields=None,
        user_id=None,
        campaign_id=None,
        template_id=None,
        event_id=None,
    ):
        resource = "/api/events/track"
        payload = {}
        payload["eventName"] = str(event_name)
        payload["email"] = email
        payload["createdAt"] = created_at
        payload["dataFields"] = data_fields
        payload["userId"] = user_id
        payload["campaignId"] = campaign_id
        payload["templateId"] = template_id
        payload["id"] = event_id
        return self.client.post(resource, data=payload)

    def track_in_app_click(
        self, message_id, email=None, user_id=None, button_index=None
    ):
        resource = "/api/events/trackInAppClick"
        payload = {}
        payload["messageId"] = str(message_id)
        payload["email"] = email
        payload["userId"] = user_id
        payload["buttonIndex"] = button_index
        return self.client.post(resource, data=payload)

    def track_in_app_open(
        self, message_id, email=None, user_id=None, button_index=None
    ):
        resource = "/api/events/trackInAppOpen"
        payload = {}
        payload["messageId"] = str(message_id)
        payload["email"] = email
        payload["userId"] = user_id
        payload["buttonIndex"] = button_index
        return self.client.post(resource, data=payload)

    def track_push_open(
        self,
        campaign_id,
        email=None,
        user_id=None,
        template_id=None,
        message_id=None,
        created_at=None,
        data_fields=None,
    ):
        resource = "/api/events/trackPushOpen"
        payload = {}
        payload["CampaignId"] = campaign_id
        payload["email"] = email
        payload["userId"] = user_id
        payload["templateId"] = template_id
        payload["messageId"] = message_id
        payload["createdAt"] = created_at
        payload["dataFields"] = data_fields
        return self.client.post(resource, data=payload)

    def track_web_push_click(
        self,
        email=None,
        user_id=None,
        message_id=None,
        campaign_id=None,
        template_id=None,
    ):
        resource = "/api/events/trackWebPushClick"
        payload = {}
        payload["messageId"] = str(message_id)
        payload["email"] = email
        payload["userId"] = user_id
        payload["campaignId"] = campaign_id
        payload["templateId"] = template_id
        return self.client.post(resource, data=payload)
