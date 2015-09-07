# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class KeyValueManager(models.Manager):


    def has_keyvalue(self, owner=None, key=None, co_owner=None):
        """
        Test if a given owner has an instance of
        keyvalue for all the names provided
        """
        if owner and key:
            qs = self.get_queryset()
            owner_content_type_id = ContentType.objects.get_for_model(owner).id
            owner_id = owner.id
            filter_args = {'owner_content_type_id': owner_content_type_id,
                           'owner_object_id': owner_id,
                           'co_owner_content_type_id': None,
                           'co_owner_object_id': None,
                           'key': key }

            if co_owner:
                co_owner_content_type_id =ContentType.objects.get_for_model(co_owner).id
                co_owner_id = co_owner.id
                filter_args['co_owner_content_type_id'] = co_owner_content_type_id
                filter_args['co_owner_object_id'] = co_owner_id

            return qs.filter(**filter_args).exists()
        else:
            return False


class ScheduledSocialPost(models.Model):

    # Model instance that is the owner of this key value
    owner_content_type_id = models.PositiveIntegerField(db_index=True)
    owner_object_id = models.PositiveIntegerField(db_index=True)
    service = twitter|facebook
    service_token = char
    service_user = char
    content = text
    sent = bool
    schedule = datetime
    created = datetime
