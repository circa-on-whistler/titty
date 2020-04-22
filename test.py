import requests

url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/WebSearchAPI"

querystring = {"autoCorrect":"true","pageNumber":"1","pageSize":"50","q":"Free Porn","safeSearch":"false"}

headers = {
    'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
    'x-rapidapi-key': "4d3cfcf73emshe73c4838c004284p10b87bjsnbd9833b788ab"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
