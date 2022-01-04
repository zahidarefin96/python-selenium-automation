from behave import when, then


@when("Hover over New Arrivals options")
def hover_new_arrivals_link(context):
    context.app.header.hover_new_arrivals_link()


@then("Verify {text} option is visible")
def verify_text(context, text):
    context.app.search_results_page.verify_correct_text(text)
