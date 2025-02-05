import re
from playwright.sync_api import sync_playwright


class element:

    def __init__(
        self,
        playwright_element,
    ):

        self.playwright_element = playwright_element

    def text(
        self,
    ):

        return self.playwright_element.inner_text()

    def re(
        self,
        pattern,
    ):

        text = self.playwright_element.inner_text()

        return re.search(pattern, text).group(0)

    def value(
        self,
        value,
    ):

        self.playwright_element.select_option(value=str(value))

    def attribute(
        self,
        key,
        value
    ):

        if value is None:

            return self.playwright_element.get_attribute(key)

        else:

            return self.playwright_element.set_attribute(key, value)

    def __getattr__(
        self,
        name,
    ):

        return getattr(self.playwright_page, name)


class browser:

    def __init__(
        self,
        url,
    ):

        self.playwright = sync_playwright().start()

        width = 5120/2
        height = 2880/2

        browser = self.playwright.chromium.launch(
            headless=False,
            args=[
                f'--window-position=2560,0'
            ]
        )

        context = browser.new_context(
            viewport={
                'width': width,
                'height': height
            },
        )

        self.playwright_page = context.new_page()

        self.playwright_page.goto(url)

    def select(
        self,
        selector,
    ):

        return self.playwright_page.query_selector(selector)

    def select_all(
        self,
        selector,
    ):

        return self.playwright_page.query_selector_all(selector)

    def select_by_text(
        self,
        text,
    ):

        return self.playwright_page.get_by_text(text)

    def fill_email(
        self,
        email,
    ):

        return self.playwright_page.fill('[type="email"]', email)

    def fill_password(
        self,
        email,
    ):

        return self.playwright_page.fill('[type="password"]', email)

    def __getattr__(
        self,
        name,
    ):

        return getattr(self.playwright_page, name)
