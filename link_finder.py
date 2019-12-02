from html.parser import HTMLParser
from urllib import parse


# A new class that inherits HTMLParser
class LinkFinder(HTMLParser):

    # Initializer method
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    # When we call HTMLParser feed(), this is called
    # and when it finds a start tag of <a>
    # then it appends the base url if not present
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    def page_links(self):
        return self.links

    # Abstract method
    def error(self, message):
        pass
