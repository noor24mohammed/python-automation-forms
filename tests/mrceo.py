import os
from utils.form_validation import validate_on_page

def run(page, data, tc_id):
    url = "https://mrceo.biz/contact-us/#investment"

    try:
        # ==============================
        # ✅ OPEN PAGE
        # ==============================
        page.goto(url)
        page.wait_for_load_state("domcontentloaded")

        # ✅ Scroll slowly (important)
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(4000)

        # ==============================
        # ✅ WAIT FOR REAL EMAIL FIELD
        # ==============================
        email_input = page.locator("input[type='email']:visible").first
        email_input.wait_for(timeout=15000)

        # ==============================
        # ✅ FILL FORM (FIELD-SPECIFIC)
        # ==============================
        # Using specific field names instead of index positions
        
        # Full Name
        page.fill("input[placeholder*='full name' i], input[name*='fullname' i], input[name*='full_name' i]", data["fullname"])
        page.wait_for_timeout(2000)

        # Mobile Number
        page.fill("input[type='tel'], input[placeholder*='mobile' i], input[name*='mobile' i]", data["mobile"])
        page.wait_for_timeout(2000)

        # Email
        page.fill("input[type='email']:visible", data["email"])
        page.wait_for_timeout(2000)

        # LinkedIn Profile
        page.fill("input[placeholder*='linkedin' i], input[name*='linkedin' i]", data["linkedin"])
        page.wait_for_timeout(2000)

        # Business Name
        page.fill("input[placeholder*='business' i], input[name*='business_name' i]", data["business_name"])
        page.wait_for_timeout(2000)

        # City
        page.fill("input[placeholder*='city' i], input[name*='city' i]", data["city"])
        page.wait_for_timeout(2000)

        # Business Email
        page.fill("input[placeholder*='business email' i], input[name*='business_email' i]", data["business_email"])
        page.wait_for_timeout(2000)

        # Website
        page.fill("input[placeholder*='website' i], input[name*='website' i]", data["website"])
        page.wait_for_timeout(2000)

        # Social Profile
        page.fill("input[placeholder*='social' i], input[name*='social' i]", data["social_profile"])
        page.wait_for_timeout(2000)

        # Optional fields
        if data.get("industry"):
            try:
                page.fill("input[placeholder*='industry' i], input[name*='industry' i]", data["industry"])
            except:
                pass
            page.wait_for_timeout(1000)

        if data.get("stage"):
            try:
                page.fill("input[placeholder*='stage' i], input[name*='stage' i]", data["stage"])
            except:
                pass
            page.wait_for_timeout(1000)

        # Textarea - Challenge/Message
        page.fill("textarea", data["challenge"])
        page.wait_for_timeout(2000)

        # ==============================
        # ✅ CHECKBOX (SAFE)
        # ==============================
        if page.locator("input[type='checkbox']:visible").count() > 0:
            page.locator("input[type='checkbox']:visible").first.check()

        # ==============================
        # ✅ CLICK CORRECT SUBMIT
        # ==============================
        page.wait_for_timeout(5000)
        # page.locator("button[type='submit']:visible").first.click()

        page.wait_for_timeout(5000)

        status = validate_on_page(page)

        # ==============================
        # ✅ SCREENSHOT
        # ==============================
        os.makedirs("screenshots", exist_ok=True)
        screenshot = f"screenshots/{tc_id}_mrceo.png"
        page.screenshot(path=screenshot)

        return status, screenshot, url

    except Exception as e:
        print("❌ MRCEO ERROR:", e)

        os.makedirs("screenshots", exist_ok=True)
        screenshot = f"screenshots/{tc_id}_mrceo_fail.png"
        page.screenshot(path=screenshot)

        return "FAIL", screenshot, url
