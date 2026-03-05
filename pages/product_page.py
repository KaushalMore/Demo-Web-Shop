from pages.base_page import BasePage


class ProductPage(BasePage):
    PRODUCT_NAME = ("css selector", "h1[itemprop='name']")
    PRODUCT_DESCRIPTION = ("css selector", "div[class='short-description']")
    PRODUCT_PRICE = ("css selector", "div.product-price>span")
    REVIEW_LINK = ("css selector", "div.product-review-links>a:nth-of-type(1)")
    QUANTITY_FIELD = ("id", "addtocart_13_EnteredQuantity")
    ADD_TO_CART_BUTTON = ("id", "add-to-cart-button-13")

    def get_product_name(self):
        return self.get_text(self.PRODUCT_NAME)

    def get_product_description(self):
        return self.get_text(self.PRODUCT_DESCRIPTION)

    def get_product_price(self):
        return self.get_text(self.PRODUCT_PRICE)

    def get_review_text(self):
        return self.get_text(self.REVIEW_LINK)

    def set_quantity(self, qty):
        self.send_keys(self.QUANTITY_FIELD, str(qty))

    def click_add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)
