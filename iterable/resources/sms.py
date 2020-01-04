from .base import Resource

class SmsMessage(Resource):

    def send(
            self,
            campaign_id,
            recipient_email,
            message_medium,
            data_fields=None,
            send_at=None,
            allow_repeat_marketing_sends=None,
    ):

        resource = "/api/sms/target"

        payload = {}

        payload["campaignId"] = campaign_id

        payload["recipientEmail"] = recipient_email

        if isinstance(message_medium, dict):
            payload["messageMedium"] = message_medium
        else:
            raise Exception('message medium is not in Dictionary format')

        if data_fields is not None:
            payload["dataFields"] = data_fields

        if send_at is not None:
            payload["sendAt"] = send_at

        if allow_repeat_marketing_sends is not None:
            payload["allowRepeatMarketingSends"] = allow_repeat_marketing_sends

        return self.client.post(resource, data=payload)
