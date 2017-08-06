import rauth
import time


def main():
    locations = [(39.98, -82.98), (42.24, -83.61), (41.33, -89.13)]
    api_calls = []
    for lat, long in locations:
        params = get_search_parameters(lat, long)
        api_calls.append(get_results(params))
        # Be a good internet citizen and rate-limit yourself
        time.sleep(1.0)
    return api_calls
        ##Do other processing


def get_results(params):
    # Obtain these from Yelp's manage access page
    consumer_key =  'uOZv9SZSepVUp2s29CyWmA'
    consumer_secret = 'akcl2MJFNuJE9lfNlG4fI3Y_Oj8'
    token = 'kqFnFl_rs7IFhQEyxBZTzq0XZbOqea65'
    token_secret = '-z5NBbAGcO4Do_cYZfrbkR5oik4'

    session = rauth.OAuth1Session(
        consumer_key=consumer_key
        , consumer_secret=consumer_secret
        , access_token=token
        , access_token_secret=token_secret)

    request = session.get("http://api.yelp.com/v2/search", params=params)

    # Transforms the JSON API response into a Python dictionary
    data = request.json()
    session.close()

    return data


def get_search_parameters(lat, long):
    # See the Yelp API for more details
    params = {}
    params["term"] = "restaurant"
    params["ll"] = "{},{}".format(str(lat), str(long))
    params["radius_filter"] = "2000"
    params["limit"] = "10"

    return params

list_api_calls = main()