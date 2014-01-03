#!/usr/bin/env python
# -*- coding: utf8 -*-

import ConfigParser


class config(object):
    def __init__(self):
        conf = ConfigParser.ConfigParser()
        conf.readfp(open('boto.cfg'))
        self.aws_key = conf.get('Credentials', 'aws_access_key_id')
        self.aws_secret = conf.get('Credentials', 'aws_secret_access_key')
        self.ec2_region_name = conf.get('Boto', 'ec2_region_name')
        self.debug = conf.get('Boto', 'debug')
