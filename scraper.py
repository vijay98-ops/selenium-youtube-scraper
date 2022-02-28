from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending'

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  # we need to pass the path to the chrome driver installed
  # this is a browser
  driver = webdriver.Chrome(options=chrome_options)
  return driver

def get_videos(driver):
  VIDEO_DIV_TAG = 'ytd-video-renderer'
  driver.get(YOUTUBE_TRENDING_URL)
  videos = driver.find_elements_by_tag_name(VIDEO_DIV_TAG)
  return videos

def parse_video(video):
  title_tag = video.find_elements_by_id('video-title')
  title = title_tag.text
  url = title_tag.get_attribute('href')
  
  thumbnail_tag = video.find_element_by_tag_name('img')
  thumbnail_url = thumbnail_tag.get_attribute('src')

  channel_div = video.find_element_by_class_name('ytd-channel-name')
  channel_name = channel_div.text

  description = video.find_element_by_id('description-text').text

  return {
    'title': title,
     'url': url,
     'thumbnail_url': thumbnail_url,
     'channel': channel_name,
     'description': description
  }


if __name__=='__main__':
  print('Creating Driver')
  # this is loading the url in browser tab
  driver = get_driver()
  print('Fetching trending videos')
  videos = get_videos(driver)
  print(f'Found {len(videos)} videos')

  print('Parsing top 10 videos')
  videos_data = [parse_video(video) for video in videos[:10]]

  print('Save the data to CSV')

  videos_df = pd.DataFrame(videos_data)
  print(videos_df)
  videos_df.to_csv('trending.csv')




  