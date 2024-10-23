import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class HockeyTeamsSpider(scrapy.Spider):

    name = 'hockey_teams'
    allowed_domains = ['scrapethissite.com']
    start_urls = ['https://www.scrapethissite.com/pages/forms/?page_num=1']

    def parse(self, response):

        for item in response.css('.team'):
            title = item.css('td.name::text').get().strip()
            year = item.css('td.year::text').get().strip()
            wins = item.css('td.wins::text').get().strip()
            loses = item.css('td.losses::text').get().strip()
            win_percentage = item.css('td.pct::text').get().strip()
            goals_for = item.css('td.gf::text').get().strip()
            goals_against = item.css('td.ga::text').get().strip()
            goals_difference = item.css('td.diff::text').get().strip()

            yield {
                'title': title,
                'year': year,
                'wins': wins,
                'losses': loses,
                'win_percentage': win_percentage,
                'goals_for': goals_for,
                'goals_against': goals_against,
                'goals_difference': goals_difference,
            }

        next_page = response.css('ul.pagination li:last-of-type a::attr(href)').get()
        new_url = response.urljoin(next_page)
        print('NEW URL', new_url)
        if next_page is not None:

            yield scrapy.Request(new_url, callback=self.parse)


if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl('hockey_teams')
    process.start()
