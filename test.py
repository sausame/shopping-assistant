import sys

from js import JsExecutor

def execute(executor, title, url):
    value = 'requestPriceInfo("{}", "{}")'.format(title, url)

    return executor.execute(value)

if __name__ == '__main__':

    reload(sys)
    sys.setdefaultencoding('utf8')

    executor = JsExecutor('huihui/huihui.js')
    url = execute(executor, "Lebond", "http://item.jd.com/962374.html")

    print url

