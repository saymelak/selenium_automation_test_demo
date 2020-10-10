from framework.elements import *
from framework.Verify import Verify
from PO.PageObjects import PageObjects
from nose.plugins.attrib import attr
import time


class SmokeTestSuite002(PageObjects):

    @attr(priority="high")
    @attr(category="regression")
    @attr(suite="002")
    def test_001_Should_be_able_to_navigate_through_all_pages_using_url(self):
        """ TCID001: Should be able to navigate through all pages using url"""
        self.Open(Page.HOME)
        Verify().PageTitle(Home.TITLE, 'Home')

        self.Open(Page.TABLES)
        Verify().PageTitle(Tables.TITLE, 'Tables')

        self.Open(Page.FORMS)
        Verify().PageTitle(Forms.TITLE, 'Forms')

        self.Open(Page.MODALS)
        Verify().PageTitle(Modals.TITLE, 'Modals')

        self.Open(Page.VARIOUS)
        Verify().PageTitle(Various.TITLE, 'Various components')

        self.Open(Page.CHARTS)
        Verify().PageTitle(Charts.TITLE, 'Charts')

    @attr(priority="high")
    @attr(category="regression")
    @attr(suite="002")
    def test_002_Should_be_able_to_navigate_through_all_pages_using_nav_bar(self):
        """ TCID002: Should be able to navigate through all pages using nav bar"""
        self.Navigate(To.HOME)
        Verify().PageTitle(Home.TITLE, 'Home')

        self.Navigate(To.TABLES)
        Verify().PageTitle(Tables.TITLE, 'Tables')

        self.Navigate(To.FORMS)
        Verify().PageTitle(Forms.TITLE, 'Forms')

        self.Navigate(To.MODALS)
        Verify().PageTitle(Modals.TITLE, 'Modals')

        self.Navigate(To.VARIOUS)
        Verify().PageTitle(Various.TITLE, 'Various components')

        self.Navigate(To.CHARTS)
        Verify().PageTitle(Charts.TITLE, 'Charts')

    @attr(priority="high")
    @attr(category="regression")
    @attr(suite="002")
    def test_003_Should_be_able_to_fill_out_and_send_the_registration_form(self):
        """ TCID003: Should be able to fill out and Send the Registration Form"""
        self.Open(Page.HOME)
        Verify().PageTitle(Home.TITLE, 'Home')

        self.Click(Home.REGISTRATION_BUTTON)
        self.FilloutFilled(Registration.FIRST_NAME_FIELD, 'Albert')
        self.FilloutFilled(Registration.LAST_NAME_FIELD, 'Smith')
        self.FilloutFilled(Registration.STREET_ADDRESS_1_FIELD, '700 Fortt St')
        self.FilloutFilled(Registration.STREET_ADDRESS_2_FIELD, 'Suite 300')
        self.FilloutFilled(Registration.CITY_FIELD, 'Victoria')
        self.FilloutFilled(Registration.STATE_FIELD, 'BC')
        self.FilloutFilled(Registration.ZIP_CODE_FIELD, 'V8X 1X1')
        self.Click(Registration.COUNTRY_OPTION)
        self.FilloutFilled(Registration.PHONE_FIELD, '250-123-4567')
        self.FilloutFilled(Registration.EMAIL_FIELD, 'albert.smith@email.com')
        self.FilloutFilled(Registration.COMMENT_FIELD, 'Hi there!')
        self.Click(Registration.SEND_BUTTON)

        Verify().TextDisplayed(Registration.OUTPUT_TEXT, 'Albert, Smith')

    @attr(priority="high")
    @attr(category="regression")
    @attr(suite="002")
    def test_004_Should_be_able_to_fill_out_and_send_the_client_onboarding_form(self):
        """ TCID004: Should be able to fill out and Send the Client Onboarding Form"""
        self.Open(Page.HOME)
        Verify().PageTitle(Home.TITLE, 'Home')

        self.Click(Home.CLIENT_ONBOARDING_BUTTON)
        self.FilloutFilled(ClientOnboarding.PHONE_FIELD, '250-222-3434')
        self.FilloutFilled(ClientOnboarding.SLACK_EMAIL_FIELD, 'slack@email.com')
        self.FilloutFilled(ClientOnboarding.YOUR_EMAIL_FIELD, 'youremail@email.com')
        self.Click(ClientOnboarding.FACEBOOK_CHECKBOX)
        self.Click(ClientOnboarding.INSTAGRAM_CHECKBOX)
        self.Click(ClientOnboarding.TWITTER_CHECKBOX)
        self.Click(ClientOnboarding.PINTEREST_CHECKBOX)
        self.Click(ClientOnboarding.LINKEDIN_CHECKBOX)
        self.FilloutFilled(ClientOnboarding.SOCIAL_MEDIA_LOGINS_FIELD, 'facebook@email.com, instagram@email.com, twitter@email.com')
        self.Click(ClientOnboarding.FIVE_TIMES_RADIO_BUTTON)
        self.Click(ClientOnboarding.NOT_NEEDED_RADIO_BUTTON)
        self.Click(ClientOnboarding.SEND_BUTTON)

        Verify().TextDisplayed(ClientOnboarding.OUTPUT_TEXT, 'youremail@email.com')

    @attr(priority="high")
    @attr(category="regression")
    @attr(suite="002")
    def test_005_Should_be_able_to_fill_out_and_send_the_marketing_agent_registration_form(self):
        """ TCID005: Should be able to fill out and send the Marketing Agent Registration Form"""
        self.Open(Page.HOME)
        Verify().PageTitle(Home.TITLE, 'Home')

        self.Click(Home.MARKETING_AGENT_REGISTRATION_BUTTON)
        self.FilloutFilled(MarketingAgentsRegistration.FIRST_NAME_FIELD, 'Rita')
        self.FilloutFilled(MarketingAgentsRegistration.LAST_NAME_FIELD, 'Baker')
        self.FilloutFilled(MarketingAgentsRegistration.EMAIL_FIELD, 'albert.smith@email.com')
        self.FilloutFilled(MarketingAgentsRegistration.COMPANY_NAME_FIELD, 'R B Ltd ')
        self.FilloutFilled(MarketingAgentsRegistration.PHONE_FIELD, '250-123-4567')
        self.FilloutFilled(MarketingAgentsRegistration.DESCRIBE_FIELD, 'All products :)')
        self.Click(MarketingAgentsRegistration.SEND_BUTTON)

        Verify().TextDisplayed(MarketingAgentsRegistration.OUTPUT_TEXT, 'Rita, Baker')

    @attr(priority="medium")
    @attr(category="sanity")
    @attr(suite="002")
    def test_006_Should_be_able_to_add_contact(self):
        """ TCID006: Should be able to add contact """
        """ Navigate to the Forms page"""
        self.Navigate(To.FORMS)

        """ Fill out the Contact Form and click Submit"""
        self.fill_out_contact_form()

        Verify().TextDisplayed(Forms.MODAL_TITLE, 'You have entered the following..')

        self.Click(Forms.MODAL_CLOSE_BUTTON)

    @attr(priority="low")
    @attr(category="smoke")
    @attr(suite="002")
    def test_007_Should_be_able_to_display_charts(self):
        """ TCID007: Should be able to display Charts """

        """ Navigate to the Charts Page """
        self.Navigate(To.CHARTS)

        """ Choose Line from the dropdown list """
        self.Select(Charts.CHART_TYPE_FIELD, 'Line')

        """ Click Submit """
        self.Click(Charts.SUBMIT_BUTTON)

        """ Verify that the Chart is displayed """
        Verify().CanvasSize(Charts.CHART1)

        """ Choose Line from the dropdown list """
        self.Select(Charts.CHART_TYPE_FIELD, 'Bar')

        """ Click Submit """
        self.Click(Charts.SUBMIT_BUTTON)

        """ Verify that the Chart is displayed """
        Verify().CanvasSize(Charts.CHART1)

        """ Choose Horizontal Bar from the dropdown list """
        self.Select(Charts.CHART_TYPE_FIELD, 'Horizontal Bar')

        """ Click Submit """
        self.Click(Charts.SUBMIT_BUTTON)

        """ Verify that the Chart is displayed """
        Verify().CanvasSize(Charts.CHART1)

        """ Choose Doughnut from the dropdown list """
        self.Select(Charts.CHART_TYPE_FIELD2, 'Doughnut')

        """ Click Submit """
        self.Click(Charts.SUBMIT_BUTTON2)

        """ Verify that the Chart is displayed """
        Verify().CanvasSize(Charts.CHART1)

        """ Choose Pie from the dropdown list """
        self.Select(Charts.CHART_TYPE_FIELD2, 'Pie')

        """ Click Submit """
        self.Click(Charts.SUBMIT_BUTTON2)

        """ Verify that the Chart is displayed """
        Verify().CanvasSize(Charts.CHART1)

