from django.shortcuts import render, Http404

# Create your views here.


def index(request):
    return Http404('Requested resource does not exists.')


def about(request):
    return render(request, 'sitelinks/about.html', context=None)


def career(request):
    return render(request, 'sitelinks/career.html', context=None)


def privacypolicy(request):
    return render(request, 'sitelinks/privacypolicy.html', context=None)


def termsofuse(request):
    return render(request, 'sitelinks/termsofuse.html', context=None)


def sitemap(request):
    return render(request, 'sitelinks/sitemap.html', context=None)
