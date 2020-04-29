import requests


class HunterPipeline(object):

    def process_item(self, item, spider):
        file = open('/home/h1dd3n/Desktop/proxy2.txt', 'a')
        proxy = self._check_proxy(item)
        if proxy is not False:
            file.write('https://' + str(proxy).split("'")[-2] + '\n')
            file.close()
        return item

    def _check_proxy(self, item):
        try:
            proxy = '%s:%s' % (item['ip'], item['port'])
            proxy = dict(https=proxy)
            request = requests.request('GET', 'https://google.com', proxies=proxy,
                                       timeout=(10, 10))
            print('-' * 10)
            print('Checking proxy ' + str(proxy))
            print('-' * 10)
            if request.status_code == 200:
                print('Found')
                request.close()
                return proxy
            else:
                return False
        except Exception as e:
            print(e)
            return False
