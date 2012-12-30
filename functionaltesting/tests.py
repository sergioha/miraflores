from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ClienteTestSuite(LiveServerTestCase):

    fixtures = ['clientes.json']

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_crear_nuevo_cliente(self):
        self.browser.get(self.live_server_url + '/admin/')
        admin_text = self.browser.find_element_by_id('login-form')
        self.assertIn('Usuario:',admin_text.text)

        username = self.browser.find_element_by_name('username')
        username.send_keys('admin')
        password = self.browser.find_element_by_name('password')
        password.send_keys('123456')
        password.send_keys(Keys.RETURN)

        clientes_link = self.browser.find_element_by_link_text('Clientes')
        self.assertEquals(clientes_link.text,u'Clientes')
        clientes_link.send_keys(Keys.SPACE)
        clientes_link.click()
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('0 Clientes', body.text)
        nuevo_cliente_link = self.browser.find_element_by_link_text('Agregar Cliente')
        nuevo_cliente_link.click()
        # TODO: Gertrude uses the admin site to create a new Poll
        self.fail('todo: terminar tests')
