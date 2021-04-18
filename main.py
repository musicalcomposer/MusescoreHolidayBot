from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import date
import datetime
import holidays
browser  = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.musescore.com/')
browser.find_element_by_class_name("_3VOC-").click();
ms_name = "MusescoreHolidayBot"
ms_pass = "rtQesj7m2@NiwUZ"
login_username = browser.find_element_by_name("username")
login_username.send_keys(ms_name)
login_pass = browser.find_element_by_name("password")
login_pass.send_keys(ms_pass)
login_username.send_keys(ms_name)
browser.find_element_by_class_name("button js-form-submit js--button-login-page form-submit").click()
browser.find_element_by_class_name("_30GTb _3jhEM _39f0R _3Afie _1KCsZ QJLL8 _1F8Hs _2wqMT").click()
search_bar = browser.find_element_by_name("text")
search_bar.send_keys("randomly screwing around")
browser.find_element_by_class_name("_15Sil").click()
browser.find_element_by_class_name("_39f0R _3Afie _2rQms _1Eaqj _2wqMT").click()
us_holidays = holidays.UnitedStates()
d = datetime.datetime.now()
if d == '12-25-2021' in us_holidays:
  browser.find_element_by_class_name("_39f0R Fa8XQ _2p4Dc _1Eaqj _2wqMT").click()
  title_1_holiday = browser.find_element_by_class_name("_1W1lV")
  body_1_holiday = browser.find_element_by_class_name("public-DraftStyleDefault-block public-DraftStyleDefault-ltr")
  title_1_holiday.send_keys("[s]Merry Christmas[/s]")
  body_1_holiday.send_keys("[b]Actually Happy Christmas [/b][i]cuz i'm british today[/i]")
  browser.find_element_by_class_name("UKzQS _39f0R _3Afie _2p4Dc _1Eaqj _2wqMT").click()
if d == '04-04-2022' in us_holidays:
  browser.find_element_by_class_name("_39f0R Fa8XQ _2p4Dc _1Eaqj _2wqMT").click()
  title_2_holiday = browser.find_element_by_class_name("_1W1lV")
  body_2_holiday = browser.find_element_by_class_name("public-DraftStyleDefault-block public-DraftStyleDefault-ltr")
  title_2_holiday.send_keys("[s]Merry Easter[/s]")
  body_2_holiday.send_keys("[i]or Hoppy Easter?[/i]")
  browser.find_element_by_class_name("UKzQS _39f0R _3Afie _2p4Dc _1Eaqj _2wqMT").click()
if d == '11-25-2021' in us_holidays:
  browser.find_element_by_class_name("_39f0R Fa8XQ _2p4Dc _1Eaqj _2wqMT").click()
  title_3_holiday = browser.find_element_by_class_name("_1W1lV")
  body_3_holiday = browser.find_element_by_class_name("public-DraftStyleDefault-block public-DraftStyleDefault-ltr")
  title_3_holiday.send_keys("[s]Happy Thanksgiving[/s]")
  body_3_holiday.send_keys("[i]i like turkeys [/i][url=https://www.youtube.com/watch?v=iik25wqIuFo]dancing turkey[/url]")
  browser.find_element_by_class_name("UKzQS _39f0R _3Afie _2p4Dc _1Eaqj _2wqMT").click()
if d == '10-31-2021' in us_holidays:
  browser.find_element_by_class_name("_39f0R Fa8XQ _2p4Dc _1Eaqj _2wqMT").click()
  title_4_holiday = browser.find_element_by_class_name("_1W1lV")
  body_4_holiday = browser.find_element_by_class_name("public-DraftStyleDefault-block public-DraftStyleDefault-ltr")
  title_4_holiday.send_keys("[i]I am a ghost...[/i]")
  body_4_holiday.send_keys("happy halloween")
  browser.find_element_by_class_name("UKzQS _39f0R _3Afie _2p4Dc _1Eaqj _2wqMT").click()