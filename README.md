# selenium-youtube-scraper
Scrape top 10 trending videos on YouTube using Selenium and AWS Lambda

**The html we get from `requests` is not a real web page. We need a browser that loads the html and receives the information from the server. SO we need a browser without head or UI, which runs the html and also js and gets the data from the server. This is where the selenium comes into picture**

*The replit comes with chromedriver and chromium-browser pre-installed*