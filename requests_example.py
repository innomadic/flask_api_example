import requests
key = 'PUTYOURKEYHERE'
r = requests.get(f"https://newsapi.org/v2/everything?q=ManCity&from=2021-05-07&sortBy=publishedAt&apiKey={key}")
articles = r.json()['articles']
print(f"We have found {len(articles)} articles.")

for article in articles:
    print(article['title'], article['url'])