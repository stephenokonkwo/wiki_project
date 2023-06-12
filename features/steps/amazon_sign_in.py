from behave import given, when, then


@then('Verify Sign in page opens')
def verify_signin_opens(context):
    context.app.sign_in_page.verify_signin_opens()
