from django.shortcuts import render
from .forms import encorder
SECURE = (('a', '!'), ('b', '@'),('c', '#'), ('d', '%'), ('e', '^'),('f', '&'),('g', '*'),('h', '('),('i', ')'),('j', '_'),('k', '-'),('l', '+'),('m', '='),('n', '~'),('o', '`'),('p', ';'),('q', ':'),('r', '"'),('s', '<'),('t', '>'),('u', ','),('v', '.'),('w', '?'),('x', '/'),('y', '|'),('z', '{'))

def home(request):
    return render(request,'home.html')



def encrypt(request):
    if request.method == "POST":
        form =  encorder(request.POST)
        if form.is_valid():
            message = form.cleaned_data["text"]
            for a,b in SECURE:
              message  = message .replace(a, b)
              form = encorder()
            return render(request, 'encrypt.html',{'text':message,'fm':form})
    else:
        form = encorder()
    return render(request, 'encrypt.html', {'fm':form})


def decrypt(request):
    if request.method == "POST":
        form =  encorder(request.POST)
        if form.is_valid():
            message = form.cleaned_data["text"]
            for a,b in SECURE:
              message  = message .replace(b, a)
              form = encorder()
            return render(request, 'encrypt.html',{'text':message,'fm':form})
    else:
        form = encorder()
    return render(request, 'decrypt.html', {'fm':form})


