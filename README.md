# Proxy_Bot

To run every 30 seconds in crontab ` */30 * * * * /usr/local/bin/crawl_proxies.sh`


Example of bash script


`#!/bin/bash`

`source /home/h1dd3n/Desktop/projects/proxy_bot/proxy_bot_env/bin/activate`

`cd /home/h1dd3n/Desktop/projects/proxy_bot/hunter/hunter/spiders/`

`PATH=$PATH:/user/local/bin`

`export PATH`

`scrapy crawl hun73r -a filepath='/home/h1dd3n/Desktop/proxy2.txt'`

`-a filepath` is required to specifiy your proxy text file. If the file does not exists, it will create a new one.
