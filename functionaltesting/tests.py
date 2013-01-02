from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ClienteAdminTestSuite(LiveServerTestCase):

    fixtures = ['clientes.json']

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()
    #todo terminar el test
    def test_crear_nuevo_cliente(self):
        self.browser.get(self.live_server_url + '/admin/')
        admin_text = self.browser.find_element_by_id('login-form')
        self.assertIn('Usuario:',admin_text.text)

        username = self.browser.find_element_by_name('username')
        username.send_keys('admin')
        password = self.browser.find_element_by_name('password')
        password.send_keys('123456')
        password.send_keys(Keys.RETURN)
        #Pagina principal del admin donde estan todas las aplicaciones
        clientes_link = self.browser.find_element_by_link_text('Cuentas de Clientes')
        self.assertEquals(clientes_link.text,u'Cuentas de Clientes')
        clientes_link.click()
        #Pagina para modificar clientes
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Escoja Cuenta Cliente a modificar', body.text)
        nuevo_cliente_link = self.browser.find_element_by_partial_link_text('Cuenta Cliente')
        nuevo_cliente_link.click()
        clientes_link = browser.find_element_by_link_text('Cuentas de Clientes')
        
class ClienteTestSuite(LiveServerTestCase):

    fixtures = ['clientes.json']

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_crear_nuevo_cliente_con_campos_requeridos(self):
        self.browser.get(self.live_server_url + '/zonaclientes/registro/')
        admin_text = self.browser.find_element_by_id('ci')
        self.assertIn('Usuario:',admin_text.text)

        username = self.browser.find_element_by_name('password')
        username.send_keys('123456')
        password = self.browser.find_element_by_name('nombres')
        password.send_keys('123456')
        password.send_keys(Keys.RETURN)
        
        #Pagina principal del cliente
        body = self.browser.find_element_by_tag_name('body')
        