from playwright.sync_api import sync_playwright
from time import sleep


def login(page):
    # Execute login in page initial
    page.goto('https://www.saucedemo.com')
    sleep(0.5)

    username = page.locator('xpath=//*[@id="user-name"]')
    username.fill('problem_user')
    sleep(0.5)

    password = page.locator('xpath=//*[@id="password"]')
    password.fill('secret_sauce')
    sleep(0.5)

    page.locator('xpath=//*[@id="login-button"]').click()
    sleep(0.5)


def add_item_car(page):
    # Add item to Cart
    add_car = page.locator('xpath=//*[@id="add-to-cart-sauce-labs-backpack"]')
    add_car.click()
    sleep(0.5)


def checkout(page):
    # Go to the checkout page, fill in the details and confirm the purchase!
    shop = page.locator('xpath=//*[@id="shopping_cart_container"]/a')  # Xpath
    shop.click()
    sleep(0.5)

    checkout = page.locator('button#checkout')  # CSS
    checkout.click()
    sleep(0.5)

    first_name = page.locator('input#first-name')  # CSS
    first_name.fill('Lucio')

    last_name = page.locator('id=last-name')  # ID
    last_name.fill('Silva')

    postal_code = page.locator('id=postal-code')  # ID
    postal_code.fill('115858')

    continue_button = page.locator('xpath=//*[@id="continue"]')
    continue_button.click()
    sleep(2)


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login(page)
        add_item_car(page)
        checkout(page)

        erro = page.wait_for_selector('xpath=//*[@id="checkout_info_container"]/div/form/div[1]/div[4]')
        if erro.is_visible():
            print('Infelizmente ocorreu um erro ao tentar concluir a Compra...')

        browser.close()
        sleep(1)
        print('SAINDO DO SITE!!!')


if __name__ == '__main__':
    main()
