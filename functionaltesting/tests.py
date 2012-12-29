from django.test import LiveServerTestCase
from selenium import webdriver

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
        password.send_keys('123465')
        
        clientes_links = self.browser.find_elements_by_link_text('Clientes')
        self.assertEquals(len(clientes_links), 2)

        # TODO: Gertrude uses the admin site to create a new Poll
        self.fail('todo: terminar tests')