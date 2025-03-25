from pathlib import Path

import scrapy
from scrapy.loader import ItemLoader
from varredor_de_sites.items import citacap_frases1

class TeatroScrapeSpider(scrapy.Spider):
    name = 'destaque'

    def start_requests(self):
        urls = [
            'https://www.sympla.com.br/eventos/teatro-espetaculo?c=teatro-em-destaque&ordem=month_trending_score',
            "https://www.sympla.com.br/eventos/teatro-espetaculo?c=em-alta&ordem=month_trending_score",
            "https://www.sympla.com.br/eventos/teatro-espetaculo?c=stand-up-comedy&ordem=month_trending_score",
            "https://www.sympla.com.br/eventos/teatro-espetaculo/circo?ordem=global-score-norm",
            "https://www.sympla.com.br/eventos/teatro-espetaculo?c=musicais-em-cartaz&ordem=week_trending_score",
            "https://www.sympla.com.br/eventos/teatro-espetaculo/danca?ordem=global-score-norm",
            "https://www.sympla.com.br/eventos/teatro-espetaculo?c=infantil&ordem=global-score-norm",
            "https://www.sympla.com.br/eventos/teatro-espetaculo?c=eventos-previstos&ordem=month_trending_score"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for elemento in response.xpath("//div[@class='_1g71xxu0 _1g71xxu1']/a"): #alterei a classe para a correta
            loader= ItemLoader(item=citacap_frases1(), selector=elemento, response=response)
            loader.add_xpath('data', "string(.//div[@class='qtfy413 qtfy414'])")
            loader.add_xpath('local',".//p[@class='pn67h1a']//text()")
            loader.add_xpath('show',".//h3[@class='pn67h18']//text()")
            yield loader.load_item()
          
