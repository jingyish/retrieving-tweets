#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 23:57:07 2021

@author: shenjingyi
"""

import sys
import os
import inspect
from TwitterAPI import TwitterAPI
from TwitterAPI import TwitterPager

def test_twitterAPI():
    a = oauth_login()
    b = search_tweet()
    assert a.oauth_login(screen_name='SpongeBob')=='SpongeBob'
    assert b.search_tweet('xxxxx') == 'xxxxx'
