import secrets

def get_stories(section):
    baseurl = 'https://api.nytimes.com/svc/topstories/v2/'
    extendedurl = baseurl + section + '.json'
    params = {'api-key': secrets.nyt_key}
    return requests.get(extendedurl, params).json()





