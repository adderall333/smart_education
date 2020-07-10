from django.shortcuts import render

def test_constructor(request):
    return render(request, 'test_constructor/testConstructor.html')
