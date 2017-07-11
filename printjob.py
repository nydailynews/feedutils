#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Print the results of a recentfeed/json ingestion.
import doctest
import json
import argparse

class Format():
    """ Manage the way we're outputting this stuff.
        """

    def __init__(self):
        """
            """
        pass

    def formats(self, **kwargs):
        """
            """
        #'<li><a href="{0}">{1}</a> <span>(published {2})</span></li>'.format(article['url'], article['title'], pretty_date(ago).lower())
        pass

    def add_timeago(self, **kwargs):
        """
            """
        #'<span>(published {2})</span>'
        pass


class JobConfig():
    """ Streamline creating new print jobs.
        """

    def __init__():
        """
            """
        pass

