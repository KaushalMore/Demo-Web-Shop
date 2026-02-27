from pages.base_page import BasePage


class CheckoutPage(BasePage):
    BILLING_CONTINUE = ("css selector", "div#billing-buttons-container > input[title='Continue']")
    SHIPPING_CONTINUE = ("css selector", "div#shipping-buttons-container > input")
    SHIPPING_METHOD_CONTINUE = ("css selector", "div#shipping-method-buttons-container > input")
    PAYMENT_METHOD_CONTINUE = ("css selector", "div#payment-method-buttons-container > input")
    PAYMENT_INFO_CONTINUE = ("css selector", "div#payment-info-buttons-container > input")
    ORDER_REVIEW = ("css selector", ".order-review-data")
    CONFIRM_ORDER = ("css selector", "div#confirm-order-buttons-container > input")
    ORDER_DETAILS = ("css selector", ".title strong")
    ORDER_LINK = ("partial link text", "Click here for order details.")
    LOGOUT_LINK = ("css selector", "a[href='/logout']")
    LOGIN_LINK = ("css selector", "a.ico-login")

    def complete_checkout(self):
        self.click(self.BILLING_CONTINUE)
        self.click(self.SHIPPING_CONTINUE)
        self.click(self.SHIPPING_METHOD_CONTINUE)
        self.click(self.PAYMENT_METHOD_CONTINUE)
        self.click(self.PAYMENT_INFO_CONTINUE)

    def get_order_review(self):
        return self.get_text(self.ORDER_REVIEW)

    def confirm_order(self):
        self.click(self.CONFIRM_ORDER)

    def get_order_details(self):
        return self.get_text(self.ORDER_DETAILS)

    def open_order_link(self):
        self.click(self.ORDER_LINK)

    def click_logout(self):
        self.click(self.LOGOUT_LINK)

    def get_confirm_logout(self):
        self.get_text(self.LOGIN_LINK)
