import requests
from bs4 import BeautifulSoup
import random

def amazon_scraper(product):
    url_amazon = f"https://www.amazon.in/s?k={product}"
    product_dict = {}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url_amazon, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            products = soup.find_all('div', {'class': 's-card-container'})

            for product in products:
                title_element = product.find('span', {'class': 'a-text-normal'})
                title = title_element.text.strip()[0:35] if title_element else None

                rate_element = product.find('span', {'class': 'a-icon-alt'})
                rate = rate_element.text.strip()[:3] if rate_element else None

                price_element = product.find('span', {'class': 'a-offscreen'})
                price = price_element.text.strip() if price_element else None

                discount_element = product.find('span', {'class': 'a-text-price'})
                discount_element = discount_element.find('span', {'class': 'a-offscreen'}) if discount_element else None
                discount = discount_element.text.strip() if discount_element else None

                link_element = product.find('a', {'class': 'a-link-normal s-no-outline'})
                link = link_element.get("href") if link_element else None

                img_element = product.find('img', {'class': 's-image'})
                img = img_element.get("src") if img_element else None

                product_dict[title] = {
                    "company":"amazon",
                    "rate": rate,
                    "price": price,
                    "discount": discount,
                    "link": link,
                    "img": img
                }

        else:
            return response.status_code

    except requests.exceptions.RequestException as e:
        return e

    return product_dict

# print(product_scraper("Samsung"))
def flipkart_scraper(product):
    url_flipkart = f"https://www.flipkart.com/search?q={product}"
    product_dict = {}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url_flipkart, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            products = soup.find_all('div', {'class': '_4ddWXP'})

            for product in products:
                title_element = product.find('a', {'class': 's1Q9rs'})
                title = title_element.text.strip() if title_element else None

                rate_element = product.find('div', {'class': '_3LWZlK'})
                rate = rate_element.text.strip() if rate_element else None

                price_element = product.find('price', {'class': '_30jeq3'})
                price = price_element.text.strip() if price_element else None

                discount_element = product.find('div', {'class': '_3I9_wc'}) if discount_element else None
                discount = discount_element.text.strip() if discount_element else None

                link_element = product.find('a', {'class': '_8VNy32'})
                link = link_element.get("href") if link_element else None

                img_element = product.find('img', {'class': '_396cs4'})
                img = img_element.get("src") if img_element else None

                product_dict[title] = {
                    "company":"flipkart",
                    "rate": rate,
                    "price": price,
                    "discount": discount,
                    "link": link,
                    "img": img
                }

        else:
            return response.status_code

    except requests.exceptions.RequestException as e:
        return e

    return product_dict

def product_scraper(product):
    amazon_s = amazon_scraper(product)
    # flipkart_s = flipkart_scraper(product)

    # if flipkart_s == 500:
    #     return amazon_s
    # elif amazon_s == 500:
    #     return flipkart_s
    # else:
    #     if amazon_s.keys() and flipkart_s.keys():
    #         keys1 = list(amazon_s.keys())
    #         keys2 = list(flipkart_s.keys())

    #         random.shuffle(keys1)
    #         random.shuffle(keys2)

    #         merged_dict = {}

    #         for key1, key2 in zip(keys1, keys2):
    #             merged_dict[key1] = amazon_s[key1]
    #             merged_dict[key2] = flipkart_s[key2]
    merged_dict = amazon_s

    return merged_dict