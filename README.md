# discordfeed


### How to use

```
from ytfeed import *

if __name__ == '__main__':
    ytchannel_id ='xxx' # youtube channel id
    webhook_url = 'yyy' # discord webhook url
    check_ytchannel(ytchannel_id=ytchannel_id, webhook_url=webhook_url, word='')
    schedule.every(2).hours.do(lambda: check_ytchannel(ytchannel_id=ytchannel_id, webhook_url=webhook_url, word=''))
    while True:
        schedule.run_pending()
        time.sleep(1)
```
