__author__ = 'dima'

class Group:
    # create parameters
    def __init__(self, name, header, footer):
        self.name = name
        self.header = header
        self.footer = footer

class Group_contact:
    # create parameters for contact
    def __init__(self, firstname, middlename, lastname, nickname, title, company, address, home, mobile, work, fax,
                 form_01, byear, form_02, form_03, form_04, ayear, address2, notes):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.form_01 = form_01
        self.byear = byear
        self.form_02 = form_02
        self.form_03 = form_03
        self.form_04 = form_04
        self.ayear = ayear
        self.address2 = address2
        self.notes = notes