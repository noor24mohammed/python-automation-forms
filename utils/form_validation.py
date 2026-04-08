import re


def normalize_expected(expected):
    if expected is None:
        return None

    return str(expected).strip().upper()


def evaluate_test_result(actual_status, expected):
    expected = normalize_expected(expected)

    if expected == "PASS":
        return "PASS" if actual_status == "PASS" else "FAIL"
    if expected == "FAIL":
        return "PASS" if actual_status == "FAIL" else "FAIL"

    return actual_status


def is_form_valid(page):
    try:
        return page.evaluate(r"""
            () => {
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                const phoneRegex = /^[0-9]{10,15}$/;
                const fields = Array.from(document.querySelectorAll(
                    'input[name]:not([type=hidden]):not([disabled]), textarea[name]:not([disabled]), select[name]:not([disabled])'
                )).filter(el => {
                    if (!(el.offsetParent || el.getClientRects().length)) return false;
                    return true;
                });

                return fields.every(el => {
                    if (!el.checkValidity()) {
                        return false;
                    }

                    const name = (el.name || '').toLowerCase();
                    const type = (el.type || '').toLowerCase();
                    const value = (el.value || '').trim();

                    if ((type === 'email' || name.includes('email')) && value.length > 0) {
                        if (!emailRegex.test(value)) {
                            return false;
                        }
                    }

                    if ((type === 'tel' || name.includes('phone') || name.includes('mobile')) && value.length > 0) {
                        if (!phoneRegex.test(value)) {
                            return false;
                        }
                    }

                    return true;
                });
            }
        """)
    except Exception:
        return True


def has_form_error_message(page):
    try:
        return page.evaluate(r"""
            () => {
                return Array.from(document.querySelectorAll(
                    '[class*=error i], [class*=invalid i], [class*=required i], [aria-invalid="true"]'
                ))
                .filter(el => el.offsetParent || el.getClientRects().length)
                .some(el => {
                    const text = (el.innerText || '').trim();
                    return /error|invalid|required|please enter|please select|must be/i.test(text);
                });
            }
        """)
    except Exception:
        return False


def validate_on_page(page):
    if not is_form_valid(page):
        return "FAIL"
    if has_form_error_message(page):
        return "FAIL"

    return "PASS"
