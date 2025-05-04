from collections.abc import Sequence
from urllib.parse import quote

from .base import Resource


class Users(Resource):

    def get(self, email=None, user_id=None):
        """Retreive one or more users by email or the user_id supplied to Iterable."""
        params = {}
        if isinstance(email, str):
            resource = f"/api/users/{quote(str(email))}"
        elif isinstance(email, Sequence):
            # NOTE: This doesn't actually do what you would expect, you can't actually get a list of users...
            resource = "/api/users/getByEmail"
            params["email"] = [str(e) for e in email]
        elif isinstance(user_id, (int, str)):
            resource = f"/api/users/byUserId/{quote(str(user_id))}"
        elif isinstance(user_id, Sequence):
            # NOTE: This doesn't actually do what you would expect, you can't actually get a list of users...
            resource = "/api/users/byUserId"
            params["userId"] = [str(uid) for uid in user_id]
        return self.client.get(resource, params=params)

    def delete(self, email=None, user_id=None):
        """Delete a user by email or user_id."""
        if email:
            resource = f"/api/users/{str(email)}"
        elif user_id:
            resource = f"/api/users/byUserId/{str(user_id)}"
        return self.client.delete(resource)

    def disable_device(self, token, email=None, user_id=None):
        """
        This request manually disable pushes to a device until it comes
        online again.
        """
        resource = "/api/users/disableDevice"
        payload = {}
        payload["token"] = str(token)
        payload["email"] = str(email)
        payload["userId"] = str(user_id)
        return self.client.post(resource, data=payload)

    def get_fields(self):
        resource = "/api/users/getFields"
        return self.client.get(resource)

    def get_sent_messages(
        self,
        email=None,
        user_id=None,
        limit=10,
        campaign_id=None,
        start_date_time=None,
        end_date_time=None,
        exclude_blast_campaigns=None,
        message_medium=None,
    ):
        """
        """
        resource = "/api/users/getSentMessages"
        channels = ["Email", "Push", "InApp", "SMS"]
        payload = {}
        payload["email"] = str(email)
        payload["userId"] = str(user_id)

        if limit is not None and limit <= 1000:
            payload["limit"] = int(limit)

        if campaign_id is not None:
            payload["campaignId"] = campaign_id

        if start_date_time is not None:
            payload["startDateTime"] = start_date_time

        if end_date_time is not None:
            payload["endDateTime"] = end_date_time

        if exclude_blast_campaigns is not None:
            payload["excludeBlastCampaigns"] = exclude_blast_campaigns

        if message_medium is not None and message_medium in channels:
            payload["messageMedium"] = str(message_medium)

        return self.client.get(resource, params=payload)

    def register_browser_token(self, browser_token, email=None, user_id=None):
        resource = "/api/users/registerBrowserToken"
        payload = {}
        payload["browserToken"] = str(browser_token)
        payload["email"] = email
        payload["userId"] = user_id
        return self.client.post(resource, data=payload)

    def register_device_token(self, device_token, email=None, user_id=None):
        resource = "/api/users/registerDeviceToken"
        payload = {}
        payload["device"] = device_token
        payload["email"] = email
        payload["userId"] = user_id
        return self.client.post(resource, data=payload)

    def update(
        self, email=None, data_fields=None, user_id=None, merge_nested_objects=None
    ):
        """
        The Iterable 'User Update' api updates a user profile with new data
        fields. Missing fields are not deleted and new data is merged.

        The body of the request takes 4 keys:
            1. email-- in the form of a string -- used as the unique identifier by
                the Iterable database.
            2. data fields-- in the form of an object-- these are the additional attributes
             of the user that we want to add or update
            3. userId- in the form of a string-- another field we can use as a lookup
                of the user.
            4. mergeNestedObjects-- in the form of an object-- used to merge top level
                objects instead of overwriting.
        """

        resource = "/api/users/update"
        payload = {}
        if email is not None:
            payload["email"] = str(email)
        payload["dataFields"] = data_fields
        if user_id is not None:
            payload["userId"] = str(user_id)
        payload["mergeNestedObjects"] = merge_nested_objects
        return self.client.post(resource, data=payload)

    def update_email(self, current_email, new_email, merge=False):
        resource = "/api/users/updateEmail"
        payload = {}
        payload["currentEmail"] = str(current_email)
        payload["newEmail"] = str(new_email)
        payload["merge"] = bool(merge)
        return self.client.post(resource, data=payload)

    def bulk_update(self, users):
        """
        The Iterable 'Bulk User Update' api Bulk update user data or adds
        it if does not exist. Data is merged - missing fields are not deleted

        The body of the request takes 1 keys:
            1. users -- in the form of an array -- which is the list of users
                that we're updating in sets of 50 users at a time, which is the
                most that can be batched in a single request.
        """
        resource = "/api/users/bulkUpdate"
        payload = {}
        if not isinstance(users, (list, tuple)):
            raise TypeError("Using bulk update with a single user")
        payload["users"] = users
        return self.client.post(resource, data=payload)

    def update_subscriptions(
        self,
        email,
        email_list_ids=None,
        unsubscribed_channel_ids=None,
        unsubscribed_message_type_ids=None,
        campaign_id=None,
        template_id=None,
    ):
        resource = "/api/users/updateSubscriptions"
        payload = {}
        payload["email"] = email
        payload["emailListIds"] = email_list_ids
        payload["unsubscribedChannelIds"] = unsubscribed_channel_ids
        payload["unsubscribedMessageTypeIds"] = unsubscribed_message_type_ids
        payload["campaignId"] = campaign_id
        payload["templateId"] = template_id
        return self.client.post(resource, data=payload)

    def bulk_update_subscriptions(self, update_subscriptions_requests):
        resource = "/api/users/bulkUpdateSubscriptions"
        payload = {}
        if isinstance(update_subscriptions_requests, list):
            payload["updateSubscriptionsRequests"] = update_subscriptions_requests
        else:
            raise TypeError("subscription requests are not in Arrary format")
        return self.client.post(resource, data=payload)
