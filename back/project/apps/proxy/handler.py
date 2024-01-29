from urllib.parse import urljoin
from urllib.parse import urlparse

import httpx
from bs4 import BeautifulSoup as BS


class ProxyHelper:

    @staticmethod
    def internal_route(path) -> str:
        return 'http://127.0.0.1/proxy/' + path

    @staticmethod
    def update_tag_attribute(tag, site, path, attribute):
        original_url = urljoin(path, tag[attribute])

        if urlparse(original_url).netloc == urlparse(path).netloc:
            if site.site not in tag[attribute]:
                tag[attribute] = site.site + tag[attribute]

            tag[attribute] = ProxyHelper.internal_route(
                site.site + tag[attribute] if tag[attribute].endswith('/') else tag[attribute]
            )


class ProxyActions:

    @staticmethod
    def perform_proxy_actions(site, path, query, headers):
        client = httpx.Client(follow_redirects=True)
        # icecream.ic(path)
        if not query:
            # icecream.ic(path)
            req = client.get(path, headers=headers).text
        else:
            req = client.get(path + '?' + query, headers=headers).text
        soup = BS(req, 'html.parser')

        for a_tag in soup.find_all('a', href=True):
            ProxyHelper.update_tag_attribute(a_tag, site, path, 'href')

        for form_tag in soup.find_all('form', action=True):
            ProxyHelper.update_tag_attribute(form_tag, site, path, 'action')

        site.traffic += len(req.encode('utf-8'))
        site.save()

        modified_html = str(soup)
        return modified_html

    @staticmethod
    def clear_path(path: str, protocol: str, check_protocol: str) -> str:
        if protocol not in path and check_protocol in path:
            path = path.replace(check_protocol, protocol)
        return path
