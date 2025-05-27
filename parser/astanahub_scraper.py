from playwright.sync_api import sync_playwright, Error as PlaywrightError
from .models import AstanaHubCompany
from config import TECHPARK_URL, TECHPARK_TIMEOUT
import logging

logger = logging.getLogger(__name__)


def scrape_companies():
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(TECHPARK_URL, timeout=TECHPARK_TIMEOUT)
            page.evaluate("window.scrollBy(0, document.body.scrollHeight)")
            page.wait_for_timeout(5000)

            rows = page.query_selector_all("tbody tr")
            AstanaHubCompany.objects.all().delete()

            for row in rows[:10]:
                try:
                    cols = row.query_selector_all("td")
                    AstanaHubCompany.objects.create(
                        number=cols[0].inner_text().strip(),
                        date_start=cols[1].inner_text().strip(),
                        date_end=cols[2].inner_text().strip(),
                        bin=cols[3].inner_text().strip(),
                        status=cols[4].inner_text().strip(),
                        name=cols[5].inner_text().strip(),
                    )
                except Exception as e:
                    logging.warning(f"Ошибка при разборе строки: {e}")

            browser.close()
    except PlaywrightError as e:
        logging.error(f"Ошибка Playwright: {e}")
    except Exception as e:
        logging.error(f"Общая ошибка при парсинге: {e}")
