#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Convert text files to a single bibtex file.

# Scraping rates from website
import datetime
# Add current file location to sys.path
import sys
from os.path import dirname, realpath
CURDIR = dirname( realpath(__file__) )
sys.path.append( CURDIR )
# Now import new functions
from scraping_rates_func import write_info_to_csv

# Get list of FIs
xpath_fis = '//table[@class="data rates"]/tr/th[@class="sortcolumn"]/text()'
# Get list of saving rates
xpath_sav = '//table[@class="data rates"]/tr/td[1]/text()'

# List of all xpath
all_xpaths = [ xpath_fis, xpath_sav ]

# Write column names to csv file
colnames = ( 'financial_institution',
            'saving_rate',
            'date_retrieved',
             )

# Get the urls
url_pg1 = r'http://www.globeinvestor.com/servlet/Page/document/v5/data/rates?pageType=deposit_acct'
urls = ( url_pg1, )

if __name__ == '__main__':
    write_info_to_csv( urls, all_xpaths, colnames, prefix = 'saving' )
    date_today = str( datetime.date.today() )
    kwargs = dict( rate_type = 'saving', date = date_today )
    print 'Scraping {rate_type} on {date}'.format( **kwargs )
