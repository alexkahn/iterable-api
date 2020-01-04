from .base import Resource


class WebPushNotification(Resource):

    def send(self,
             campaign_id,
             recipient_email,
             message_medium,
             data_fields=None,
             send_at=None,
             allow_repeat_marketing_sends=None):
        resource = "/api/webPush/target"
        payload = {}
        payload["campaignId"] = campaign_id
        payload["recipientEmail"] = recipient_email
        payload["messageMedium"] = message_medium
        payload["dataFields"] = data_fields
        payload["sendAt"] = send_at
        payload["allowRepeatMarketingSends"] = allow_repeat_marketing_sends
        return self.client.post(resource, data=payload)
