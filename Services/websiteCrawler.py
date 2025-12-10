from flask import jsonify
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
from Services.storeCrawledData import storeCrawledData
from Services.dataEmbedings import StoreEmbeddings


class websiteCrawller:
    def __init__(self, url=None, website_id=None):
        self.url = url
        self.website_id = website_id

    def chunk_data(self, web_content, chunk_size):
        content_arr = web_content.split('\n')
        chunks = []

        for i in range(0, len(content_arr), chunk_size):
            chunk_lines = content_arr[i:i + chunk_size]
            chunk_text = " ".join(chunk_lines).strip()

            if chunk_text:
                chunks.append(chunk_text)

        return chunks

    def crawlLink(self):
        url_html = requests.get(self.url)
        soup = BeautifulSoup(url_html.text, 'html.parser')
        links = soup.find_all('a')

        unique_links = set()

        for link in links:
            href = link.get("href")
            if href:
                unique_links.add(href)

        return self.scrapLinkContent(unique_links)

    def scrapLinkContent(self, extrated_links):
        for extrated_link in extrated_links:
            try:
                requset_link = requests.get(extrated_link)
                requset_link.raise_for_status()

                soup = BeautifulSoup(requset_link.text, "html.parser")

                for selector in ["header", "nav", "footer", "script", "style"]:
                    for tag in soup.select(selector):
                        tag.extract()

                text_content = soup.get_text(separator="\n", strip=True)

                store_link = storeCrawledData(
                    website_id=self.website_id,
                    website_url=extrated_link
                )
                store_crawled_link = store_link.store_crawl_links()

                chunk_web_data = self.chunk_data(text_content, 6)

                for chunk in chunk_web_data:

                    embedding_obj = StoreEmbeddings(chunk, self.website_id)
                    chroma_id = embedding_obj.createEmbedding()

                    store_chunk = storeCrawledData(
                        website_id=self.website_id,
                        url_id=store_crawled_link,
                        chunk_data=chunk,
                        chroma_id=chroma_id
                    )
                    store_chunk.add_website_link_data()

            except requests.exceptions.RequestException:
                continue
