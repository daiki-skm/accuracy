from newsapi import NewsApiClient


def get_url() -> None:
    newsapi = NewsApiClient(api_key='')

    p_data = newsapi.get_top_headlines(category='business')
    n_data = newsapi.get_top_headlines(category='sports')

    with open('pUrl.txt', 'a') as outf:
        for article in p_data['articles']:
            print(article['url'], file=outf)
    outf.close()

    with open('nUrl.txt', 'a') as outf:
        for article in n_data['articles']:
            print(article['url'], file=outf)
    outf.close()

get_url()
