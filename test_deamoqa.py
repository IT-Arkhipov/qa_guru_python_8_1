from selene.support.shared import browser
from selene import be, have

browser.open("https://demoqa.com/text-box")

browser.element("#userName").type("User")
browser.element("#userEmail").type("user@test.ru")
browser.element("#submit").press_enter()
browser.element("#name").should(have.text("User"))
browser.element("#email").should(have.text("user@test.ru"))




