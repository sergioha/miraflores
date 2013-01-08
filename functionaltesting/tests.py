# -*- coding: iso-8859-1 -*-
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class BasicTestSuite(LiveServerTestCase):
    
    browser = None
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def _ingresar_como_admin(self):
        self.browser.get(self.live_server_url + '/admin/')
        admin_text = self.browser.find_element_by_id('login-form')
        #self.assertIn('Usuario:',admin_text.text)
        username = self.browser.find_element_by_name('username')
        username.send_keys('admin')
        password = self.browser.find_element_by_name('password')
        password.send_keys('123456')
        password.send_keys(Keys.RETURN)
        
    def _ingresar_como_cliente(self):
        self.browser.get(self.live_server_url + '/zonacliente/')
        #admin_text = self.browser.find_element_by_id('login-form')
        #self.assertIn('Usuario:',admin_text.text)
        #username = self.browser.find_element_by_name('username')
        #username.send_keys('admin')
        #password = self.browser.find_element_by_name('password')
        #password.send_keys('123456')
        #password.send_keys(Keys.RETURN)

class ClienteAdminTestSuite(BasicTestSuite):

    fixtures = ['clientes.json']
    
    def test_crear_nuevo_cliente(self):
        self._ingresar_como_admin()
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
        
class ClienteTestSuite(BasicTestSuite):

    fixtures = ['clientes.json']

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

class CrearServicio(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "http://127.0.0.1:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_crear_servicio(self):
        driver = self.driver
        driver.get(self.live_server_url + '/admin/')
        self.assertEqual("Iniciar sesi\on | Sitio de administraci\on de Django".decode('utf-8'), driver.title)
        # Warning: verifyTextPresent may require manual changes
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, r"^[\s\S]*Administración de Django[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        self.assertEqual(u"Sitio administrativo | Sitio de administración de Django", driver.title)
        # Warning: verifyTextPresent may require manual changes
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, r"^[\s\S]*Sitio administrativo[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        # Warning: verifyTextPresent may require manual changes
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, r"^[\s\S]*Servicios[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("(//a[contains(text(),'Servicios')])[2]").click()
        self.assertEqual(u"Escoja servicio a modificar | Sitio de administración de Django", driver.title)
        # Warning: verifyTextPresent may require manual changes
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, r"^[\s\S]*Escoja servicio a modificar[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        # Warning: verifyTextPresent may require manual changes
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, "^[\\s\\S]*\n\n    Añadir servicio [\\s\\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text(u"Añadir servicio").click()
        self.assertEqual(u"Añadir servicio | Sitio de administración de Django", driver.title)
        # Warning: verifyTextPresent may require manual changes
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, r"^[\s\S]*Añadir servicio[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        Select(driver.find_element_by_id("id_tipo_servicio")).select_by_visible_text("test")
        driver.find_element_by_id("id_nombre").clear()
        driver.find_element_by_id("id_nombre").send_keys("estoneado")
        driver.find_element_by_id("id_descripcion").clear()
        driver.find_element_by_id("id_descripcion").send_keys("estoneado de jeans")
        driver.find_element_by_id("id_precio_bs").clear()
        driver.find_element_by_id("id_precio_bs").send_keys("1")
        driver.find_element_by_name("_save").click()
        self.assertEqual(u"Escoja servicio a modificar | Sitio de administración de Django", driver.title)
        # Warning: verifyTextPresent may require manual changes
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, r"^[\s\S]*	estoneado[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("estoneado").click()
        self.assertEqual(u"Modificar servicio | Sitio de administración de Django", driver.title)
        # Warning: verifyTextPresent may require manual changes
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, r"^[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert.text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
        