from framework.config import Config


class Home:
    TITLE = ('xpath', '//h1[contains(text(),"Home")]')
    MODAL_BUTTON = ('xpath', '/html/body/div[3]/div[3]/button')
    REGISTRATION_BUTTON = ('xpath', '//*[@id="register1"]')
    CLIENT_ONBOARDING_BUTTON = ('xpath', '//*[@id="register2"]')
    MARKETING_AGENT_REGISTRATION_BUTTON = ('xpath', '//*[@id="register3"]')


class Tables:
    TITLE = ('xpath', '//h1[contains(text(),"Tables")]')


class Forms:
    TITLE = ('xpath', '//h1[contains(text(),"Forms")]')
    MODAL_BUTTON = ('xpath', '/html/body/div[3]/div[3]/button')
    NAME_FIELD = ('xpath', '//*[@id="myname"]')
    EMAIL_FIELD = ('xpath', '//*[@id="myemail"]')
    PASSWORD_FIELD = ('xpath', '//*[@id="mypassword"]')
    WEBSITE_FIELD = ('xpath', '//*[@id="myurl"]')
    PHONE_FIELD = ('xpath', '//*[@id="mytelephone"]')
    REFERENCE_FIELD = ('xpath', '//*[@id="reference"]')
    QUESTION_RADIO_BUTTON = ('xpath', '//*[@id="questionitem"]')
    COMMENT_RADIO_BUTTON = ('xpath', '//*[@id="commentitem"]')
    COMMENTS_FIELD = ('xpath', '//*[@id="myComments"]')
    SEND_BUTTON = ('xpath', '//*[@id="sendButton"]')
    MODAL_TITLE = ('xpath', '//*[@id="modalTitle"]')
    MODAL_CLOSE_BUTTON = ('xpath', '//*[@id="myModal"]/div/span')


class Registration:
    TITLE = ('xpath', '//*[@id="registration_modal_1"]/div/div/div/div/div/h4/strong')
    FIRST_NAME_FIELD = ('xpath', '//*[@id="_firstname"]')
    LAST_NAME_FIELD = ('xpath', '//*[@id="_lastname"]')
    STREET_ADDRESS_1_FIELD = ('xpath', '//*[@id="address1"]')
    STREET_ADDRESS_2_FIELD = ('xpath', '//*[@id="address2"]')
    CITY_FIELD = ('xpath', '//*[@id="city"]')
    STATE_FIELD = ('xpath', '//*[@id="state"]')
    ZIP_CODE_FIELD = ('xpath', '//*[@id="zipcode"]')
    COUNTRY_FIELD = ('xpath', '//*[@id="reference"]')
    COUNTRY_OPTION = ('xpath', '//*[@id="reference"]/option[2]')
    PHONE_FIELD = ('xpath', '//*[@id="telephone"]')
    EMAIL_FIELD = ('xpath', '//*[@id="email"]')
    COMMENT_FIELD = ('xpath', '//*[@id="myComments"]')
    SEND_BUTTON = ('xpath', '//*[@id="sendButton"]')
    CANCEL_BUTTON = ('xpath', '//*[@id="CancelRegistration"]')
    OUTPUT_TEXT = ('xpath', '//*[@id="newRegistration"]')


class ClientOnboarding:
    PHONE_FIELD = ('xpath', '//*[@id="_telephone"]')
    SLACK_EMAIL_FIELD = ('xpath', '//*[@id="slackemail"]')
    YOUR_EMAIL_FIELD = ('xpath', '//*[@id="youremail"]')
    FACEBOOK_CHECKBOX = ('xpath', '//*[@id="facebook"]')
    INSTAGRAM_CHECKBOX = ('xpath', '//*[@id="instagram"]')
    TWITTER_CHECKBOX = ('xpath', '//*[@id="twitter"]')
    PINTEREST_CHECKBOX = ('xpath', '//*[@id="pinterest"]')
    LINKEDIN_CHECKBOX = ('xpath', '//*[@id="linkedin"]')
    SOCIAL_MEDIA_LOGINS_FIELD = ('xpath', '//*[@id="social_media_logins"]')
    THREE_TIMES_RADIO_BUTTON = ('xpath', '//*[@id="three_times"]')
    FIVE_TIMES_RADIO_BUTTON = ('xpath', '//*[@id="five_times"]')
    SEVEN_TIMES_RADIO_BUTTON = ('xpath', '//*[@id="seven_times"]')
    DONE_RADIO_BUTTON = ('xpath', '//*[@id="done"]')
    NOT_NEEDED_RADIO_BUTTON = ('xpath', '//*[@id="not_needed"]')
    SEND_BUTTON = ('xpath', '//*[@id="sendButton"]')
    CANCEL_BUTTON = ('xpath', '//*[@id="quantityCancel"]')
    OUTPUT_TEXT = ('xpath', '//*[@id="newClientRegistration"]')


