Downloads proxies from `https://www.sslproxies.org/` and saves them to a text file.
in `pipelines.py` change directory of text file where to save them.

If running linux task can be automated with crontab

Create a bash script

```
source /*source to your virtual env */
cd /* change directory to spider */
PATH=$PATH:/user/local/bin
export PATH
scrapy crawl hun73r
```

To crawl for proxies every 30 min write to crontab
` */30 * * * * /path_to_bash_script.sh`


