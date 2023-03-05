import requests

# Enter your username and password here
username = 'maochengzhi1@gmail.com'
password = 'R*G_JLNT78U!6hv'

# Set up the session
session = requests.Session()

# Log in to Space-Track.org
response = session.post('https://www.space-track.org/ajaxauth/login',
                        data={'identity': username, 'password': password})

# Check if login was successful
if 'SSO SAML Login' in response.text:
    print('Login failed')
else:
    print('Login successful')

# Set up the API query
query_url = 'https://www.space-track.org/basicspacedata/query/class/gp_history/NORAD_CAT_ID/36395/orderby/EPOCH%20ASC/EPOCH/{start}--{end}/interval/1%20min/format/tle'

# Set the start and end times of the query
start_time = '2011-01-27%2020:00:00'
end_time = '2011-01-27%2021:00:00'

# Replace {start} and {end} in the query URL with the specified times
query_url = query_url.format(start=start_time, end=end_time)

# Make the API query
response = session.get(query_url)

# Print the TLE data
print(response.text)
