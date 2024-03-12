import requests
from bs4 import BeautifulSoup


def extract_article_information(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract relevant information from the article
            title = soup.find('title').text
            paragraphs = soup.find_all('p')
            content = '\n'.join([p.text for p in paragraphs])

            return {'title': title, 'content': content}
        else:
            print(f"Failed to fetch URL: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")

    return {'title': '', 'content': ''}
