# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HockeyTeamsItem(scrapy.Item):
    name = scrapy.Field()
    year = scrapy.Field()
    wins = scrapy.Field()
    loses = scrapy.Field()
    win_percentage = scrapy.Field()
    goals_for = scrapy.Field()
    goals_against = scrapy.Field()
    goals_difference = scrapy.Field()
