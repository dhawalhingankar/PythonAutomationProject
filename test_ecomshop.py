import pytest
import softest
from pages.login_page import LoginPage
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestAndShop(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LoginPage(self.driver)

    def test_shop(self):

        # Login Page
        add_product = self.lp.enter_login_details("standard_user","secret_sauce")

        # Find a Product and add it to the cart
        checkout = add_product.enter_add_product()

        # Click on Add to cart & checkout
        details = checkout.enter_checkout_page()

        # Add name,details & continue
        finish = details.enter_add_personal_details('Jiva', "Shekhar", "Galaxy Apartment")

        # Finish the process
        finish.enter_finish_process()

        # Assertion
        assertion_utils = Utils()
        assertion_utils.compare_texts('element_1', 'element_2')

























