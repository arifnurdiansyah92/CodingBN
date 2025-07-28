import requests

# We're asking the weather API for data about Bandung
api_url = "https://api.openweathermap.org/data/2.5/weather"
params = {'q': 'Bandung', 'appid': 'ed703e53cc6b95bacc573bccfd81d524', 'units': 'metric'}

# Our waiter makes the GET request
response = requests.get(api_url, params=params)

# The server's response is in a format called JSON
data = response.json() 
# Now we can look at the data we got back
print(f"Weather in {data['name']}: {data['weather'][0]['description']} with a temperature of {data['main']['temp']}°C.")
