import os
from utils.form_validation import validate_on_page

def run(page, data, tc_id):
    url = "https://lollypop.terralogic.com/project-enquiry/"

    try:
        page.goto(url)
        page.wait_for_timeout(5000)
        page.wait_for_load_state("domcontentloaded")

        # ✅ FIXED SELECTORS (VERY IMPORTANT)
        page.fill("textarea[name='description']", data["description"])
        page.wait_for_timeout(5000)
        page.fill("input[name='full_name']", data["name"])   # ❌ was #name
        page.wait_for_timeout(5000)
        page.fill("input[name='email']", data["email"])
        page.wait_for_timeout(5000)
        page.fill("input[name='phone']", data["phone"])
        page.wait_for_timeout(5000)

        if data.get("offer_code"):
            page.fill("input[name='free_design']", data["offer_code"])

        page.wait_for_timeout(5000)
        # page.click("input[type='submit']")

        status = validate_on_page(page)

        os.makedirs("screenshots", exist_ok=True)
        screenshot = f"screenshots/{tc_id}_enquiry.png"
        page.screenshot(path=screenshot)

        return status, screenshot, url

    except Exception as e:
        print("❌ ERROR:", e)

        screenshot = f"screenshots/{tc_id}_enquiry_fail.png"
        page.screenshot(path=screenshot)

        return "FAIL", screenshot, url

        