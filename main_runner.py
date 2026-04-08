import json
from playwright.sync_api import sync_playwright
from utils.excel_writer import write_result, save

from tests import general, saburi, enquiry, shankara, mrceo

forms = {
    "1": ("general", general, "data/general.json"),
    "2": ("saburi", saburi, "data/saburi.json"),
    "3": ("enquiry", enquiry, "data/enquiry.json"),
    "4": ("shankara", shankara, "data/shankara.json"),
    "5": ("mrceo", mrceo, "data/mrceo.json")
}


def run_form(page, name, module, file):
    with open(file) as f:
        test_data = json.load(f)

    for i, data in enumerate(test_data, start=1):
        tc_id = f"{name.upper()}_TC_{i}"   # ✅ UNIQUE TC ID

        print(f"➡ Running {tc_id}")

        status, screenshot, url = module.run(page, data, tc_id)  # ✅ FIX

        print(f"✅ {status}")

        write_result(
            name,
            url,
            status,
            screenshot,
            data
        )

def show_menu():
    print("\n========= FORM MENU =========")
    print("1. General")
    print("2. Saburi")
    print("3. Enquiry")
    print("4. Shankara")
    print("5. MRCEO")
    print("6. Run ALL")
    print("=============================\n")


if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        show_menu()
        choice = input("Enter choice: ")

        if choice == "6":
            for key in forms:
                name, module, file = forms[key]
                run_form(page, name, module, file)
        elif choice in forms:
            name, module, file = forms[choice]
            run_form(page, name, module, file)
        else:
            print("Invalid choice")

        save()
        page.wait_for_timeout(3000)
        browser.close()