import requests


def yelp_data(offset):
    
    url = "https://api.yelp.com/v3/businesses/search"

    querystring = {"term": "bar",
                    "location": "NYC",
                    "limit": "50",
                    "offset": str(offset),
    }

    access_key_token = "your_bearer_access_token/key_goes_here"

    headers = {'authorization': f'Bearer {access_key_token}'}

    response = requests.get(url, headers = headers, params = querystring)

    return response.json()


if __name__ == "__main__":

    # offset should be thought of as pagination

    offset = 0
    total_businesses = int(yelp_data(offset=0)['total'])

    while offset < total_businesses + 10:
        yelp_data(offset=0)
        offset += 50
