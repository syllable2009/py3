from app.base.abstract_crawler import AbstractCrawler
from app.impl import VOACrawler, LummiCrawler, EruptCrawler


class CrawlerFactory:
    CRAWLERS = {
        "voa": VOACrawler,
        "lummi": LummiCrawler,
        "erupt": EruptCrawler,
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
            raise ValueError(
                "Invalid Media Platform Currently only supported xhs or dy or ks or bili ...")
        return crawler_class()
