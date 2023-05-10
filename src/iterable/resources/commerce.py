from .base import Resource


class Commerce(Resource):

    def track_purchase(self,
                       user,
                       items,
                       total,
                       campaign_id=None,
                       template_id=None,
                       created_at=None,
                       data_fields=None):
        resource = "/api/commerce/trackPurchase"
        payload = {}
        payload["user"] = user
        if not isinstance(items, (list, tuple)):
            items = [items]
        payload["items"] = items
        payload["total"] = total
        payload["campaignId"] = campaign_id
        payload["templateId"] = template_id
        payload["createdAt"] = created_at
        payload["dataFields"] = data_fields
        return self.client.post(resource, data=payload)

    def update_cart(self, user=None, items=None):
        resource = "/api/commerce/updateCart"
        payload = {}
        payload["user"] = user
        if not isinstance(items, (list, tuple)):
            items = [items]
        payload["items"] = items
        return self.client.post(resource, data=payload)
