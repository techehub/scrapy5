# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup as bs
from ..items import ExpertzlabItem

class ExpertzlabSpider(scrapy.Spider):
    name = 'expertzlab'
    allowed_domains = ['expertzlab.com']
    start_urls = ['http://www.expertzlab.com/courses.html']
    '''
    def parse(self, response):
        # print (response.text)
        coursename = response.xpath('//div[@class="course"]/h4/text()').getall()
        desc = response.xpath('//div[@class="course"]/p/text()').getall()
        data={ k:v for k, v in zip (coursename, desc)}
        return data
    '''

    def parse(self, response):
        soup = bs(response.text, 'html5lib')
        courses = soup.findAll('div', attrs={'class': 'course'})

        for course in courses:
            item = ExpertzlabItem()
            item['name'] = course.h4.text
            item['desc'] = course.p.text
            item['duration'] = course.ul.li.text

            yield item
