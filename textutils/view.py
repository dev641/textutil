
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def Analyze(request):
    #get the text
    djtext=request.POST.get('text','default')
    print(djtext)
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')

    if removepunc == "on":
        #Analyze the text
        punctuations='''!@#$&(){}[]:;"'\<>,/?^~`_-.'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Remove Punctuations','analyzed_text':analyzed}
    
        djtext=analyzed
    if fullcaps=="on":
        analyzed=''
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'UpperCase','analyzed_text':analyzed}
        djtext=analyzed

    if newlineremover=='on':
          analyzed=''
          for char in djtext:
              if char != '\n' and char !='\r':
                 analyzed=analyzed+char
          params={'purpose':'New line Remover','analyzed_text':analyzed}

          djtext=analyzed

    if extraspaceremover=='on':
          analyzed=''
          for index,char in enumerate(djtext):
              if not(djtext[index]==' '  and djtext[index+1]==' '):
                 analyzed=analyzed+char
          params={'purpose':'New line Remover','analyzed_text':analyzed}

          djtext=analyzed

    if charcount=='on':
        count=0
        punctuations='''!@#$&(){}[]:;"'\<>,/?^~`_-.'''
        for char in djtext:
            if char not in punctuations and char != '\n' and char!=' ':
                count=count+1;
        analyzed=analyzed+'\nCharacter is :'+str(count)
        params={'purpose':'Char Count','analyzed_text':analyzed}
        djtext=analyzed

    return render(request,'Analyze.html',params)
