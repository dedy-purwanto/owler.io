from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

class HomeView(TemplateView):

    template_name = "home/home.html"

    def render_to_response(self, context, **response_kwargs):
        if self.request.user.is_authenticated():
            return redirect(reverse("accounts:dashboard"))

        return super(HomeView, self).render_to_response(context, **response_kwargs)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        return context
