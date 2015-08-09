__author__ = 'huanyu'
# -*- coding: utf-8 -*-
#!/usr/bin/env python

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import scrapy


me = "huanyu_zh@126.com"
you = ['huanyu_zh@126.com','945938362@qq.com']
msg = MIMEMultipart('alternative')
msg['Subject'] = u"自住房信息"
msg['From'] = me
msg['To'] = ",".join( you )
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       你好吗？<br>
       Here is the <a href="https://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""
class ZiZhuHouseSpider(scrapy.Spider):
    name = "ZiZhuHouse"
    allowed_domains = ["bjjs.gov.cn"]
    start_urls = ["http://www.bjjs.gov.cn/publish/portal0/tab4021/"]



    def send_email(self,to_list,subject,content):
        part2 = MIMEText(content, 'html','utf-8')
        msg.attach(part2)
        try:
            for i in range(0,you.__len__()):
                s = smtplib.SMTP('smtp.126.com')
            # sendmail function takes 3 arguments: sender's address, recipient's address
            # and message to send - here it is sent as one string.
                s.login("huanyu_zh@126.com","2Wsxcde3")

                s.sendmail(me, you[i], msg.as_string())
                s.quit()
            return True
        except Exception, e:
            print str(e)
            return False


    def parse(self,response):
        contentXpath = response.xpath('//table[@id=\'ess_ctr10073_ListC_Info_LstC_Info\']')
        contentList = contentXpath.extract()

        for i in range(0,contentList.__len__()):
            contentList[i] = str(contentList[i].encode('utf-8'))

        content = ""
        content = content.join(contentList)

        if self.send_email("huanyu_zh@126.com","zizhuHouse",content):
            print "########发送成功#########\n"
        else:
            print "#######发送失败##########\n"


