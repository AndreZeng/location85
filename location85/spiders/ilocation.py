# -*- coding: utf-8 -*-
import scrapy
import re

from ..items import Location85Item


class IlocationSpider(scrapy.Spider):
    name = 'ilocation'
    # allowed_domains = ['https://www.instagram.com/explore/locations/?page=']
    start_urls = ['https://www.instagram.com/explore/locations/?page=']

    def parse(self, response):
        result_ids_and_slugs = re.findall('"id":"(.+?)","name":"(.+?)","slug":"(.+?)"', response.text)
        for result_id_and_slug in result_ids_and_slugs:
            item = Location85Item()
            item["country_id"] = result_id_and_slug[0]
            item["country_name"] = result_id_and_slug[1]
            item["country_slug"] = result_id_and_slug[2]
            country_url = 'https://www.instagram.com/explore/locations/' + result_id_and_slug[0] +'/'+ result_id_and_slug[2] +'/'
            yield scrapy.Request(url=country_url,callback=self.parse_country,meta={'item':item})
            next_page = re.search('"next_page":(\d*)', response.text)
            if next_page.group(1) != '':
                yield scrapy.Request(response.urljoin('?page=' + next_page.group(1)),callback=self.parse)

    def parse_country(self, response):
        item = response.meta['item']
        result_ids_and_slugs = re.findall('"id":"([a-z0-9]+?)","name":"(.+?)","slug":"(.+?)"', response.text)
        # parentID = re.search('country_info":{"id":"(.+?)","name"', response.text)
        # print(parentID[1])
        # result_slugs = re.findall('"slug":"(.+?)"', response.text)
        for result_id_and_slug in result_ids_and_slugs:
            item["city_id"] = result_id_and_slug[0]
            item["city_name"] = result_id_and_slug[1]
            item["city_slug"] = result_id_and_slug[2]
            # item["parentID"] = parentID[1]
            city_url = 'https://www.instagram.com/explore/locations/' + result_id_and_slug[0] + '/' + result_id_and_slug[2] + '/'
            yield scrapy.Request(url=city_url, callback=self.parse_city, meta={'item': item})
            next_page = re.search('"next_page":(\d*)', response.text)
            if next_page.group(1) != '':
                yield scrapy.Request(response.urljoin('?page=' + next_page.group(1)),callback=self.parse_country)

    def parse_city(self, response):
        item = response.meta['item']
        result_ids_and_slugs = re.findall('"id":"([0-9]+?)","name":"(.+?)","slug":"(.+?)"', response.text)
        for result_id_and_slug in result_ids_and_slugs:
            item = response.meta['item']
            item["location_id"] = result_id_and_slug[0]
            item["location_name"] = result_id_and_slug[1]
            item["location_slug"] = result_id_and_slug[2]
            yield item
        next_page = re.search('"next_page":(\d*)',response.text)
        if next_page.group(1) != '':
            yield scrapy.Request(response.urljoin('?page='+next_page.group(1)),callback=self.parse_city)