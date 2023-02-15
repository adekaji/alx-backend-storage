#!/usr/bin/env python3
""" Writing strings to Redis, Reading from Redis and recovering original type,
    Incrementing values, Storing lists, Retrieving lists """
from typing import Union, Callable, Optional, Any
import redis
import uuid
from functools import wraps


