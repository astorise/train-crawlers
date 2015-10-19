"""
A crawler that fetches random data from the SNCF API and puts them into JSON files

Usage: python sncf_crawler.py -o output.json

In the future this should contain a few utilities to get the output in a chosen, relevant
format. This being JSON already plays rather nicely with tools like Elasticsearch.

"""
# stdlib
import json
import argparse

# 3p
import requests

API_PREFIX = 'https://api.sncf.com/v1/coverage/sncf/'

def main(path, api_key, out_json_path):
    """ Let's crawl some data """

    # Let's crawl some random data out of nowhere and save the JSON result
    print("Crawling the {0} endpoint and saving the results into {1}".format(API_PREFIX + path,
                                                                             out_json_path))
    req = requests.get(API_PREFIX + path, auth=requests.auth.HTTPBasicAuth(api_key, ''))
    with open(out_json_path, 'w') as out:
        out.write(json.dumps(req.json(), sort_keys=True, indent=2, separators=(', ', ': ')))
    print("Data crawled successfully")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Crawls data from the SNCF API')
    parser.add_argument('--path', type=str, default='',
                        help='Path to the resource (the URL part after "coverage/sncf")')
    parser.add_argument('--key', type=str, required=True,
                        help='The API key you use to connect to the SNCF API.')
    parser.add_argument('--out', type=str, default='./result.json',
                        help='Path tot he output file.')

    args = parser.parse_args()

    main(args.path, args.key, args.out)
