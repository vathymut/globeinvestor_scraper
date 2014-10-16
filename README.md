README
=======

These scripts, written in `Python`, scrapes GIC rates and saving rates from 
the Globe And Mail's [Globe Investor] website.

The only dependencies, as far as libraries goes, are [requests] and [lxml].
It should be much easier to maintain than using `Scrapy`.

The Windows `.bat` files schedule the relevant scripts to scrape the website
every Monday, Wednesday and Friday.

Note to self: Look into [schedule] as an alternative to set up this cron job without `.bat` files.

[Globe Investor]:http://www.theglobeandmail.com/globe-investor/
[requests]:http://docs.python-requests.org/en/latest/
[lxml]:http://lxml.de/
[schedule]:https://github.com/dbader/schedule