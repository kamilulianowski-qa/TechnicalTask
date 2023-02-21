from assertpy import assert_that


def test_failed_payment(login_page, dashboard_main_page, pricing_page, payment_status_page, card_frame,
                        base_user, base_document, invalid_card):
    login_page.wait_for_page_load()
    login_page.accept_cookies()
    login_page.login(base_user.email, base_user.password)

    assert_that(dashboard_main_page.check_if_document_is_visible(base_document)).is_true()

    dashboard_main_page.download_cv()
    pricing_page.click_continue()
    card_frame.fill_form(invalid_card)
    card_frame.submit()

    assert_that(payment_status_page.invalid_payment_page_is_displayed_correctly()).is_true()
