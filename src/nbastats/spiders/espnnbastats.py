import scrapy


class EspnnbastatsSpider(scrapy.Spider):
    name = "espnnbastats"
    allowed_domains = ["www.espn.com"]
    start_urls = ["https://www.espn.com/nba/stats/player/_/season/2024/seasontype/2/table/offensive/sort/avgPoints/dir/desc"]

    def parse(self, response):
        
        yield {
            'rk': response.css('td.Table__TD::text').getall()[0:50],
            'player_name': response.css('div.athleteCell__flag.flex.items-start.mr7 a.AnchorLink::text').getall(),
            'player_position': response.css('tr.Table__TR.Table__TR--sm.Table__even').css('div.position::text').getall(),
            'all_stats': response.css('td.Table__TD::text').getall()
        }

        pass
