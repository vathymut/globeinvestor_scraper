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
xpath_year1 = '//table[@class="data rates"]/tr/td[5]/text()'
# Get list of 60days
xpath_year2 = '//table[@class="data rates"]/tr/td[6]/text()'
# Get list of 90days
xpath_year3 = '//table[@class="data rates"]/tr/td[7]/text()'
# Get list of 120days
xpath_year4 = '//table[@class="data rates"]/tr/td[8]/text()'
# Get list of 180days
xpath_year5 = '//table[@class="data rates"]/tr/td[9]/text()'
# Get list of 270days
xpath_year6 = '//table[@class="data rates"]/tr/td[10]/text()'

# List of all xpath
all_xpaths = [ xpath_fis,
            xpath_comp_freq,
            xpath_payment_freq,
            xpath_redeem,
            xpath_min_deposit,
            xpath_year1,
            xpath_year2,
            xpath_year3,
            xpath_year4,
            xpath_year5,
            xpath_year6 ]

# Write column names to csv file
colnames = ( 'financial_institution',
            'compound_frequency',
            'payment_frequency',
            'redeemable',
            'minimum_deposit',
            'year1',
            'year2',
            'year3',
            'year4',
            'year5',
            'year6',
            'date_retrieved',
             )

# Get the urls
def create_url( page_no ):
    url = r'http://www.globeinvestor.com/servlet/Page/document/v5/data/rates?order=a'
    url += r'&pageType=gic_long&sort=FIN_NAME'
    url += r'&page={page_no}'.format( page_no = page_no)
    url += r'&tax_indicator=R'
    return url

urls = [ create_url( pg ) for pg in xrange( 1, 5 ) ]

if __name__ == '__main__':
    write_info_to_csv( urls, all_xpaths, colnames, prefix = 'gic-long-term-registered' )
    date_today = str( datetime.date.today() )
    kwargs = dict( rate_type = 'gic-long-term-registered', date = date_today )
    print 'Scraping {rate_type} on {date}'.format( **kwargs )
