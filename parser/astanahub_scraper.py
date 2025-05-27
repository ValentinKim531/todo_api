import time
from playwright.sync_api import sync_playwright
from .models import AstanaHubCompany
from config import TECHPARK_URL, TECHPARK_TIMEOUT


def scrape_companies():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(TECHPARK_URL, timeout=TECHPARK_TIMEOUT)

        page.evaluate("window.scrollBy(0, document.body.scrollHeight)")
        time.sleep(5)

        rows = page.query_selector_all("tbody tr")

        AstanaHubCompany.objects.all().delete()

        for row in rows[:10]:
            cols = row.query_selector_all("td")
            if len(cols) >= 6:
                AstanaHubCompany.objects.create(
                    number=cols[0].inner_text().strip(),
                    date_start=cols[1].inner_text().strip(),
                    date_end=cols[2].inner_text().strip(),
                    bin=cols[3].inner_text().strip(),
                    status=cols[4].inner_text().strip(),
                    name=cols[5].inner_text().strip(),
                )
        browser.close()
