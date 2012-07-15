from django.shortcuts import redirect

"""
If your hasn't entered any email, don't let them go in any pages
started with /accounts/ except those that are specified here
"""
def is_url_allowed(user, path):
    account_prefix = "/accounts/"
    account_allowed_url = (
            "%sset-email/" % account_prefix,
            "%slogout/" % account_prefix,
    )
    if user.is_authenticated():
        if not user.emails.exists() and path.startswith(account_prefix) and path not in account_allowed_url:
            return False

    return True


class EmailRequiredMiddleware(object):

    def process_request(self, request):
        if is_url_allowed(request.user, request.path) is False:
            return redirect('/accounts/set-email/')

        return None
