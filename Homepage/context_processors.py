from .models import Banner,Product,BusinessInfo,FrontendSetting,\
    OrderDetails,Feature,FAQ,BillingDetails,FeaturesSection,SiteSettings
from django.contrib.auth.models import User
from django.db.models import Count, Sum



def banner(request):
    return {
        'banner': Banner.objects.first(),
    }

def product(request):
    return {
        'product': Product.objects.first(),
    }


def businessinfo(request):
    return {
        'businessinfo': BusinessInfo.objects.first(),
    }


def frontend_setting(request):
    return {
        'frontend_setting': FrontendSetting.objects.first(),
    }

def feature_section(request):
    return {
        'feature_section': FeaturesSection.objects.first(),
    }

def site_settings(request):
    return {
        'site_settings': SiteSettings.objects.first(),
    }



def last_orders(request):
    total_admin = User.objects.filter(is_staff=True).count()
    total_orders = OrderDetails.objects.count()
    total_feature = Feature.objects.count()
    total_faq = FAQ.objects.count()
    latest_orders = OrderDetails.objects.select_related("billing_details").order_by("-date")[:10]

    return {

        'total_admin': total_admin,
        'total_orders':total_orders,
        'total_feature':total_feature,
        'total_faq': total_faq,
        'latest_orders':latest_orders,

    }