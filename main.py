from twilio.rest import Client
import requests
import datetime as dt

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_api_key = "OZXJ7PNW0VMY4PUL"
news_api_key = "e928d13a6ea340d49739bc0fd609872f"
twilio_account_sid = "AC8f4177c4cf790c42416c1535d6fd438a"
twilio_auth_token = "2619ab1e734f4a126acb3138e49f96c5"
client = Client(twilio_account_sid, twilio_auth_token)

current_dt = dt.datetime.now()
today = current_dt.date()
yesterday = today - dt.timedelta(days=1)

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock_api_key
}

stock_entry = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_entry.raise_for_status()
stock_data = stock_entry.json()
today_close = float(stock_data["Time Series (Daily)"][today]["4. close"])
yesterday_close = float(stock_data["Time Series (Daily)"][yesterday]["4. close"])
delta = today_close - yesterday_close
delta_percent = abs((delta / yesterday_close) * 100)
delta_p_rounded = round(delta_percent)
# print(delta_p_rounded)

news_parameters = {
    "apiKey": news_api_key,
    "q": COMPANY_NAME,
    "from": yesterday,
    "to": today,
    "sortBy": "popularity"
}

news_entry = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
news_entry.raise_for_status()
news_data = news_entry.json()


# print(news_data)
def send_news():
    for article_num in range(0, 3):
        article_title = news_data["articles"][article_num]["title"]
        article_desc = news_data["articles"][article_num]["description"]
        notification_info = f"{article_title}: {article_desc}\n"
        message = client.messages \
            .create(
                body=f"Tesla changed {delta_p_rounded} percent.\n{notification_info}",
                from_='+13187272671',
                to='+18134589336'
            )
        print(message.sid)


if delta_p_rounded >= 5:
    send_news()
