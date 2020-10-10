from framework.elements import *
from framework.Verify import Verify
from PO.PageObjects import PageObjects
from nose.plugins.attrib import attr
from data.data import ClientRegistration, ClientOnBoarding, Marketing, Users
import time


class SmokeTestSuite001(PageObjects):

    @attr(priority="high")
    @attr(category="regression")
    @attr(suite="001")
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
    @attr(suite="001")
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
    @attr(suite="001")
    def test_003_Should_be_able_to_fill_out_and_send_the_registration_form(self):
        """ TCID003: Should be able to fill out and Send the Registration Form"""
        self.Open(Page.HOME)
        Verify().PageTitle(Home.TITLE, 'Home')

        self.Click(Home.REGISTRATION_BUTTON)
        self.fill_out_registration_form(ClientRegistration.data)
        Verify().TextDisplayed(Registration.OUTPUT_TEXT, ClientRegistration.expected_text)

    @attr(priority="high")
    @attr(category="regression")
    @attr(suite="001")
    def test_004_Should_be_able_to_fill_out_and_send_the_client_onboarding_form(self):
        """ TCID004: Should be able to fill out and Send the Client On Boarding Form"""
        self.Open(Page.HOME)
        Verify().PageTitle(Home.TITLE, 'Home')

        self.Click(Home.CLIENT_ONBOARDING_BUTTON)
        self.fill_out_client_onboarding_form(ClientOnBoarding.data)

        Verify().TextDisplayed(ClientOnboarding.OUTPUT_TEXT, ClientOnBoarding.expected_text)

    @attr(priority="high")
    @attr(category="regression")
    @attr(suite="001")
    def test_005_Should_be_able_to_fill_out_and_send_the_marketing_agent_registration_form(self):
        """ TCID005: Should be able to fill out and send the Marketing Agent Registration Form"""

        self.Open(Page.HOME)
        Verify().PageTitle(Home.TITLE, 'Home')

        self.Click(Home.MARKETING_AGENT_REGISTRATION_BUTTON)
        self.fill_out_marketing_agent_registration_form(Marketing.data)

        Verify().TextDisplayed(MarketingAgentsRegistration.OUTPUT_TEXT, Marketing.expected_text)

    @attr(priority="medium")
    @attr(category="sanity")
    @attr(suite="001")
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
    @attr(suite="001")
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

    @attr(priority="low")
    @attr(category="smoke")
    @attr(suite="001")
    @attr(bb="bb")
    def test_008_Should_be_able_to_add_users(self):
        """ TCID008: Should be able to add users """

        """ Navigate to the Modals Page """
        self.Navigate(To.MODALS)

        """ Click the Add User button """
        self.Click(Modals.ADD_USER)

        """ Fill out the Add User Form"""
        self.fill_out_add_user_form(Users.names)
