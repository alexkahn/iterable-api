from datetime import datetime

from .utils import Mapper
from .base import Resource


class Campaigns(Resource):
    mapper = Mapper({
        'list_ids': "listIds",
        'template_id': "templateId",
        'suppression_list_ids': "supressionListIds",
        'send_at': "sendAt",
        'send_mode': "sendMode",
        'start_time_zone': "startTimeZone",
        'default_time_zone': "defaultTimeZone",
        'data_fields': "dataFields",
    })

    def list(self):
        resource = "/api/campaigns"
        return self.client.get(resource)

    def create(self, **kwargs):
        """
        name=None,
        list_ids=None,
        template_id=None,
        suppression_list_ids=None,
        send_at=None,
        send_mode=None,
        start_time_zone=None,
        default_time_zone=None,
        data_fields=None
        """
        resource = "/api/campaigns/create"
        assert kwargs.get('name') is not None, "Missing name for new campaign"
        assert kwargs.get(
            'list_ids'
        ) is not None, f"Lists for new campaign {kwargs.get('name')}"
        if not isinstance(kwargs.get('list_ids'), (list, tuple)):
            kwargs['list_ids'] = [kwargs['list_ids']]
        kwargs['send_at'] = str(
            kwargs.get('send_at')) if kwargs.get('send_at') else None
        kwargs['send_mode'] = str(
            kwargs.get('send_mode')) if kwargs.get('send_mode') else None
        kwargs['start_time_zone'] = str(kwargs.get(
            'start_time_zone')) if kwargs.get('start_time_zone') else None
        kwargs['default_time_zone'] = str(kwargs.get(
            'default_time_zone')) if kwargs.get('default_time_zone') else None
        payload = self.mapper.remap(kwargs)
        return self.client.post(resource, data=payload)

    def get_metrics(self,
                    campaign_id,
                    start_date_time=None,
                    end_date_time=None,
                    use_new_format=None):
        resource = "/api/campaigns/metrics"
        payload = {}
        if not isinstance(campaign_id, list):
            raise TypeError('campaign ids are not stored in list format')
        if len(campaign_id) >= 1:
            payload["campaignId"] = campaign_id
        else:
            raise ValueError('At least 1 campaign ID is necessary to get metrics')
        if isinstance(start_date_time, datetime):
            payload["startDateTime"] = start_date_time
        else:
            raise TypeError('Start date must be a datetime object')

        if isinstance(end_date_time, datetime):
            payload["endDateTime"] = end_date_time
        else:
            raise TypeError('End date must be a datetime object')

        if use_new_format is not None:
            payload["useNewFormat"] = use_new_format

        return self.client.get(resource, params=payload)

    def get_child_campaigns(self, campaign_id):
        resource = f"/api/campaigns/recurring/{str(campaign_id)}/childCampaigns"
        return self.client.get(resource)
