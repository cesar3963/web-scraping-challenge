from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt 

def scrape_all():
    browser = Browser("chrome", executable_path="chromedriver", headless=True)
    news_title, news_paragraph = mars_news(browser)      

    data = {
        "news_title": news_title, 
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "hemispheres": hemispheres(browser),
        "last_modified": dt.datetime.now() 
    }

    browser.quit()
    return data
  
def mars_news(browser):
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)
    html = browser.html
    news_soup = soup(html, 'html.parser')

    elem_list = news_soup.select_one("ul.item_list li.slide")
    tittle = elem_list.find("div", class_="content_title").get_text()
    paragraph = elem_list.find("div", class_="article_teaser_body").get_text()

    return tittle,paragraph
def featured_image(browser):
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    html = browser.visit(url)

    elem_img = browser.find_by_id('full_image')[0]
    elem_img.click()

    
    browser.is_element_present_by_text('more info',wait_time=...)
    more_info = browser.links.find_by_partial_text('more info')
    more_info.click()

    html = browser.html
    img_soup = soup(html, 'html.parser')     

    img_url = img_soup.select_one("figure.lede a img").get("src")
    return img_url



def mars_facts():
    df = pd.read_html('http://space-facts.com/mars/')[0]

    df.columns=['Description', 'Mars']
    df.set_index('Description', inplace=True)

    return df.to_html(classes="table table-straped")

    
def hemispheres(browser):
    url= ('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')
    browser.visit(url)
    hemisphere_image_urls = []

    for i in range(4):
        browser.find_by_css("a.product-item h3")[i].click()
        hemi_data = scrape_hemisphere(browser.html)
        hemisphere_image_urls.append(hemi_data)
        browser.back()
   
def scrape_hemisphere(html_text):
    hemi_soup =soup(html_text, 'html.parser')

    title_elem = hemi_soup.find("h2", class_="title").get_text()
    sample_elem = hemi_soup.find("a", text="Sample").get("href")

    hemispheres = {
        "title": title_elem,
        "img_url": sample_elem
    }

    return hemispheres






if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())