from .base import Resource


class InAppMessages(Resource):

    def get(self, email, count, user_id=None, platform=None, sdk_version=None):
        resource = "/api/inApp/getMessages"
        payload = {}
        payload["email"] = str(email)
        payload["count"] = count
        payload["userId"] = str(user_id)
        payload["platform"] = str(platform)
        payload["SDKVersion"] = sdk_version
        return self.client.get(resource, params=payload)

    def send(self,
             campaign_id,
             recipient_email,
             message_medium,
             data_fields=None,
             send_at=None,
             allow_repeat_marketing_sends=None):
        resource = "/api/inApp/target"
        payload = {}
        payload["campaignId"] = campaign_id
        payload["recipientEmail"] = recipient_email
        payload["messageMedium"] = message_medium
        payload["dataFields"] = data_fields
        payload["sendAt"] = send_at
        payload["allowRepeatMarketingSends"] = allow_repeat_marketing_sends
        return self.client.post(resource, data=payload)
