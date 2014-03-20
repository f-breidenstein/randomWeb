#! /usr/bin/env python2
import urllib2
from BeautifulSoup import BeautifulSoup
import random
from urlparse import urlparse


def getNextUrl(url):
    """ Return one random url from a given website """
    result = []
    try:
        response = urllib2.urlopen(url)
        the_page = response.read()
        pool = BeautifulSoup(the_page)
        result = pool.findAll('a')
    except:
        # Errors should be catched here
        pass


    if len(result) == 0:
        # Return the old url if nothing was found
        return url
    else:
        num = random.randrange(len(result))
        newUrl = result[num]['href']

        if newUrl[0] == '/':
            # Add root domain at the begin if it is a relative link
            return "http://" + urlparse(url)[1] + newUrl

        if newUrl[0] == '.':
            return "http://" + urlparse(url)[1] + newUrl[1:]

        if newUrl[0] == '#':
            return url

        else:
            return newUrl


def main():
    steps = 10
    verbose = True
    url = "http://www.spiegel.de"

    print "Start: " + url

    for i in range(steps):
        if (verbose):
            print str(i) + ": " + url
        url = getNextUrl(url)

    print "End: " + url

if __name__ == "__main__":
    main()
