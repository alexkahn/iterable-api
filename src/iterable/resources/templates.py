from .utils import Mapper

from .base import Resource


class Template:
    attributes = set((
        'bcc_emails',
        'cache_data_feed',
        'cc_emails',
        'client_template_id',
        'creator_user_id',
        'data_feed_id',
        'from_email',
        'from_name',
        'google_analytics_campaign_name',
        'html',
        'link_parameters',
        'locale',
        'merge_data_feed_context',
        'message_type_id',
        'name',
        'plain_text',
        'preheader_text',
        'reply_to_email',
        'subject',
    ))

    def __init__(self, **attrs):
        for attr in self.attributes:
            setattr(self, attr, attrs.get(attr, None))

    def to_dict(self):
        intermediate = {}
        for attr, value in self.__dict__.items():
            if attr in self.attributes:
                intermediate[attr] = value
        return intermediate

class Email(Resource):
    mapper = Mapper({
        "bcc_emails": "bccEmails",
        "cache_data_feed": "cacheDataFeed",
        "cc_emails": "ccEmails",
        "client_template_id": "clientTemplateId",
        "creator_user_id": "creatorUserId",
        "data_feed_id": "dataFeedId",
        "from_email": "fromEmail",
        "from_name": "fromName",
        "google_analytics_campaign_name": "googleAnalyticsCampaignName",
        "html": "html",
        "link_parameters": "linkParams",
        "locale": "locale",
        "merge_data_feed_context": "mergeDataFeedContext",
        "message_type_id": "messageTypeId",
        "metadata": "metadata",
        "name": "name",
        "plain_text": "planText",
        "preheader_text": "preheaderText",
        "reply_to_email": "replyToEmail",
        "subject": "subject",
    })

    def get(self, template_id, locale):
        resource = "/api/templates/email/get"
        payload = {}
        payload["templateId"] = template_id
        if locale is not None:
            payload["locale"] = locale
        return self.client.get(resource, params=payload)

    def update(self, template_id, **kwargs):
        """
        Update a template.
        """
        resource = "/api/templates/email/update"
        assert template_id is not None, "Template ID not provided"
        payload = self.mapper.remap(kwargs)
        return self.client.post(resource, data=payload)

    def upsert(self, **kwargs):
        """
        Create or update a template.
        """
        resource = "/api/templates/email/upsert"
        payload = self.mapper.remap(kwargs)
        return self.client.post(resource, data=payload)


class Push(Resource):
    mapper = Mapper({
        "created_at": "createdAt",
        "updated_at": "updatedAt",
        "name": "name",
        "message": "message",
        "payload_content": "payload",
        "badge": "badge",
        "locale": "locale",
        "message_type_id": "messageTypeId",
        "sound": "sound",
        "deeplink": "deeplink",
        "client_template_id": "clientTemplateId",
        "campaign_id": "campaignId",
    })

    def get(self, template_id, locale=None):
        resource = "/api/templates/push/get"
        payload = {}
        payload["templateId"] = template_id
        payload["locale"] = locale
        return self.client.get(resource, params=payload)

    def update(self, template_id, **kwargs):
        """
        created_at=None,
        updated_at=None,
        name=None,
        message=None,
        payload_content=None,
        badge=None,
        locale=None,
        message_type_id=None,
        sound=None,
        deeplink=None,
        client_template_id=None,
        campaign_id=None):
        """
        resource = "/api/templates/push/update"
        data = self.mapper.remap(kwargs)
        data["templateId"] = template_id
        return self.client.post(resource, data=data)

    def upsert(self, client_template_id, **kwargs):
        """
        name=None,
        message=None,
        payload_content=None,
        badge=None,
        locale=None,
        message_type_id=None,
        sound=None,
        deeplink=None,
        campaign_id=None):
        """
        resource = "/api/templates/push/upsert"
        data = self.mapper.remap(kwargs)
        data["clientTemplateId"] = client_template_id
        return self.client.post(resource, data=data)

class Sms(Resource):
    mapper = Mapper({
        "campaign_id": "campaignId",
        "created_at": "createdAt",
        "updated_at": "updatedAt",
        "name": "name",
        "message": "message",
        "locale": "locale",
        "message_type_id": "messageTypeId",
        "image_url": "imageUrl",
        "client_template_id": "clientTemplateId",
    })

    def get(self, template_id, locale=None):
        resource = "/api/templates/sms/get"
        payload = {}
        payload["templateId"] = template_id
        payload["locale"] = locale
        return self.client.get(resource, params=payload)

    def update(self, template_id, **kwargs):
        """
        created_at=None,
        updated_at=None,
        name=None,
        message=None,
        locale=None,
        message_type_id=None,
        image_url=None,
        client_template_id=None,
        campaign_id=None):
        """
        resource = "/api/templates/sms/update"
        payload = self.mapper.remap(kwargs)
        payload["templateId"] = template_id
        return self.client.post(resource, data=payload)

    def upsert(self, client_template_id, **kwargs):
        """
        name=None,
        message=None,
        locale=None,
        message_type_id=None,
        image_url=None,
        campaign_id=None):
        """
        resource = "/api/templates/sms/upsert"
        payload = self.mapper.remap(kwargs)
        payload["clientTemplateId"] = client_template_id
        return self.client.post(resource, data=payload)


class Templates(Resource):
    iterable_template_types = set(("Base", "Blast", "Triggered", "Workflow"))
    iterable_message_mediums = set(("Email", "Push", "InApp", "SMS"))

    def __init__(self, client):
        super().__init__(client)
        self.email = Email(client)
        self.push = Push(client)
        self.sms = Sms(client)

    def list(self,
             template_type=None,
             message_medium=None,
             start_date_time=None,
             end_date_time=None):
        resource = "/api/templates"
        params = {}

        if template_type is not None and template_type in self.iterable_template_types:
            params["templateType"] = template_type

        elif template_type is not None and template_type not in self.iterable_template_types:
            raise TypeError(
                "It looks like you listed an incorrect template type '%s'" %
                template_type)

        if message_medium is not None and message_medium in self.iterable_message_mediums:
            params["messageMedium"] = message_medium

        elif message_medium is not None and message_medium not in self.iterable_message_mediums:
            raise TypeError(
                "It looks like you listed an incorrect message medium '%s'" %
                message_medium)

        if start_date_time is not None:
            params["startDateTime"] = start_date_time

        if end_date_time is not None:
            params["endDateTime"] = end_date_time

        return self.client.get(resource, params=params)

    def get_by_client(self, client_template_id):
        resource = "/api/templates/getClientTemplateId"
        payload = {}
        payload["clientTemplateId"] = client_template_id
        return self.client.get(resource, params=payload)
