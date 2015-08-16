__author__ = 'dave'
from django.conf.urls import url, include
from mezzanine.core.views import direct_to_template
from .views import ajax, coming_soon

urlpatterns = [

    url("^about-us\.html$", direct_to_template, {"template": "hes/about-us.html"}, name="about-us"),
    url("^signup\.html$", direct_to_template, {"template": "hes/signup.html"}, name="signup"),
    url("^forgot-password\.html$", direct_to_template, {"template": "hes/forgot-password.html"}, name="forgot-password"),
    url("^account-home\.html$", direct_to_template, {"template": "users/account-home.html"}, name="account-home"),
    url("^account-close\.html$", direct_to_template, {"template": "users/account-close.html"}, name="account-close"),
    url("^account-saved-search\.html$", direct_to_template, {"template": "users/account-saved-search.html"}, name="account-saved-search"),
    url("^account-pending-approval-ads\.html$", direct_to_template, {"template": "users/account-pending-approval-ads.html"}, name="account-pending-approval-ads"),
    url("^account-favourite-ads\.html$", direct_to_template, {"template": "users/account-favourite-ads.html"}, name="account-favorite-ads"),
    url("^item-detail$", direct_to_template, {"template": "hes/ads-details.html"}, name="item-detail"),
    url("^account-archived-ads\.html$", direct_to_template, {"template": "users/account-archived-ads.html"}, name="account-archived-ads"),
    url("^blank-page\.html$", direct_to_template, {"template": "hes/blank-page.html"}, name="blank-page"),
    url("^posting-success\.html$", direct_to_template, {"template": "hes/posting-success.html"}, name="posting-success"),
    url("^category\.html$", direct_to_template, {"template": "hes/category.html"}, name="category"),
    url("^ajax/(?P<ajax_code>[1-3])\.html$", ajax, name="ajax"),
    url("^sub-category-sub-location\.html$", direct_to_template, {"template": "hes/sub-category-sub-location.html"}, name="sub-category"),
    url("^coming-soon$", coming_soon, name="coming-soon"),
    url("^contact$", direct_to_template, {"template": "hes/contact.html"}, name="contact"),

    #User management
    url(r'^users/', include("hes.users.urls", namespace="hes_users")),
]