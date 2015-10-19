"""
A crawler that fetches random data from the SNCF API and puts them into JSON files

Usage: python sncf_crawler.py -o output.json

In the future this should contain a few utilities to get the output in a chosen, relevant
format. This being JSON already plays rather nicely with tools like Elasticsearch.

"""
# stdlib
import os
import json

# 3p
import requests

API_PREFIX = 'https://api.sncf.com/v1/coverage/sncf/'

def main():
    """ Let's crawl some data """
    api_key = os.environ.get('SNCF_API_KEY')
    if api_key is None:
        print('You need to provide your SNCF API key in the SNCF_API_KEY environment variable')
        exit(0)

    # Let's crawl some random data out of nowhere and save the JSON result
    req = requests.get(API_PREFIX + 'networks', auth=requests.auth.HTTPBasicAuth(api_key, ''))
    with open('./results.json', 'w') as out:
        out.write(json.dumps(req.json(), sort_keys=True, indent=2, separators=(', ', ': ')))
    print("Data crawled successfully")

if __name__ == '__main__':
    main()
