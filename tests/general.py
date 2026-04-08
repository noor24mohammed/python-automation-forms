import os

def run(page, data, tc_id):
    try:
        url = "https://lollypop.design/general-enquiry/"
        page.goto(url)
        page.wait_for_timeout(3000)
        page.wait_for_load_state("load")

        page.fill("textarea[name='description']", data["description"])
        page.wait_for_timeout(3000)
        page.fill("#full_name", data["full_name"])
        page.wait_for_timeout(3000)
        page.fill("#email", data["email"])
        page.wait_for_timeout(3000)
        page.fill("#phone", data["phone"])

        page.wait_for_timeout(5000)
        # page.click("input[type='submit']")


        # Screenshot folder
        os.makedirs("screenshots", exist_ok=True)
        screenshot_path = f"screenshots/{tc_id}_general.png"

        page.screenshot(path=screenshot_path)

        return "PASS", screenshot_path, url

    except Exception as e:
        print("❌ ERROR:", e)
        return "FAIL", "", url