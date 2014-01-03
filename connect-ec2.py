#!/usr/bin/env python
# -*- coding: utf8 -*-

import boto.ec2
import settings

c = settings.config()
conn = boto.ec2.connect_to_region(c.ec2_region_name,
                                  aws_access_key_id=c.aws_key,
                                  aws_secret_access_key=c.aws_secret,
                                  debug=c.debug)
print conn.get_all_instances()
