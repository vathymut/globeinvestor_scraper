#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Convert text files to a single bibtex file.

from lxml import html
import datetime
import requests
import csv
from functools import partial
from itertools import izip

def extract_list( tree, xpath_src ):
    '''
    Extract list of strings from the
    '''
    return tree.xpath( xpath_src )

def get_tree( url ):
    src = requests.get( url )
    tree = html.fromstring( src.text )
    return tree

def write_info_to_csv( urls, all_xpaths, colnames, prefix = 'saving-rates' ):
    '''
    Write the information extracted from the website table to a csv.
    '''
    # Get today's date
    date_today = str( datetime.date.today() )
    # Open csv file
    filename = '{prefix}-{date}.csv'.format( prefix = prefix, date = str( date_today ) )
    f = open( filename, 'wb' ) # Don't forget to close f when done
    writer = csv.DictWriter( f, fieldnames = colnames )
    # Write header row to csv
    headers = dict( ( n, n ) for n in colnames )
    writer.writerow( headers )
    for url in urls:
        tree = get_tree( url )
        fpartial = partial( extract_list, tree )
        columns_list = map( fpartial, all_xpaths )
        for row in izip( *columns_list ):
            # Append value for date_retrieved
            row_list = list( row )
            row_list.append( str( date_today ) )
            row_dict = dict( ( key, val ) for key, val in izip( colnames, row_list ) )
            print row_dict
            writer.writerow( row_dict )
    print 'Close file.'
    f.close( )