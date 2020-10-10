from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import sys
from framework.config import Config
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from framework.elements import *
from framework.base_case import BaseCase
import time
import random


class PageObjects(BaseCase):

    def fill_out_registration_form(self, data):
        self.FilloutFilled(Registration.FIRST_NAME_FIELD, data["firstname"])
        self.FilloutFilled(Registration.LAST_NAME_FIELD, data["lastname"])
        self.FilloutFilled(Registration.STREET_ADDRESS_1_FIELD, data["street_address_1"])
        self.FilloutFilled(Registration.STREET_ADDRESS_2_FIELD, data["street_address_2"])
        self.FilloutFilled(Registration.CITY_FIELD, data["city"])
        self.FilloutFilled(Registration.STATE_FIELD, data["state"])
        self.FilloutFilled(Registration.ZIP_CODE_FIELD, data["zip_code"])
        self.Click(Registration.COUNTRY_OPTION)
        self.FilloutFilled(Registration.PHONE_FIELD, data["phone"])
        self.FilloutFilled(Registration.EMAIL_FIELD, data["email"])
        self.FilloutFilled(Registration.COMMENT_FIELD, data["comment"])
        time.sleep(2)
        self.Click(Registration.SEND_BUTTON)

    def fill_out_client_onboarding_form(self, data):
        self.FilloutFilled(ClientOnboarding.PHONE_FIELD, data["phone"])
        self.FilloutFilled(ClientOnboarding.SLACK_EMAIL_FIELD, data["slack_email"])
        self.FilloutFilled(ClientOnboarding.YOUR_EMAIL_FIELD, data["your_email"])
        self.Click(ClientOnboarding.FACEBOOK_CHECKBOX)
        self.Click(ClientOnboarding.INSTAGRAM_CHECKBOX)
        self.Click(ClientOnboarding.TWITTER_CHECKBOX)
        self.Click(ClientOnboarding.PINTEREST_CHECKBOX)
        self.Click(ClientOnboarding.LINKEDIN_CHECKBOX)
        self.FilloutFilled(ClientOnboarding.SOCIAL_MEDIA_LOGINS_FIELD, data["social_media_logins"])
        self.Click(ClientOnboarding.FIVE_TIMES_RADIO_BUTTON)
        self.Click(ClientOnboarding.NOT_NEEDED_RADIO_BUTTON)
        time.sleep(2)
        self.Click(ClientOnboarding.SEND_BUTTON)

    def fill_out_marketing_agent_registration_form(self, data):
        self.FilloutFilled(MarketingAgentsRegistration.FIRST_NAME_FIELD, data["firstname"])
        self.FilloutFilled(MarketingAgentsRegistration.LAST_NAME_FIELD, data["lastname"])
        self.FilloutFilled(MarketingAgentsRegistration.EMAIL_FIELD, data["email"])
        self.FilloutFilled(MarketingAgentsRegistration.COMPANY_NAME_FIELD, data["company"])
        self.FilloutFilled(MarketingAgentsRegistration.PHONE_FIELD, data["phone"])
        self.FilloutFilled(MarketingAgentsRegistration.DESCRIBE_FIELD, data["describe"])
        time.sleep(2)
        self.Click(MarketingAgentsRegistration.SEND_BUTTON)

    def fill_out_contact_form(self):
        self.FilloutFilled(Forms.EMAIL_FIELD, 'ronny.reznick@email.com')
        self.FilloutFilled(Forms.PASSWORD_FIELD, 'password123')
        self.FilloutFilled(Forms.WEBSITE_FIELD, 'http://www.xyz.com')
        self.FilloutFilled(Forms.PHONE_FIELD, '000-000-0000')
        self.Select(Forms.REFERENCE_FIELD, 'Facebook')
        self.Click(Forms.QUESTION_RADIO_BUTTON)
        self.FilloutFilled(Forms.COMMENTS_FIELD, 'ABC Comment 1, 2, 3, ...')
        self.FilloutFilled(Forms.NAME_FIELD, 'Ronny, Reznick')
        time.sleep(2)
        self.Click(Forms.SEND_BUTTON)

    def fill_out_add_user_form(self, data):

        # self.FilloutFilled(Modals.NAME_FIELD, data[0])
        # self.FilloutFilled(Modals.USERNAME_FIELD, data[0].lower())
        # self.FilloutFilled(Modals.EMAIL_ADDRESS_FIELD, data[0].lower()+'@email.com')
        # self.FilloutFilled(Modals.ADDRESS_FIELD, str(random.randint(50, 300)) + ' ' + data[0] + ' Street')
        # self.FilloutFilled(Modals.PHONE_FIELD, '(' + str(random.randint(100, 999)) + ')' + ' ' + str(random.randint(100, 999)) + '-' + str(random.randint(1000, 9999)))
        # self.FilloutFilled(Modals.WEBSITE_FIELD, 'http://www.'+data[0].lower()+'.com')
        # self.FilloutFilled(Modals.COMPANY_FIELD, data[0].upper()+' Inc.')
        # time.sleep(2)
        # self.Click(Modals.SUBMIT_BUTTON)

        name = self.get_name(data)

        self.FilloutFilled(Modals.NAME_FIELD, name)
        self.FilloutFilled(Modals.USERNAME_FIELD, name.lower())
        self.FilloutFilled(Modals.EMAIL_ADDRESS_FIELD, name.lower() + '@email.com')
        self.FilloutFilled(Modals.ADDRESS_FIELD, str(random.randint(50, 300)) + ' ' + name + ' Street')
        self.FilloutFilled(Modals.PHONE_FIELD,
                           '(' + str(random.randint(100, 999)) + ')' + ' ' + str(random.randint(100, 999)) + '-' + str(
                               random.randint(1000, 9999)))
        self.FilloutFilled(Modals.WEBSITE_FIELD, 'http://www.' + name.lower() + '.com')
        self.FilloutFilled(Modals.COMPANY_FIELD, name.upper() + ' Inc.')
        time.sleep(2)
        self.Click(Modals.SUBMIT_BUTTON)

    def get_name(self, data):

        source = self.get_page_source()
        source = source.split()
        for item in data:
            if item not in source:
                return item
