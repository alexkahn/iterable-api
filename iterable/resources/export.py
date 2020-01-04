from .base import Resource


class Export(Resource):
    date_ranges = set(("Today", "Yesterday", "BeforeToday", "All"))
    formats = set(("csv", "json"))

    def export_data(self,
                    data_type_name=None,
                    date_range=None,
                    delimiter=None,
                    start_date_time=None,
                    end_date_time=None,
                    omit_fields=None,
                    only_fields=None,
                    campaign_id=None,
                    format=None,
                    chunk_size=1024,
                    path=None,
                    return_response_object=False):
        call = f"/api/export/data.{format}" if format in self.formats else "json"
        payload = {}
        payload["dataTypeName"] = data_type_name
        payload["startDateTime"] = start_date_time
        payload["endDateTime"] = end_date_time
        payload["omitFields"] = omit_fields
        payload["onlyFields"] = only_fields
        payload["campaignId"] = campaign_id
        if date_range in self.date_ranges:
            payload["range"] = date_range
        return self.client.export_data_api(
            call=call,
            chunk_size=chunk_size,
            params=payload,
            path=path,
            return_response_object=return_response_object)
