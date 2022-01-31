import csv
from time import sleep

from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver import Chrome
import psycopg2
from textwrap import TextWrapper
from reportlab.pdfgen.canvas import Canvas


def create_webdriver_instance():

    driver = Chrome()
    return driver


class User(UserMixin, db.Model):
    __tablename__ = 'mytable'

    username = db.Column(db.String(), unique=True)
    userHandle = db.Column(db.String(), unique=True)
    tweet_date = db.Column(db.String(), unique=True)
    tweet = db.Column(db.String(), unique=True)

    def __init__(self, username, userHandle, tweet_date, tweet):
        self.username = username
        self.userHandle = userHandle
        self.tweet_date = tweet_date
        self.tweet = tweet


def twitter_search(driver):
    url = 'https://twitter.com/i/lists/1471656496849047552?t=aMtdKtTBP6b3yUiOjVEI_g&s=09'

    driver.get(url)

    driver.maximize_window()

    sleep(1)

    return True


def generate_tweet_id(tweet):
    return ''.join(tweet)

# scrolling code


def scroll_down_page(driver, last_position, num_seconds_to_load=0.5, scroll_attempt=0, max_attempts=5):
    end_of_scroll_region = False
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(num_seconds_to_load)
    curr_position = driver.execute_script("return window.pageYOffset;")
    if curr_position == last_position:
        if scroll_attempt < max_attempts:
            end_of_scroll_region = True
        else:
            scroll_down_page(last_position, curr_position, scroll_attempt + 1)
    last_position = curr_position
    return last_position, end_of_scroll_region


def save_database(records):
    print(records[0], records[1], records[2], records[3])
    conn = psycopg2.connect(database="mydatabase", user='postgres',
                            password='postgres', host='localhost', port='5432')

    conn.autocommit = True
    cursor = conn.cursor()

    s = "INSERT INTO public.mytable(\"userName\", \"userHandle\", \"tweet_date\", \"tweet\")VALUES ("+"'" + records[0].replace(
        "'", "\"")+"', '"+records[1].replace("'", "\"")+"', '"+records[2].replace("'", "\"")+"', '"+records[3].replace("'", "\"")+"')"
    print(s)
    cursor.execute(s)
    # print(record)
    conn.commit()


def save_tweet_data_to_csv(records, filepath, mode='a+'):

    header = ['User', 'Handle', 'PostDate', 'TweetText']
    with open(filepath, mode=mode, newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if mode == 'w':
            writer.writerow(header)
        if records:
            writer.writerow(records)


def collect_all_tweets_from_current_view(driver, lookback_limit=25):

    page_cards = driver.find_elements_by_xpath(
        '//article[@data-testid="tweet"]')
    if len(page_cards) <= lookback_limit:
        return page_cards
    else:
        return page_cards[-lookback_limit:]


def extract_data_from_current_tweet_card(card):

    try:
        user = card.find_element_by_xpath('.//span').text
    except exceptions.NoSuchElementException:
        user = ""
    except exceptions.StaleElementReferenceException:
        return
    try:
        handle = card.find_element_by_xpath(
            './/span[contains(text(), "@")]').text
    except exceptions.NoSuchElementException:
        handle = ""
    try:
        postdate = card.find_element_by_xpath(
            './/time').get_attribute('datetime')
    except exceptions.NoSuchElementException:
        return
    try:
        _comment = card.find_element_by_class_name('css-901oao').text
    except exceptions.NoSuchElementException:
        _comment = ""
    try:
        responding = card.find_element_by_xpath('.//div[2]/div[2]/div[2]').text
	

	

    except exceptions.NoSuchElementException:
        _responding = ""
    tweet_text = _comment + _responding

    tweet = (user, handle, postdate, tweet_text)
    return tweet


def main(filepath, page_sort='Latest'):

    save_tweet_data_to_csv(None, filepath, 'w')
    last_position = None
    end_of_scroll_region = False
    unique_tweets = set()

    driver = create_webdriver_instance()
    twitter_search_page_term = twitter_search(driver)

    while not end_of_scroll_region:

        cards = collect_all_tweets_from_current_view(driver)
        for card in cards:
            try:
                tweet = extract_data_from_current_tweet_card(card)
            except exceptions.StaleElementReferenceException:
                continue
            if not tweet:
                continue
            tweet_id = generate_tweet_id(tweet)
            if tweet_id not in unique_tweets:
                unique_tweets.add(tweet_id)
                # print(tweet)
                # print(type(tweet))
                save_database(tweet)
                # save_tweet_data_to_csv(tweet, filepath)
        last_position, end_of_scroll_region = scroll_down_page(
            driver, last_position)
    driver.quit()


output_pdf_file = "static/output/" + \
    str(date) + "_" + "summary_of_entered_URL.pdf"
canvas = Canvas(output_pdf_file)
user_in = output_text
user_in_lines = user_in.split('\n')
wrapper = TextWrapper()
user_in_wrapped_lines = list()
for line in user_in_lines:
    user_in_wrapped_lines += wrapper.wrap(line)
count = 0
text_object = canvas.beginText(100, 741.89)
for line in user_in_wrapped_lines:
    text_object.textLine(line)
    count += 1
    if count == 45:
        # We need to create a new text_object for the new page
        canvas.drawText(text_object)
        canvas.showPage()
        text_object = canvas.beginText(100, 741.89)
        count = 0
canvas.drawText(text_object)
canvas.showPage()
canvas.save()

if __name__ == '__main__':
    path = '11.csv'

    main(path)
