
from framework.base_case import BaseCase


class Verify:

    def TextDisplayed(self, locator, txt):
        """ Verify the specified txt is displayed """
        element = BaseCase().wait_for_element_visibility(locator)
        output_text = element.text
        assert txt == output_text

    # def TextNotDisplayed(self, locator, txt):
    #     """ Verify the specified txt is not displayed """
    #     element = BaseCase().wait_until_element_clickable(locator)
    #     output_text = element.text
    #     assert txt != output_text
    #
    # def ElementExists(self, locator):
    #     """ Verify the specified element is displayed """
    #     element = BaseCase().wait_for_element_visibility(locator)
    #     count = driver.find_elements_by_xpath(locator[1])
    #     assert len(count) == 1
    #
    # def ElementsExist(self, locator):
    #     """ Verify the specified elements are displayed """
    #     count = driver.find_elements_by_xpath(locator[1])
    #     assert len(count) > 0
    #
    def PageTitle(self, locator, title):
        """ Verify the title of the page """
        element = BaseCase().wait_for_element_visibility(locator)
        current_title = element.text
        assert current_title == title

    def CanvasSize(self, locator):
        # delay = 3  # seconds
        # try:
        #     WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, xpath)))
        # except TimeoutError:
        #     print("Loading took too much time!")
        element = BaseCase().wait_for_element_visibility(locator)
        w = element.get_attribute("width")
        h = element.get_attribute("height")

        assert int(w) > 0
        assert int(h) > 0
