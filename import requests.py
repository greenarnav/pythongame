import requests

# URL of the webpage
url = 'https://finance.yahoo.com/news/micron-technology-mu-invests-7b-222840205.html'

# Send a GET request to the URL
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Get the HTML content
    html_content = response.text
    # Write the HTML content to a file
    with open('webpage.html', 'w', encoding='utf-8') as file:
        file.write(html_content)
    print('HTML content has been written to webpage.html')
else:
    print(f'Failed to retrieve the page. Status code: {response.status_code}')
