from app.impl.voa.core import VOACrawler
from app.base.abstract_crawler import AbstractCrawler

class CrawlerFactory:
    CRAWLERS = {
        "voa": VOACrawler,
        "dy": VOACrawler,
        "ks": VOACrawler,
        "bili": VOACrawler,
        "wb": VOACrawler,
        "tieba": VOACrawler,
        "zhihu": VOACrawler
    }

    @staticmethod
    def create_crawler(platform: str) -> AbstractCrawler:
        crawler_class = CrawlerFactory.CRAWLERS.get(platform)
        if not crawler_class:
            raise ValueError("Invalid Media Platform Currently only supported xhs or dy or ks or bili ...")
        return crawler_class()