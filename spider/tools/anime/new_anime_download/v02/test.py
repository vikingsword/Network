# !usr/bin/env python
# -*- coding:utf-8 _*-

from download_anime import init_driver

driver = init_driver()

driver.get('https://www.ntdm9.com/play/5160-1-17.html')
res = driver.page_source
print(res)
