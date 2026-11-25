# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


browser = webdriver.Chrome()
browser.maximize_window()
site_url = 'https://fix-online.sbis.ru/'
user_login = '0gman'
user_password = 'gelo090'
people_for_message_name = 'Александров Олег'
message_text = 'Привет, Олег!'

try:
    print('Открыть страницу https://fix-online.sbis.ru/')
    browser.get(site_url)
    sleep(2)

    print('Вводим логин')
    login_input = browser.find_element(By.CSS_SELECTOR, '[data-qa="auth-AdaptiveLoginForm__login"] input')
    login_input.send_keys(user_login)
    print('Кликаем Далее')
    browser.find_element(By.CSS_SELECTOR, '[data-qa="auth-AdaptiveLoginForm__checkSignInTypeButton"]').click()
    sleep(2)

    print('Вводим пароль')
    password_input = browser.find_element(By.CSS_SELECTOR, '[data-qa="auth-AdaptiveLoginForm__password"] input')
    password_input.send_keys(user_password)
    print('Нажимаем Войти')
    browser.find_element(By.CSS_SELECTOR, '[data-qa="auth-AdaptiveLoginForm__signInButton"]').click()
    sleep(5)

    print('Кликаем на Контакты в аккардеоне')
    browser.find_element(By.CSS_SELECTOR, 'a.NavigationPanels-Accordion__item[data-qa="Контакты"]').click()
    sleep(1)
    print("В выпадающем окне выбираем Контакты")
    browser.find_element(By.CSS_SELECTOR, 'a.NavigationPanels-SubMenu__item[data-name="contacts"]').click()
    sleep(3)

    print('Кликаем на + Новое сообщение')
    browser.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]').click()
    sleep(3)

    print(f'В строку поиска вводим {people_for_message_name}')
    search = browser.find_element(By.CSS_SELECTOR, 'div[data-qa="controls-Render__field"] input')
    search.send_keys(people_for_message_name)
    sleep(3)

    print(f'Кликаем по строке с {people_for_message_name}')
    result_row = browser.find_element(By.XPATH,f'//*[@data-qa="msg-addressee-selector__plain-list-view"]//div[@data-qa="item"][contains(., "{people_for_message_name}")]')
    result_row.click()
    sleep(3)

    print('Вводим сообщение')
    browser.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]').send_keys(message_text)
    sleep(1)

    print('Отправляем сообщение')
    browser.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]').click()
    sleep(3)

    print('Закрываем диалог')
    browser.find_element(By.CSS_SELECTOR, '[class*="controls-CloseButton__close__wrapper"]').click()
    sleep(3)


    print('Проверяем, что сообщение появилось в реестре')
    message_xpath = f'//div[contains(@class, "msg-dialogs-item__message-text")][contains(., "{message_text}")]'
    message_preview = browser.find_element(By.XPATH, message_xpath)
    assert message_preview.is_displayed(), 'Сообщение не появилось в реестре'
    sleep(3)


    print('Удаляем сообщение')
    message_row = message_preview.find_element(By.XPATH, 'ancestor::div[@data-qa="item"]')
    ActionChains(browser).context_click(message_row).perform()
    sleep(2)
    browser.find_element(By.XPATH, '//div[contains(@class, "controls-Menu__content")][@title="Перенести в удаленные"]').click()
    sleep(2)

    print('Проверяем, что сообщение удалено')
    messages = browser.find_elements(By.XPATH, message_xpath)
    assert len(messages) == 0, 'Сообщение не было удалено'
finally:
    browser.quit()
