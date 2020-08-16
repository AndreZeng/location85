# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import Location85Item


class InslocationSpider(scrapy.Spider):
    name = 'ilocation'
    # allowed_domains = ['https://www.instagram.com/explore/locations/']
    start_urls = ['https://www.instagram.com/explore/locations/?page=1']



    def parse(self, response):
        # item = Location85Item()
        allcountry = re.findall(r'"country_list"(.+?)"next_page"', response.text)
        result_ids_and_slugs = re.findall('"id":"(.+?)","name":"(.+?)","slug":"(.+?)"', allcountry[0])
        for result_id_and_slug in result_ids_and_slugs:
            # item["country_id"] = result_id_and_slug[0]
            # item["country_name"] = result_id_and_slug[1]
            # item["country_slug"] = result_id_and_slug[2]
            country_url = 'https://www.instagram.com/explore/locations/' + result_id_and_slug[0] + '/' + \
                          result_id_and_slug[2] + '/'
            # print(country_url)
            yield scrapy.Request(url=country_url, callback=self.parse_country)
        next_page = re.search('"next_page":(\d+)', response.text)
        if next_page != None:

            yield scrapy.Request(response.urljoin('?page=' + next_page.group(1)), callback=self.parse)
        else:
            pass



    def parse_country(self,response):
        # item = response.meta['item']
        #这一步确定item传递过程中不出错，保证item的连贯性
        # country_information = re.findall(r'""country_info"(.+?)"city_list"',response.text)
        # country_information_ids = re.findall('"id":"(.+?)","name":"(.+?)","slug":"(.+?)"', country_information[0])
        # country_id = country_information_ids[0]
        # country_name = country_information_ids[1]
        # country_slug = country_information_ids[2]
        # item["country_id"] = country_id
        # item["country_name"] = country_name
        # item["country_slug"] = country_slug
        allcity = re.findall(r'"city_list"(.+?)"next_page"', response.text)
        result_ids_and_slugs = re.findall('"id":"(.+?)","name":"(.+?)","slug":"(.+?)"', allcity[0])

        for result_id_and_slug in result_ids_and_slugs:

            # item["city_id"] = result_id_and_slug[0]
            # item["city_name"] = result_id_and_slug[1]
            # item["city_slug"] = result_id_and_slug[2]
            # print(item)
            city_url = 'https://www.instagram.com/explore/locations/' + result_id_and_slug[0] + '/' + result_id_and_slug[2] + '/'
            yield scrapy.Request(url=city_url, callback=self.parse_location)
        next_page = re.search('"next_page":(\d+)', response.text)
        if next_page != None:
            yield scrapy.Request(response.urljoin('?page=' + next_page.group(1)),callback=self.parse_country)
        else:
            pass

    def parse_location(self, response):
        item = Location85Item()
        country_information = re.findall(r'"country_info"(.+?)"city_info"', response.text)
        country_information_ids = re.findall('"id":"(.+?)","name":"(.+?)","slug":"(.+?)"', country_information[0])
        country_id = country_information_ids[0][0]
        country_name = country_information_ids[0][1]
        country_slug = country_information_ids[0][2]
        item["country_id"] = country_id
        item["country_name"] = country_name
        item["country_slug"] = country_slug

        city_information = re.findall(r'"city_info"(.+?)"location_list"', response.text)
        city_information_ids = re.findall('"id":"(.+?)","name":"(.+?)","slug":"(.+?)"', city_information[0])
        city_id = city_information_ids[0][0]
        city_name = city_information_ids[0][1]
        city_slug = city_information_ids[0][2]
        item["city_id"] = city_id
        item["city_name"] = city_name
        item["city_slug"] = city_slug

        alllocation = re.findall(r'"location_list"(.+?)"next_page"', response.text)
        result_ids_and_slugs = re.findall('"id":"(.+?)","name":"(.+?)","slug":"(.+?)"', alllocation[0])
        for result_id_and_slug in result_ids_and_slugs:
            item["location_id"] = result_id_and_slug[0]
            item["location_name"] = result_id_and_slug[1]
            item["location_slug"] = result_id_and_slug[2]
            yield item
        next_page = re.search('"next_page":(\d+)', response.text)
        if next_page != None:
            yield scrapy.Request(response.urljoin('?page=' + next_page.group(1)),callback=self.parse_location)
        else:
            pass