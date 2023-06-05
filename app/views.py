from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='login')
def home_page(request):
    qust = Question.objects.all()
    qustion = Question.objects.all().values_list("id", flat=True)
    answ = Question.objects.all().values_list('ans',flat=True)
    
    if request.method == 'POST':
        ans=request.POST
        
        ansnew = dict(ans)
        del ansnew['csrfmiddlewaretoken']
        result = {key: value[0] for key, value in ansnew.items()}
        print(result)
        
        qustion_no = qustion
        qustion_ans = answ
        anskey = dict(zip(qustion_no, qustion_ans))
        print(anskey)
        
        n = len(anskey)
        print(n)
        
        mark = 0
        for i in range(1,n+1):
            if str(i) in result.keys():
                if anskey[i] == result[str(i)]:
                    mark+=1
                else:
                    mark-=0.25
        
            
        print(mark)
        
        Answer.objects.create(
            mark = mark,
            fk_user = request.user
        )
        
        return redirect('result')
    
    context = {
        'qust' : qust
    }
    return render(request,"test_page/home_page.html",context)


@login_required(login_url='login')
def add_question(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        option1 =  request.POST.get('option1')
        option2 =  request.POST.get('option2')
        option3 =  request.POST.get('option3')
        option4 =  request.POST.get('option4')
        ans = request.POST.get('option')
        
        Question.objects.create(
            question = question,
            option1 = option1,
            option2 = option2,
            option3 = option3,
            option4 = option4,
            ans = ans
            
        )
        return redirect('home_page')
        
    return render(request,'test_page/add_question.html')


@login_required(login_url='login')
def result(request):
    user = request.user
    ans = Answer.objects.filter(fk_user = user).last()
    
    context ={
        'ans' : ans
    }
    return render(request,'test_page/result.html',context)


@login_required(login_url='login')
def user_permissions(request):
    
    user = User.objects.all()
    print(user)
    context = {
        'user' : user
    }
    
    return render(request,'test_page/permission.html',context)


@login_required(login_url='login')
def approve_sts(request,id):
    user = User.objects.get(id=id)
    user.is_active = not user.is_active
    user.save()
    return redirect('user_permissions')

