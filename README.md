# train-crawlers
A repository to experiment with the SNCF API

## Usage of the crawler program

```
python sncf_crawler.py --key=<PASTE_YOUR_API_KEY_HERE> [--path=<ENDPOINT_PATH>]
```

for example,

```
python sncf_crawler.py --key=<PASTE_YOUR_API_KEY_HERE> --path=networks
```

will crawl the following endpoint:

```
https://api.sncf.com/v1/coverage/sncf/networks
```

# Useful links
* Documentation of the SNCF API: https://data.sncf.com/api/documentation
* Documentation of the request module in Python: http://docs.python-requests.org/en/latest/
