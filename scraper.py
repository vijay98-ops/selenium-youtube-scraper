from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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

if __name__=='__main__':
  print('Creating Driver')
  # this is loading the url in browser tab
  driver = get_driver()
  print('Fetching trending videos')
  videos = get_videos(driver)
  print(f'Found {len(videos)} videos')

  print('Parsing the first video')
  # title, url, thumbnail_url, channel, views, uploaded, description
  video = videos[0]
  title_tag = video.find_elements_by_id('video-title')
  title = title_tag.text
  url = title_tag.get_attribute('href')
  print('Title:',title)
  print('URL:', url)



  