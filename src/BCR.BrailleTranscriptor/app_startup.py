import os
import sys
import logging
import urllib.request

from opencensus.ext.azure.log_exporter import AzureLogHandler


if (os.environ['INSIGHTS_CNN_STRING']):
    logger = logging.getLogger(__name__)
    logger.addHandler(logging.StreamHandler(sys.stdout))
    logger.addHandler(AzureLogHandler(connection_string=os.environ['INSIGHTS_CNN_STRING']))

    logger.setLevel('INFO')


