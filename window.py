from tkinter import *
from PIL import Image
from tkinter import ttk
from tkinter import messagebox
import customtkinter
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait as ww
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import os
from threading import Thread



# LINKEDIN AUTOMATION
################################################################################################
def Selenium():
    chrome_options = Options()
    arguments = ['--lang=en-US', '--window-size=1300,1000',
                '--incognito']

    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1

    })

    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)
    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,
        ]
    )
    


    driver.get('https://www.linkedin.com.br/')
    sleep(2)

    ######################################################################################


    # LOGIN
    ######################################################################################
    email_page = wait.until(expected_conditions.visibility_of_element_located((
        By.XPATH, '//input[@autocomplete="username"]')))
    email_page.send_keys(entry_email.get())
    sleep(2)
    password_page = wait.until(expected_conditions.visibility_of_element_located((
        By.XPATH, '//input[@autocomplete="current-password"]')))   
    password_page.send_keys(password_entry.get())   
    sleep(2)  
    button = wait.until(expected_conditions.visibility_of_element_located((
        By.XPATH, '//button[@class="sign-in-form__submit-button"]')))
    button.click()
    output_area.insert(customtkinter.INSERT, 'Login successful!')
    sleep(5)
    ######################################################################################


    # Search button
    ######################################################################################
    search_button = ww(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//input[@class="search-global-typeahead__input"]')))    
    search_button.send_keys(role_entry.get())
    sleep(1)
    search_button.send_keys(Keys.ENTER)
    output_area.insert(customtkinter.INSERT, '\n\nInserting role to search...')
    sleep(4)
    ######################################################################################



    # People button
    ######################################################################################
    people_button = ww(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//li[@class='search-reusables__primary-filter']/button[text()='Pessoas']")))    
    people_button.click()
    output_area.insert(customtkinter.INSERT, '\n\nSearching people...')
    sleep(3)
    ######################################################################################
    
    while True:
            # Conections locations
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(5)

        driver.execute_script('window.scrollTo(0, document.body.scrollTop);')
        sleep(5)

        buttons_connect = ww(driver, 10).until(expected_conditions.visibility_of_all_elements_located((By.XPATH, "//*[text()='Conectar']"))) 
        sleep(3)

        for button in buttons_connect:        
            try:
                button.click()
                add_note = ww(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[@aria-label='Adicionar nota']")))
                add_note.click()
                sleep(2)
                textarea = ww(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//textarea[@id='custom-message']")))
                textarea.send_keys(message.get("1.0","end-1c"))
                sleep(2)
                send_request = ww(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[@aria-label='Enviar agora']")))
                send_request.click()
                output_area.insert(customtkinter.INSERT, '\n\nRequest sent!')
                
                sleep(10)
            except:
                button_fechar = driver.find_element(By. XPATH, "//div[@class='artdeco-modal artdeco-modal--layer-default send-invite']/button")   
                sleep(2)
                button_fechar.click() 
            
        try:
            next = ww(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//li-icon[@type='chevron-right-icon']")))
            next.click()
            output_area.insert(customtkinter.INSERT, '\n\nWe are in the next page now!')
            sleep(5)
            
        except:
            output_area.insert(customtkinter.INSERT, '\n\nWe reached the last page!')
            break    
        

    input('')
    driver.close()
################################################################################################

def open_selenium():
    thread_function = Thread(target=Selenium, daemon=True)
    thread_function.start()
        


# TKINTER MAIN WINDOW
################################################################################################
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

window = customtkinter.CTk()
window.title("Linkedin automation")
window.geometry('600x900+600+70')
window.resizable(0, 0)
################################################################################################


# FRAMES, LABELS, TEXTS AND ENTRIES
################################################################################################
frame_top = customtkinter.CTkFrame(master=window)
frame_top.pack(fill='both', expand=True)

label_top = customtkinter.CTkLabel(master=frame_top, text='Welcome to Linkedin Automation', font=('Microsoft YaHei UI',12), bg_color='#1f538d')
label_top.pack(fill='both')

# FRAME EMAIL E SENHA
frame_login_text = customtkinter.CTkFrame(master=window, width=500, height=130)
frame_login_text.place(x=50, y=50)

email_value = StringVar()
email_text = customtkinter.CTkLabel(master=frame_login_text, text='E-mail', font=('Microsoft YaHei UI',12,'bold'))
email_text.place(x=15,y=10)

entry_email = customtkinter.CTkEntry(master=frame_login_text, textvariable=email_value,width=230, font=('Microsoft YaHei UI',12), border_width=1)
entry_email.place(x=15, y=35)

password_value = StringVar()
password_text = customtkinter.CTkLabel(master=frame_login_text, text='Password', font=('Microsoft YaHei UI',12,'bold'))
password_text.place(x=271,y=10)
password_entry = customtkinter.CTkEntry(master=frame_login_text, show='*', textvariable= password_value, width=230, font=('Microsoft YaHei UI',12), border_width=1)
password_entry.place(x=270, y=35)

role_text_value = StringVar()
role_text = customtkinter.CTkLabel(master=frame_login_text, text='Role to search', font=('Microsoft YaHei UI',12,'bold'))
role_text.place(x=15,y=75)
role_entry = customtkinter.CTkEntry(master=frame_login_text, textvariable=role_text_value, width=230, font=('Microsoft YaHei UI',12), border_width=1)
role_entry.place(x=15, y=100)

mensagem_output = customtkinter.CTkFrame(master=window, width=480, height=175)
mensagem_output.place(x=50, y=200)

message_value = StringVar()
message_text = customtkinter.CTkLabel(master=mensagem_output, text='Message for invitation ', font=('Microsoft YaHei UI',12,'bold'))
message_text.place(x=15,y=10)
message = customtkinter.CTkTextbox(master=mensagem_output,  width=400, border_width=1, height=100, font=('Microsoft YaHei UI',12))
message.place(x=15, y=35)

frame_output = customtkinter.CTkFrame(master=window, width=500, height=470)
frame_output.place(x=50, y=382)

events_label = customtkinter.CTkLabel(master=mensagem_output, text='Events', font=('Microsoft YaHei UI',12,'bold'))
events_label.place(x=15,y=155)

output_area = customtkinter.CTkTextbox(master=frame_output, width=400, height=420, border_width=1)
output_area.place(x=14)

button_start = customtkinter.CTkButton(master=window, text='Start', cursor='hand2', command= open_selenium)
button_start.place(x=62, y=830)
################################################################################################


window.mainloop()
################################################################################################      







#Olá, me chamo Alexsandro Passos, sou desenvolvedor Python, estou em busca de novas conexões e vi seu perfil e achei interessante, acredito que posso agregar em algo. Obrigado e bom dia!
