# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
browser.maximize_window()
sbis_site = 'https://sbis.ru/'

try:
    print('Открываем https://sbis.ru/')
    browser.get(sbis_site)
    sleep(2)

    print('Переходим в раздел "Контакты"')
    browser.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item [href="/contacts"]').click()
    sleep(2)

    print('Клик по баннеру Тензор')
    browser.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor').click()
    sleep(2)

    print('Переходим на вкладку tensor.ru')
    handles = browser.window_handles
    browser.switch_to.window(handles[1])
    sleep(2)

    print('Проверяем блок "Сила в людях"')
    block = browser.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4')
    assert block.is_displayed(), 'Блок "Сила в людях" не отображается'
    assert 'Сила в людях' in block.text, 'На странице нет блока "Сила в людях"'
    sleep(2)

    print('Переходим по ссылке "Подробнее"')
    link = block.find_element(By.CSS_SELECTOR, 'a[href="/about"]')
    link.click()
    sleep(2)

    print('Проверяем адрес страницы "О компании"')
    assert browser.current_url == 'https://tensor.ru/about', 'Открылась не страница "О компании"'
finally:
    browser.quit()