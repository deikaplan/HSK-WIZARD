import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.weibo.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

chinese_pattern = re.compile(r'[\u4e00-\u9fff]+') # Match Chinese characters

with open('temp_sent.txt', 'a', encoding='utf-8') as outfile:
    for p in soup.find_all('p'):
        sentences = p.text.strip().split('。') # Split text into sentences
        for sentence in sentences:
            if chinese_pattern.search(sentence):
                outfile.write(sentence.strip() + '。\n') # Write sentence to file
