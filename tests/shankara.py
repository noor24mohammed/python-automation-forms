import os
from utils.form_validation import validate_on_page

def run(page, data, tc_id):
    url = "https://shankarbaba.org/contact-us/"
    page.wait_for_timeout(3000)

    try:
        page.goto(url)
        page.wait_for_timeout(3000)
        page.wait_for_selector("input[name='username']")
        page.wait_for_timeout(3000)
        page.fill("input[name='username']", data["name"])
        page.wait_for_timeout(3000)
        page.fill("input[name='mobile-number']", data["mobile"])
        page.wait_for_timeout(3000)
        page.fill("input[name='email']", data["email"])
        page.wait_for_timeout(3000)
        page.fill("input[name='address']", data["address"])
        page.wait_for_timeout(3000)
        page.fill("textarea[name='message']", data["message"])
        

        page.wait_for_timeout(5000)
        # page.click("input[type='submit']")

        status = validate_on_page(page)

        os.makedirs("screenshots", exist_ok=True)
        screenshot = "screenshots/shankara.png"
        page.screenshot(path=screenshot)

        return status, screenshot, url

    except Exception as e:
        print("❌ Shankara ERROR:", e)
        return "FAIL", "", url