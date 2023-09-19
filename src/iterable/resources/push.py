from .base import Resource

from .utils import Mapper


class PushNotification(Resource):

    mapper = Mapper(
        {
            "campaign_id": "campaignId",
            "recipient_email": "recipientEmail",
            "message_medium": "messageMedium",
            "data_fields": "dataFields",
            "send_at": "sendAt",
            "allow_repeat_marketing_sends": "allowRepeatMarketingSends",
            "metadata": "metadata",
        }
    )

    def send(self, **kwargs):
        resource = "/api/push/target"
        payload = self.mapper.remap(kwargs)
        return self.client.post(resource, data=payload)
