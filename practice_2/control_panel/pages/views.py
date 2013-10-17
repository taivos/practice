# Create your views here.

def home(request):
        import datetime
        from django.shortcuts import render
        context = { }
        context['ts'] = datetime.datetime.now()
        return render(request, 'home.html', context)

#function for lab_2.1
#def listing(request, temp):
#    import os
#    if temp == "":
#        dirs =  os.listdir("/var/log")
#    else:
#        dirs =  os.listdir("/var/log/"+str(temp))
#    context = {"dir_content": dirs}
#    return render(request, 'listing.html',context)

#function for lab_2.2
#def listing(request, temp):
#        import os
#        from django.shortcuts import render
#        context = {'dir_content': os.listdir('/var/log' + '/' + str(temp))}
#        context['dir'] = []
#        context['fils'] = []
#        for t in context['dir_content']:
#            if os.path.isdir(os.path.join('/var/log' + '/' + str(temp), t)):
#                context['dir'].append(t)
#            else:
#                context['fils'].append(t)
#        return render(request, 'listing.html', context)

from datetime import datetime

#function for lab_2.3
def listing(request, temp):
    import os
    import time
    from django.shortcuts import render
    context = {'dir_content': os.listdir('/var/log' + '/' + str(temp))}
    context['myTable'] = []
    for t in context['dir_content']:
        myStr = []
        mySize = os.path.getsize(os.path.join('/var/log' + '/' + str(temp), t))
        myTemp = os.stat(os.path.join('/var/log' + '/' + str(temp), t))
        myTime = time.localtime(myTemp.st_mtime)
        myStr.append(t)
        myStr.append(mySize)
        myStr.append(str(myTime[2])+':'+str(myTime[1])+':'+ str(myTime[0]))
        context['myTable'].append(myStr)
    return render(request, 'listing.html', context)