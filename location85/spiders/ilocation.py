# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import Location85Item


class InslocationSpider(scrapy.Spider):
    name = 'ilocation'
    # allowed_domains = ['https://www.instagram.com/explore/locations/']
    start_urls = ['https://www.instagram.com/explore/locations/?page=1']



    def parse(self, response):
        item = Location85Item()
        allcountry = re.findall(r'"country_list"(.+?)"next_page"', response.text)
        result_ids_and_slugs = re.findall('"id":"(.+?)","name":"(.+?)","slug":"(.+?)"', allcountry[0])
        for result_id_and_slug in result_ids_and_slugs:
            item["country_id"] = result_id_and_slug[0]
            item["country_name"] = result_id_and_slug[1]
            item["country_slug"] = result_id_and_slug[2]
            country_url = 'https://www.instagram.com/explore/locations/' + result_id_and_slug[0] +'/'+ result_id_and_slug[2] +'/'
            yield scrapy.Request(url=country_url,callback=self.parse_country,meta={'item':item})
        next_page = re.search('"next_page":(\d*?)', response.text)

        if next_page.group(1) != '':
            yield scrapy.Request(response.urljoin('?page=' + next_page.group(1)),callback=self.parse)
        else:
            pass


    def parse_country(self,response):
        allcity = re.findall(r'"city_list"(.+?)"next_page"', response.text)
        result_ids_and_slugs = re.findall('"id":"(.+?)","name":"(.+?)","slug":"(.+?)"', allcity[0])
        for result_id_and_slug in result_ids_and_slugs:
            item = response.meta['item']
            item["city_id"] = result_id_and_slug[0]
            item["city_name"] = result_id_and_slug[1]
            item["city_slug"] = result_id_and_slug[2]
            city_url = 'https://www.instagram.com/explore/locations/' + result_id_and_slug[0] + '/' + result_id_and_slug[2] + '/'
            yield scrapy.Request(url=city_url, callback=self.parse_city, meta={'item': item})
        next_page = re.search('"next_page":(\d*?)', response.text)
        if next_page.group(1) != '':
            yield scrapy.Request(response.urljoin('?page=' + next_page.group(1)),callback=self.parse_country)
        else:
            pass
    def parse_city(self,response):
        alllocation = re.findall(r'"location_list"(.+?)"next_page"', response.text)
        result_ids_and_slugs = re.findall('"id":"(.+?)","name":"(.+?)","slug":"(.+?)"', alllocation[0])
        for result_id_and_slug in result_ids_and_slugs:
            item = response.meta['item']
            item["location_id"] = result_id_and_slug[0]
            item["location_name"] = result_id_and_slug[1]
            item["location_slug"] = result_id_and_slug[2]
            yield item
        next_page = re.search('"next_page":(\d*?)', response.text)
        if next_page.group(1) != '':
            yield scrapy.Request(response.urljoin('?page=' + next_page.group(1)),callback=self.parse_city)
        else:
            pass