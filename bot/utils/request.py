import json

import requests

from requests import Response

from urllib.parse import urljoin


class Requests:
    url: str = None
    headers = None
    proxy = None
    cookies = None
    data = None
    timeout = 60

    def __init__(self, url: str, headers=None, proxy=None, cookies=None, timeout=None, data=None):
        self.set_request_settngs(headers, proxy, cookies, timeout, data)
        self.set_url(url)

    def set_request_settngs(self, headers, proxy, cookies, timeout, data):
        if headers is not None:
            self.headers = headers

        if proxy is not None:
            self.proxy = proxy

        if cookies is not None:
            self.cookies = cookies

        if timeout is not None:
            self.timeout = timeout

        if data is not None:
            self.data = json.dumps(data)

    def get(self, link_addition: str = None, headers=None, proxy=None, cookies=None, timeout=None,
            data=None) -> Response:
        url = self.url
        if link_addition is not None:
            url = urljoin(self.url, link_addition)
        if data is not None:
            data = json.dumps(data)

        return requests.get(url=url, headers=headers or self.headers, proxies=proxy or self.proxy,
                            cookies=cookies or self.cookies, timeout=timeout or self.timeout, data=data or self.data)

    def post(self, link_addition: str = None, headers=None, proxy=None, cookies=None, timeout=None,
             data=None) -> Response:
        url = self.url
        if link_addition is not None:
            url = urljoin(self.url, link_addition)
        if data is not None:
            data = json.dumps(data)

        return requests.post(url=url, headers=headers or self.headers, proxies=proxy or self.proxy,
                             cookies=cookies or self.cookies, timeout=timeout or self.timeout, data=data or self.data)

    def set_url(self, url: str):
        self.url = url
