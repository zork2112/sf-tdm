#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Stephen Stokes: sstokes[at]relationshipvelocity.com'

import logging
import sys

import sf_tdm as tdm
import tools.helpers as h

# Logging setup
h.setup_logging()

# Logging statements for each module:
log = logging.getLogger(__name__)
log.debug(f'{__name__} logging is configured.')


@h.exception(log)
@h.timer(log)
def run_template():
    config = sys.argv[1]
    results = tdm.run_template(tdm_config=config)
    return results


# Run main program
if __name__ == '__main__':
    h.setup_logging()
    results = run_template()
    log.info(f'{results}\n')