# -*- coding: utf-8 -*-

from .categories import CATEGORIES_MAPPING
from .invites import INVITES_MAPPING
from .topics import TOPICS_MAPPING

RESOURCE_MAPPING = {}
RESOURCE_MAPPING.update(CATEGORIES_MAPPING)
RESOURCE_MAPPING.update(INVITES_MAPPING)
RESOURCE_MAPPING.update(TOPICS_MAPPING)
