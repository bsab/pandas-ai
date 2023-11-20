import os
import pandas as pd
from typing import Optional, Union

from .base import YahooFinanceConnectorConfig, BaseConnector
import time
from ..helpers.path import find_project_root
from ..constants import DEFAULT_FILE_PERMISSIONS
import hashlib

class MongoDBConnector(BaseConnector):
    """
    The MongoDB connector allows you to connect to a MongoDB database.
    """

    def __init__(self):
        pass
