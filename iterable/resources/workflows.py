from .utils import Mapper

from .base import Resource


class Workflows(Resource):

    def trigger_workflow(self,
                         workflow_id,
                         email=None,
                         data_fields=None,
                         list_id=None):
        resource = "/api/workflows/triggerWorkflow"
        payload = {}
        payload["workflowId"] = workflow_id
        payload["email"] = email
        payload["dataFields"] = data_fields
        payload["listId"] = list_id
        return self.client.post(resource, data=payload)
