
import requests


# Create a Request object
url = "https://books.toscrape.com/"
#payload = {"key": "value"}
#headers = {"Authorization": "Bearer token"}


# Create a prepared request
req = requests.Request('GET', url ) # data=payload, headers=headers
prepared = req.prepare()


# Now you can inspect the prepared request before sending it
print(f"URL: {prepared.url}")
print(f"Headers: {prepared.headers}")
print(f"Body: {prepared.body}")


with requests.Session() as session:
    response = session.send(prepared)
    print(f"Response: {response.status_code}")
    #print(f"Response Body: {response.text}")


a=type(response)


print(a)


