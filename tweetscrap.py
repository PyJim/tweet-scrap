import csv
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import os
import wget

driver = webdriver.Chrome("C:/Program Files (x86)/chromedriver.exe")

driver.get('https://www.twitter.com/login')
driver.maximize_window()
username = driver.find_element_by_xpath('//input[@name = "session[username_or_email]"]')
username.send_keys("@essel_kodwo")

password = driver.find_element_by_xpath('//input[@name = "session[password]"]')
password.send_keys("Gh9280011@")
password.send_keys(Keys.RETURN)

search_input = driver.find_element_by_xpath('//input[@aria-label = "Search query"]')
search_input.send_keys("#science")
search_input.send_keys(Keys.RETURN)

driver.find_element_by_link_text("Latest").click()

results = driver.find_elements_by_xpath('//div[@data-testid = "tweet"]')
result = results[0]

#username
result.find_element_by_xpath('.//span').text

#handle
result.find_element_by_xpath('.//span[contains(text(), "@")]').text

#posdate
result.find_element_by_xpath('.//time').get_attribute('datetime')

#main content
comments = result.find_element_by_xpath('.//div[2]/div[2]/div[1]').text
response = result.find_element_by_xpath('.//div[2]/div[2]/div[2]').text
comments + response

#reply counts
result.find_element_by_xpath('.//div[@data-testid = "reply"]')
#retweet
result.find_element_by_xpath('.//div[@data-testid = "retweet"]')
#likes
result.find_element_by_xpath('.//div[@data-testid = "likes"]')

def all_tweet_data(result):
    #username
    username = result.find_element_by_xpath('.//span').text

    #handle
    handle = result.find_element_by_xpath('.//span[contains(text(), "@")]').text

    #posdate
    try:
        postdate = result.find_element_by_xpath('.//time').get_attribute('datetime')
    except Exception:
        return

    #main content
    comments = result.find_element_by_xpath('.//div[2]/div[2]/div[1]').text
    response = result.find_element_by_xpath('.//div[2]/div[2]/div[2]').text
    text = comments + response

    #reply counts
    reply_counts = result.find_element_by_xpath('.//div[@data-testid = "reply"]')
    #retweet
    retweet_counts = result.find_element_by_xpath('.//div[@data-testid = "retweet"]')
    #likes
    likes_counts = result.find_element_by_xpath('.//div[@data-testid = "likes"]')

    #tweet tuple
    tweet = (username, handle, postdate, text, reply_counts, retweet_counts, likes_counts) 
    return tweet  

tweet_data = []
for result in results:
    data = all_tweet_data(result)
    if data:
        tweet_data.append(data)

#scroll
driver.execute_script('window.scrollTo(0, scrollHeight);')

#data analysis
import csv
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import os
import wget

##defining function
def all_tweet_data(result):
    #username
    username = result.find_element_by_xpath('.//span').text

    #handle
    handle = result.find_element_by_xpath('.//span[contains(text(), "@")]').text

    #posdate
    try:
        postdate = result.find_element_by_xpath('.//time').get_attribute('datetime')
    except NoSuchElementException:
        return

    #main content
    comments = result.find_element_by_xpath('.//div[2]/div[2]/div[1]').text
    response = result.find_element_by_xpath('.//div[2]/div[2]/div[2]').text
    text = comments + response

    #reply counts
    reply_counts = result.find_element_by_xpath('.//div[@data-testid = "reply"]')
    #retweet
    retweet_counts = result.find_element_by_xpath('.//div[@data-testid = "retweet"]')
    #likes
    likes_counts = result.find_element_by_xpath('.//div[@data-testid = "likes"]')

    #tweet tuple
    tweet = (username, handle, postdate, text, reply_counts, retweet_counts, likes_counts) 
    return tweet  
#webdriver
driver = webdriver.Chrome("C:/Program Files (x86)/geckodriver.exe")

#navigation and login
driver.get("Https://www.twitter.com/login")
driver.maximize_window()
username = driver.find_element_by_xpath('//input[@name = "session[username_or_email]"]')
username.send_keys("@essel_kodwo")

password = driver.find_element_by_xpath('//input[@name = "session[password]"]')
password.send_keys("Gh9280011@")
password.send_keys(Keys.RETURN)

#search tweet
search_input = driver.find_element_by_xpath('//input[@aria-label = "Search query"]')
search_input.send_keys("#science")
search_input.send_keys(Keys.RETURN)

#extract data from tweet
driver.find_element_by_link_text("Latest").click()

#get data from tweet
tweet_data = []
tweet_ids = set()

last_page = driver.execute_script("return windwo.pageYOffset;")

scrolling = True
#looping through
while scrolling:
    page_results = driver.find_elements_by_xpath('//div[@data-testid = "tweet"]')
    for result in results:
        data = all_tweet_data(result)
        if data:
            tweet_id = ''.join(data)
            if tweet_id not in tweet_ids:
                tweet_ids.add(tweet_id)
                tweet_data.append(data)
    scroll = 0
    while True:
        driver.execute_script('window.scrollTo(0, scrollHeight);')
        sleep(1)
        current_page = driver.execute_script("return windwo.pageYOffset;")
        if last_page == current_page:
            scroll += 1
            
            #ending the loop
            if scroll >= 3:
                scrolling = False
                break
            else:
                sleep(2)
        else:
            last_page = current_page
            break
        
#Saving the extracts
with open('science_tweets.csv', 'w', newline ='', encoding = 'utf-8') as f:
    header = ["username", "handle", "postdate", "text", "reply_counts", "retweet_counts", "likes_counts"]
    writer = csv.writer(f)
    writer.writerows(header)
    writer.writerows(tweet_data)


    
    
    
    
    
    
    
