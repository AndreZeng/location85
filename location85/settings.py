# -*- coding: utf-8 -*-

# Scrapy settings for location85 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'location85'

SPIDER_MODULES = ['location85.spiders']
NEWSPIDER_MODULE = 'location85.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'location85 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'location85.middlewares.Location85SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'location85.middlewares.Location85DownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'location85.pipelines.Location85Pipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# -----------------------------------------------------------------------------
# ROTATED PROXY SETTINGS (Spider Settings Backend)
# -----------------------------------------------------------------------------
DOWNLOADER_MIDDLEWARES.update({
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': None,
    'scrapy_rotated_proxy.downloadmiddlewares.proxy.RotatedProxyMiddleware': 750,
})
ROTATED_PROXY_ENABLED = True
PROXY_STORAGE = 'scrapy_rotated_proxy.extensions.file_storage.FileProxyStorage'
# When set PROXY_FILE_PATH='', scrapy-rotated-proxy
# will use proxy in Spider Settings default.
PROXY_FILE_PATH = ''
HTTP_PROXIES = [
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28824',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28825',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28826',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28827',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28828',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28829',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28830',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28831',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28832',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28833',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28834',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28835',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28836',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28837',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28838',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28839',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28840',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28841',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28842',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28843',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28844',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28845',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28846',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28847',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28848',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28849',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28850',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28851',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28852',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28853',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28854',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28855',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28856',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28857',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28858',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28859',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28860',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28861',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28862',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28863',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28864',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28865',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28866',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28867',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28868',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28869',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28870',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28871',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28872',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28873',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28874',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28875',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28876',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28877',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28878',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28879',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28880',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28881',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28882',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28883',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28884',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28885',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28886',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28887',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28888',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28889',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28890',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28891',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28892',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28893',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28894',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28895',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28896',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28897',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28898',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28899',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28900',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28901',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28902',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28903',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28904',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28905',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28906',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28907',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28908',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28909',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28910',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28911',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28912',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28913',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28914',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28915',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28916',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28917',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28918',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28919',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28920',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28921',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28922',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28923'

]
HTTPS_PROXIES = [
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28824',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28825',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28826',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28827',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28828',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28829',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28830',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28831',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28832',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28833',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28834',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28835',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28836',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28837',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28838',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28839',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28840',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28841',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28842',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28843',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28844',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28845',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28846',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28847',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28848',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28849',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28850',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28851',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28852',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28853',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28854',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28855',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28856',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28857',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28858',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28859',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28860',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28861',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28862',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28863',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28864',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28865',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28866',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28867',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28868',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28869',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28870',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28871',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28872',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28873',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28874',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28875',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28876',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28877',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28878',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28879',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28880',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28881',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28882',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28883',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28884',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28885',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28886',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28887',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28888',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28889',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28890',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28891',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28892',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28893',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28894',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28895',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28896',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28897',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28898',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28899',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28900',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28901',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28902',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28903',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28904',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28905',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28906',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28907',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28908',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28909',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28910',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28911',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28912',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28913',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28914',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28915',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28916',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28917',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28918',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28919',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28920',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28921',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28922',
    'http://zengboling:GWjn3jj53fc@107.181.187.120:28923'

]