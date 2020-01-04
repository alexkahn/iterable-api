from .base import Resource


class Metadata(Resource):

    def list_available_tables(self):
        resource = "/api/metadata"
        return self.client.get(resource)

    def delete_all_metadata_from_table(self, table):
        resource = "/api/metadata" + str(table)
        return self.client.delete(resource)

    def list_keys_in_table(self, table, next_marker=None):
        resource = "/api/metadata/" + str(table)
        payload = {}
        if next_marker is not None:
            payload["nextMarket"] = next_marker
        return self.client.get(resource, params=payload)

    def delete_single_metadata_key_value(self, table, key):
        resource = "/api/metadata/" + str(table) + "/" + str(key)
        return self.client.delete(resource)

    def get_single_metadata_key_value(self, table, key):
        resource = "/api/metadata/" + str(table) + "/" + str(key)
        return self.client.get(resource)

    def create_or_replace_metadata(self, table, key, value):
        resource = "/api/metadata/" + str(table) + "/" + str(key)
        payload = {}
        if isinstance(value, dict):
            payload["value"] = value
        else:
            raise TypeError('value is not in object format')
        return self.client.put(resource, data=payload)
