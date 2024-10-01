import requests
from bs4 import BeautifulSoup
import csv
import time
import random


class AmazonBestSellersScraper:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        self.base_urls = {
            "US": "https://www.amazon.com/Best-Sellers/zgbs",
            "UK": "https://www.amazon.co.uk/best-sellers/zgbs",
            "India": "https://www.amazon.in/gp/bestsellers/zgbs",
        }   

    def get_categories(self, region):
        url = self.base_urls[region]
        response = self.make_request(url)
        soup = BeautifulSoup(response.content, "html.parser")
        categories = soup.select("#zg_browseRoot ul li a")
        return [(cat.text.strip(), cat["href"]) for cat in categories]

    def get_bestsellers(self, category_url, num_products=50):
        bestsellers = []
        page = 1
        while len(bestsellers) < num_products:
            url = f"{category_url}?pg={page}"
            response = self.make_request(url)
            soup = BeautifulSoup(response.content, "html.parser")
            products = soup.select("li.zg-item-immersion")

            for product in products:
                if len(bestsellers) >= num_products:
                    break

                title_elem = product.select_one("div.p13n-sc-truncate-desktop-type2")
                rank_elem = product.select_one("span.zg-bdg-text")
                price_elem = product.select_one("span.p13n-sc-price")

                title = title_elem.text.strip() if title_elem else "N/A"
                rank = rank_elem.text.strip() if rank_elem else "N/A"
                price = price_elem.text.strip() if price_elem else "N/A"

                bestsellers.append({"rank": rank, "title": title, "price": price})

            page += 1   
            if page > 2:  # Amazon usually shows only 2 pages
                break

            time.sleep(random.uniform(1, 3))  # Random delay between requests

        return bestsellers

    def make_request(self, url):
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            print(f"Failed to fetch {url}: Status code {response.status_code}")
        return response

    def save_to_csv(self, data, filename):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file, fieldnames=["region", "category", "rank", "title", "price"]
            )
            writer.writeheader()
            writer.writerows(data)

    def scrape_bestsellers(
        self, region, categories_to_scrape=None, products_per_category=50
    ):
        all_data = []
        categories = self.get_categories(region)

        for category_name, category_url in categories:
            if categories_to_scrape and category_name not in categories_to_scrape:
                continue

            print(f"Scraping {category_name} in {region}...")
            bestsellers = self.get_bestsellers(category_url, products_per_category)

            for product in bestsellers:
                product["region"] = region
                product["category"] = category_name
                all_data.append(product)

        return all_data


# Usage
scraper = AmazonBestSellersScraper()

# Scrape bestsellers for US, UK, and India
regions = ["US", "UK", "India"]
all_data = []

for region in regions:
    region_data = scraper.scrape_bestsellers(
        region, categories_to_scrape=["Books", "Electronics"], products_per_category=20
    )
    all_data.extend(region_data)

scraper.save_to_csv(all_data, "amazon_bestsellers1.csv")
