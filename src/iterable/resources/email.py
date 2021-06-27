from .utils import Mapper

from .base import Resource


class EmailMessage(Resource):

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
        resource = "/api/email/target"
        payload = self.mapper.remap(kwargs)
        return self.client.post(resource, data=payload)

    def view_in_browser(self, email, message_id):
        resource = "/api/email/viewInBrowser"
        payload = {}
        payload["email"] = str(email)
        payload["messageId"] = str(message_id)
        return self.client.get(resource, params=payload)