class MarketingAgentsRegistration:
    TITLE = ('xpath', '//*[@id="registration_modal_3"]/div/div/div/div/div/h4/strong')
    FIRST_NAME_FIELD = ('xpath', '//*[@id="firstname"]')
    LAST_NAME_FIELD = ('xpath', '//*[@id="lastname"]')
    EMAIL_FIELD = ('xpath', '//*[@id="email"]')
    COMPANY_NAME_FIELD = ('xpath', '//*[@id="companyname"]')
    PHONE_FIELD = ('xpath', '//*[@id="telephone"]')
    DESCRIBE_FIELD = ('xpath', '//*[@id="social_media_logins"]')
    SEND_BUTTON = ('xpath', '//*[@id="sendButton"]')
    CANCEL_BUTTON = ('xpath', '//*[@id="quantityCancel"]')
    OUTPUT_TEXT = ('xpath', '//*[@id="newAgentRegistration"]')

class Page:
    HOME = Config.base_url + 'index.html'
    TABLES = Config.base_url + 'tables.html'
    FORMS = Config.base_url + 'forms.html'
    MODALS = Config.base_url + 'modals.html'
    VARIOUS = Config.base_url + 'various.html'
    CHARTS = Config.base_url + 'charts.html'


class To:
    HOME = ('xpath', '//*[@id="responsive-menu"]/div[1]/ul/li[2]/a')
    TABLES = ('xpath', '//*[@id="responsive-menu"]/div[1]/ul/li[3]/a')
    FORMS = ('xpath', '//*[@id="responsive-menu"]/div[1]/ul/li[4]/a')
    MODALS = ('xpath', '//*[@id="responsive-menu"]/div[1]/ul/li[5]/a')
    VARIOUS = ('xpath', '//*[@id="responsive-menu"]/div[1]/ul/li[6]/a')
    CHARTS = ('xpath', '//*[@id="responsive-menu"]/div[1]/ul/li[7]/a')


class Charts:
    TITLE = ('xpath', '//h1[contains(text(),"Charts")]')
    CHART_TYPE_FIELD = ('xpath', '//*[@id="chartSelect"]')
    SUBMIT_BUTTON = ('xpath', '//*[@id="myButton1"]')
    CHART_TYPE_FIELD2 = ('xpath', '//*[@id="chartSelect2"]')
    SUBMIT_BUTTON2 = ('xpath', '//*[@id="myButton2"]')
    CHART1 = ('xpath', '//*[@id="myChart"]')
    CHART2 = ('xpath', '//*[@id="myChart2"]')


class Various:
    TITLE = ('xpath', '//h1[contains(text(),"Various")]')


class Modals:
    TITLE = ('xpath', '//h1[contains(text(),"Modals")]')
    QUANTITY_BUTTON = ('xpath', '//button[contains(text(),"Quantity")]')
    ALERT_BUTTON = ('xpath', '//button[contains(text(),"Alert")]')
    SECURITY_BUTTON = ('xpath', '//button[contains(text(),"Security")]')
    SETTINGS_BUTTON = ('xpath', '//button[contains(text(),"Settings")]')

    ADD_USER = ('xpath', '//*[@id="addUser"]')
    NAME_FIELD = ('xpath', '//*[@id="name"]')
    USERNAME_FIELD = ('xpath', '//*[@id="username"]')
    EMAIL_ADDRESS_FIELD = ('xpath', '//*[@id="email"]')
    ADDRESS_FIELD = ('xpath', '//*[@id="address"]')
    PHONE_FIELD = ('xpath', '//*[@id="phone"]')
    WEBSITE_FIELD = ('xpath', '//*[@id="website"]')
    COMPANY_FIELD = ('xpath', '//*[@id="company"]')
    SUBMIT_BUTTON = ('xpath', '//*[@id="submitUser"]')




