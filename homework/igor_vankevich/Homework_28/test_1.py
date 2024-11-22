from playwright.sync_api import Page, Route, expect
import json

new_name = 'яблокофон 16 про'


def test_change_name(page: Page):

    def name_route(route: Route):
        response = route.fetch()
        body = response.json()
        body["body"]["digitalMat"][0]["familyTypes"][0]["productName"] = new_name
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )
    page.route('**/digitalmat', name_route)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.get_by_role('heading', name='iPhone 16 Pro & iPhone 16 Pro Max').click()
    name = page.locator('#rf-digitalmat-overlay-label-0').first
    expect(name).to_have_text(new_name)
