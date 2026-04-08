import os

def run(page, data, tc_id):   # ✅ colon added
    try:
        url = "https://saburi.works/contact/"
        page.goto(url)

        page.wait_for_selector("input[name='fname']")
        page.wait_for_timeout(3000)
        page.fill("input[name='fname']", data["name"])
        page.wait_for_timeout(3000)
        page.fill("input[name='email']", data["email"])
        page.wait_for_timeout(3000)
        page.fill("input[name='phonenumber']", data["phone"])
        page.wait_for_timeout(3000)
        page.fill("input[name='companyname']", data["company"])
        page.wait_for_timeout(3000)
        page.select_option("select[name='city']", data["city"])
        page.wait_for_timeout(3000)
        page.select_option("select[name='lookingFor']", data["service"])
        page.wait_for_timeout(3000)
        page.fill("textarea[name='message']", data["message"])


        page.wait_for_timeout(5000)
        # page.click("input[type='submit']")

        os.makedirs("screenshots", exist_ok=True)
        screenshot = f"screenshots/{tc_id}_saburi.png"
        page.screenshot(path=screenshot)

        return "PASS", screenshot, url

    except Exception as e:
        print("❌ Saburi ERROR:", e)
        return "FAIL", "", url