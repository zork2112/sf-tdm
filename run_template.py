#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Stephen Stokes: sstokes[at]relationshipvelocity.com'

import logging
import os
import sys

import sf_tdm as tdm
import tools.helpers as h

# Logging setup
h.setup_logging()

# Logging statements for each module:
log = logging.getLogger(__name__)
log.debug(f'{__name__} logging is configured.')

# Get script argument
try:
    config = sys.argv[1]
except Exception as argument_error:
    log.info(f'No input arguments.\nError: {argument_error}')
    raise

# Run template
results = tdm.run_template(tdm_config=config)
log.info(f'{results}\n')
