#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Scraping rates from website
import datetime
# Add current file location to sys.path
import sys
from os.path import dirname, realpath

CURDIR = dirname( realpath(__file__) )
sys.path.append( CURDIR )

from scraping_rates_func import write_info_to_csv

# Get list of FIs
xpath_fis = '//table[@class="data rates"]/tr/th/text()'
# Get list of compound_frequency
xpath_comp_freq = '//table[@class="data rates"]/tr/td[1]/text()'
# Get list of payment_frequency
xpath_payment_freq = '//table[@class="data rates"]/tr/td[2]/text()'
# Get list of redeemable
xpath_redeem = '//table[@class="data rates"]/tr/td[3]/text()'
# Get list of minimum_deposit
xpath_min_deposit = '//table[@class="data rates"]/tr/td[4]/text()'
# Get list of 30days
xpath_term30 = '//table[@class="data rates"]/tr/td[5]/text()'
# Get list of 60days
xpath_term60 = '//table[@class="data rates"]/tr/td[6]/text()'
# Get list of 90days
xpath_term90 = '//table[@class="data rates"]/tr/td[7]/text()'
# Get list of 120days
xpath_term120 = '//table[@class="data rates"]/tr/td[8]/text()'
# Get list of 180days
xpath_term180 = '//table[@class="data rates"]/tr/td[9]/text()'
# Get list of 270days
xpath_term270 = '//table[@class="data rates"]/tr/td[10]/text()'

# List of all xpath
all_xpaths = [ xpath_fis,
            xpath_comp_freq,
            xpath_payment_freq,
            xpath_redeem,
            xpath_min_deposit,
            xpath_term30,
            xpath_term60,
            xpath_term90,
            xpath_term120,
            xpath_term180,
            xpath_term270 ]

# Write column names to csv file
colnames = ( 'financial_institution',
            'compound_frequency',
            'payment_frequency',
            'redeemable',
            'minimum_deposit',
            '30days',
            '60days',
            '90days',
            '120days',
            '180days',
            '270days',
            'date_retrieved',
             )

# Get the urls: ugly hack (fix later)
url_pg1 = r'http://www.globeinvestor.com/servlet/Page/document/v5/data/rates?order=d&pageType=gic_short&sort=COMPOUND&page=1&tax_indicator=R'
url_pg2 = r'http://www.globeinvestor.com/servlet/Page/document/v5/data/rates?order=d&pageType=gic_short&sort=COMPOUND&page=2&tax_indicator=R'
urls = ( url_pg1, url_pg2 )

if __name__ == '__main__':
    write_info_to_csv( urls, all_xpaths, colnames, prefix = 'gic-short-term-registered' )
    date_today = str( datetime.date.today() )
    kwargs = dict( rate_type = 'gic-short-term-registered', date = date_today )
    print 'Scraping {rate_type} on {date}'.format( **kwargs )
