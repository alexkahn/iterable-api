from itertools import islice
from .resources.utils import Mapper


user_mapper = Mapper({
    'user_id': 'userId',
    'data_fields': 'dataFields'
})

subscription_mapper = Mapper({
    "email": "email",
    "email_list_ids": "emailListIds",
    "unsubscribed_channel_ids": "unsubscribedChannelIds",
    "unsubscribed_message_type_ids": "unsubscribedMessageTypeIds",
    "campaign_id": "campaignId",
    "template_id": "templateId",
})


def chunks(sequence, size):
    it = iter(sequence)
    while True:
        chunk = tuple(islice(it, size))
        if not chunk:
            return
        yield chunk


def bulk_update(client, users):
    results = []
    for chunk in chunks(users, 50):
        mapped = [user_mapper.remap(u) for u in chunk]
        res = client.users.bulk_update(mapped)
        results.append(res)
    return results


def bulk_update_subscriptions(client, update_subscription_requests):
    results = []
    for chunk in chunks(update_subscription_requests, 50):
        mapped = [subscription_mapper.remap(sub) for sub in chunk]
        res = client.users.bulk_update(mapped)
        results.append(res)
    return results
