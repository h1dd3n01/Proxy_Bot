import requests
from itertools import chain
import os


class HunterPipeline:
    proxies = []

    def process_item(self, item, spider):
        proxy = self._check_proxy(item)
        if proxy is not False:
            proxy = 'https://' + str(proxy).split("'")[-2] + '\n'
            self.proxies.append(proxy)
            print('Appended {} to list'.format(proxy))
            print('List count is {}'.format(len(self.proxies)))
        return item

    def _check_proxy(self, item):
        try:
            proxy = '%s:%s' % (item['ip'], item['port'])
            proxy = dict(https=proxy)
            print('-' * 10)
            print('Checking proxy ' + str(proxy))
            print('-' * 10)
            request = requests.request('GET', 'https://google.com', proxies=proxy,
                                       timeout=(10, 10))
            if request.status_code == 200:
                request.close()
                return proxy
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def close_spider(self, spider):
        print('Spider finished scraping, testing proxies.')
        print('Current number of proxies in list {}'.format(len(self.proxies)))
        if os.path.isfile(spider.filepath):
            proxy_list = list(open(spider.filepath))
            new_list = set(chain(proxy_list, self.proxies))
            os.remove(spider.filepath)
            with open(spider.filepath, 'a') as f:
                for i in new_list:
                    f.write(i)
                f.close()
        else:
            with open(spider.filepath, 'a') as f:
                for i in self.proxies:
                    f.write(i)
                f.close()

