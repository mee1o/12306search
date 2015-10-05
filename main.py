# -*- coding: utf-8 -*-
import web
import search
import model

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

urls = (
    '/', 'Search',
    '/multiple', 'MultipleDays'
)

web.config.debug = True

render = web.template.render('templates')

class Search():
    def GET(self):
        return render.search([], {'date':'2015-01-27', 'from':'北京', 'to':'成都'})
    
    def POST(self):
        x = web.input()
        data = search.getInfoByUrl(str(x['date']),str(x['from']),str(x['to']))
        return render.search(data, x)


class MultipleDays():
    def GET(self):
        return render.multiple([])
                
app = web.application(urls, globals())

if __name__=="__main__":
    app.run()