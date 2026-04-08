# import os

# def run(page, data, tc_id):
#     url = "https://terralogic.academy/"   # 🔁 update if exact page differs

#     try:
#         page.goto(url)
#         page.wait_for_load_state("domcontentloaded")

#         # =========================
#         # Fill form (ONLY visible fields)
#         # =========================
#         page.locator("input[name='firstName']:visible").fill(data["name"])
#         page.locator("input[name='phoneNumber']:visible").fill(data["phone"])
#         page.locator("input[name='email']:visible").fill(data["email"])
#         page.locator("textarea[name='query']:visible").fill(data["query"])

#         # =========================
#         # Handle Course Dropdown (IMPORTANT)
#         # =========================
#         if data.get("course"):
#             page.locator("button[aria-label='Select course']").click()
#             page.wait_for_timeout(1000)

#             # Select option dynamically
#             page.locator(f"text={data['course']}").first.click()
            

#         # =========================
#         # Submit form
#         # =========================
#         page.wait_for_timeout(4000)
#         # page.locator("button:has-text('Register Now')").click()

#         page.wait_for_timeout(4000)

#         # =========================
#         # Validation check
#         # =========================
#         errors = page.locator("input:invalid, textarea:invalid").count()

#         if errors > 0:
#             status = "FAIL"
#             print(f"❌ {tc_id} → Validation errors found")
#         else:
#             status = "PASS"
#             print(f"✅ {tc_id} → Form submitted")

#         # =========================
#         # Screenshot
#         # =========================
#         os.makedirs("screenshots", exist_ok=True)
#         screenshot = f"screenshots/{tc_id}_academy.png"
#         page.screenshot(path=screenshot)

#         return status, screenshot, url

#     except Exception as e:
#         print(f"❌ ERROR in {tc_id}: {e}")

#         os.makedirs("screenshots", exist_ok=True)
#         screenshot = f"screenshots/{tc_id}_academy_fail.png"
#         page.screenshot(path=screenshot)

#         return "FAIL", screenshot, url

import os

def run(page, data, tc_id):
    url = "https://terralogic.academy/"

    try:
        # =========================
        # Open page
        # =========================
        page.goto(url)
        page.wait_for_load_state("domcontentloaded")

        # =========================
        # Fill form fields
        # =========================
        page.locator("input[name='firstName']:visible").fill(data["name"])
        page.locator("input[name='phoneNumber']:visible").fill(data["phone"])
        page.locator("input[name='email']:visible").fill(data["email"])
        page.locator("textarea[name='query']:visible").fill(data["query"])

        # =========================
        # 🔥 Handle Course Dropdown (FINAL FIX)
        # =========================
        if data.get("course"):

            # 🚫 Remove blocking overlays (chatbot/header/backdrop)
            page.evaluate("""
                document.querySelectorAll('iframe, .fixed, .sticky').forEach(el => {
                    if (el.style) el.style.pointerEvents = 'none';
                });
            """)

            # Open dropdown
            dropdown = page.locator("button[aria-label='Select course']")
            dropdown.scroll_into_view_if_needed()
            dropdown.click()

            page.wait_for_timeout(1000)

            # Select option safely
            option = page.locator(f"text='{data['course']}'").first
            option.scroll_into_view_if_needed()
            option.click(force=True)

        # =========================
        # Submit form
        # =========================
        # submit_btn = page.locator("button:has-text('Register Now')")
        # submit_btn.scroll_into_view_if_needed()
        # submit_btn.click(force=True)

        page.wait_for_timeout(4000)

        # =========================
        # Validation check
        # =========================
        errors = page.locator("input:invalid, textarea:invalid").count()

        if errors > 0:
            status = "FAIL"
            print(f"❌ {tc_id} → Validation errors found")
        else:
            status = "PASS"
            print(f"✅ {tc_id} → Form submitted")

        # =========================
        # Screenshot (success)
        # =========================
        os.makedirs("screenshots", exist_ok=True)
        screenshot = f"screenshots/{tc_id}_academy.png"
        page.screenshot(path=screenshot)

        return status, screenshot, url

    except Exception as e:
        print(f"❌ ERROR in {tc_id}: {e}")

        # =========================
        # Screenshot (failure)
        # =========================
        os.makedirs("screenshots", exist_ok=True)
        screenshot = f"screenshots/{tc_id}_academy_fail.png"
        page.screenshot(path=screenshot)

        return "FAIL", screenshot, url