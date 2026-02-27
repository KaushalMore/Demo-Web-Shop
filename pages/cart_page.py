from pages.base_page import BasePage

class CartPage(BasePage):
    CART_LINK = ("css selector", "li#topcartlink span.cart-label")
    COUNTRY_DROPDOWN = ("id", "CountryId")
    STATE_DROPDOWN = ("id", "StateProvinceId")
    ESTIMATE_SHIPPING_BUTTON = ("name", "estimateshipping")
    TERMS_CHECKBOX = ("id", "termsofservice")
    CHECKOUT_BUTTON = ("id", "checkout")

    def open_cart(self):
        self.click(self.CART_LINK)

    def select_country(self, country):
        self.select(self.COUNTRY_DROPDOWN, country)

    def select_state(self, state):
        self.select(self.STATE_DROPDOWN, state)

    def estimate_shipping(self):
        self.click(self.ESTIMATE_SHIPPING_BUTTON)

    def accept_terms(self):
        self.click(self.TERMS_CHECKBOX)

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)