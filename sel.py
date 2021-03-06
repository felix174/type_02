# -*- coding: utf-8 -*-
# lellons_1_06
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import Group
from group import Group_contact

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class type_04(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    # add contact
    def test_second(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.add_new_contact(wd, Group_contact(firstname="Dmytro", middlename="Victorovuch", lastname="Rudenko",
                                               nickname="felix174", title="web", company="promo", address="chabanu",
                                               home="012345678", mobile="7777777777", work="555555555", fax="154541455",
                                               form_01="8", byear="1989", form_02="10", form_03="12", form_04="3",
                                               ayear="2013", address2="none_2", notes="my secount work"))
        self.return_to_contact_page(wd)
        self.logout(wd)

    # add group
    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_group_page(wd)
        self.create_group(wd, Group(name="second2", header="hello", footer="bye"))
        self.return_to_group_page(wd)
        self.logout(wd)

    # add group with number
    def test_add_number_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_group_page(wd)
        self.create_group(wd,  Group(name="121212", header="232323", footer="343434"))
        self.return_to_group_page(wd)
        self.logout(wd)

    def return_to_contact_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def add_new_contact(self, wd, group):
        # add new contact
        wd.find_element_by_link_text("add new").click()
        # fill contact firm
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(group.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(group.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(group.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(group.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(group.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(group.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(group.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(group.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(group.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(group.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(group.fax)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%s]" % group.form_01).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%s]" % group.form_01).click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%s]" % group.form_02).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%s]" % group.form_02).click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(group.byear)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[%s]" % group.form_03).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[%s]" % group.form_03).click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[%s]" % group.form_04).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[%s]" % group.form_04).click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(group.ayear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(group.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(group.notes)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_group_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def create_group(self, wd, group):
        # init group page
        wd.find_element_by_name("new").click()
        # fill group firm
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def open_group_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()