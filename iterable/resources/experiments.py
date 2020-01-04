from .base import Resource


class Experiments(Resource):
    def __init__(self, client):
        self.client = client

    def get_experiment_metrics(self,
                               experiment_id=None,
                               campaign_id=None,
                               start_date_time=None,
                               end_date_time=None):
        resource = "/api/experiments/metrics"
        payload = {}
        payload["experimentId"] = experiment_id
        payload["campaignId"] = campaign_id
        payload["startDateTime"] = start_date_time
        payload["endDateTime"] = end_date_time
        return self.client.get(resource, params=payload)
