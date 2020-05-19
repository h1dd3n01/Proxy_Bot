# Proxy_Bot



You can specify the path to your proxy file with -a filepath='myfilepath'

`crontab` to run every 30 seconds ->  */30 * * * * /usr/local/bin/crawl_proxies.sh

example of my bash script

'''
#!/bin/bash

source /home/h1dd3n/Desktop/projects/proxy_bot/proxy_bot_env/bin/activate
cd /home/h1dd3n/Desktop/projects/proxy_bot/hunter/hunter/spiders/
PATH=$PATH:/user/local/bin
export PATH
scrapy crawl hun73r -a filepath='/home/h1dd3n/Desktop/proxy2.txt'

'''
