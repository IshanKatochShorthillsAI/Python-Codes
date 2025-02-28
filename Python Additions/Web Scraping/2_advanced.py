from bs4 import BeautifulSoup
import requests

html_text = requests.get(
    "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="
).text
soup = BeautifulSoup(html_text, "lxml")


"""
Example Code:

import requests
from bs4 import BeautifulSoup
import json

# URL of the webpage that contains dynamic content.
url = "https://example.com/dynamic-content-page"

# Fetch the webpage using requests.
response = requests.get(url)
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    
    # Approach 1: Look for embedded JSON within a <script> tag.
    # This assumes the dynamic data is stored in a script tag with a unique identifier (e.g., id="dynamicData").
    script_tag = soup.find("script", id="dynamicData")
    if script_tag:
        try:
            # The script's content is expected to be valid JSON.
            json_data = json.loads(script_tag.string)
            print("Extracted JSON data from the script tag:")
            print(json.dumps(json_data, indent=4))
        except json.JSONDecodeError:
            print("Found the script tag, but failed to decode JSON from its content.")
    else:
        print("No embedded JSON data found in the page.")
    
    # Approach 2: Directly call an API endpoint if known.
    # Inspect the network traffic in your browser to find the endpoint that returns the dynamic data.
    api_url = "https://example.com/api/dynamic-data"
    api_response = requests.get(api_url)
    if api_response.status_code == 200:
        try:
            api_data = api_response.json()
            print("Data fetched directly from the API endpoint:")
            print(json.dumps(api_data, indent=4))
        except json.JSONDecodeError:
            print("Failed to decode JSON from the API response.")
    else:
        print(f"API request failed with status code: {api_response.status_code}")
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
"""
