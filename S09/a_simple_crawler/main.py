import  re
import urllib.request


class Browser:
    instances = []

    def __init__(self, url):
        if url in [s.url for s in self.instances]:
            print("duplicated url", url)
        self.instances.append(self)
        self.__url = url
        self.__text = None

    @property
    def url(self):
        return self.__url

    @property
    def text(self):
        if self.__text is None:
            fp = urllib.request.urlopen(self.__url)
            self.__text = fp.read().decode("utf8")
            fp.close()
        return self.__text

    @property
    def get_links(self):
        pat = r'href=[\'"]?(https?://[^\'" >]+)'
        res = re.findall(pat, self.text)
        return [Browser(r) for r in res]








b = Browser('https://www.python.org')
c = Browser('https://www.python.org')
print(b.get_links)
