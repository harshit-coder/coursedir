from django.contrib import messages
from django.core.mail import send_mail
from django.http.response import JsonResponse
from django.shortcuts import render, redirect

from .models import *


# Create your views here.
def home(request):
    li2 = []
    cat = quiz.objects.values_list('name', flat=True)
    for i in list(quiz.objects.values_list('name', flat=True)):

        count = 0
        ca = quiz.objects.get(name=i)
        co = course.objects.filter(category=ca.id)
        for j in co:
            count = count + 1
        li2.append(count)
    ba = course.objects.filter(level="BEGINNERS")[:6]
    ia = course.objects.filter(level="INTERMEDIATE")[:6]
    aa = course.objects.filter(level="ADVANCE")[:6]
    li1 = zip(cat, li2)

    qu = quiz.objects.all()
    return render(request, "Homepage.html", context={'li1': li1, 'ba': ba, 'ia': ia, 'aa': aa, 'qu': qu})


def quiz_view(request, qid):
    qu1 = quiz.objects.get(id=qid)
    return render(request, "quiz.html", context={'qu1': qu1})


def quiz_data_view(request, pk):
    qu = quiz.objects.get(id=pk)
    quest = []
    print('views' + str(qu.get_questions()))
    for q in qu.get_questions():
        ans = []
        for a in q.get_answers():
            ans.append(a.answer_text)
        quest.append({str(q.question_text): ans})

    return JsonResponse({
        'data': quest,
        'time': qu.time,
    })


def quiz_data_save(request, pk):
    if request.is_ajax():
        data = request.POST
        score = 0
        data1 = dict(data.lists())
        quest = []
        data1.pop('csrfmiddlewaretoken')

        qui = quiz.objects.get(id=pk)
        print('views1' + str(data1.keys()))
        for k in data1.keys():
            k=k.replace("#012"," ")
            question = Question.objects.get(question_text=str(k))
            quest.append(question)

        for j in quest:
            ans = request.POST.get(j.question_text)
            if ans != "" :
                quest_ans = Answer.objects.filter(question_text1=j)
                for h in quest_ans:
                    if h.answer_text == ans:
                        if h.correct_answer:
                            score = score + 1

        if qui.basic_min_score <= score <= qui.basic_max_score:
            co = course.objects.filter(level='BEGINNERS')
            return JsonResponse({'score': score})
            #return render(request, 'result.html', context={'score': score, 'co': co})
        elif qui.medium_min_score <= score <= qui.medium_max_score:
            co = course.objects.filter(level='INTERMEDIATE')
            return JsonResponse({'score': score})
            #return render(request, 'result.html', context={'score': score, 'co': co})
        else:
            co = course.objects.filter(level='ADVANCE')
            return JsonResponse({'score': score})
            #return render(request, 'result.html', context={'score': score, 'co': co})


def morecourse(request):
    ba = course.objects.filter(level="BEGINNERS")
    ia = course.objects.filter(level="INTERMEDIATE")
    aa = course.objects.filter(level="ADVANCE")
    return render(request, "courses.html", context={'ba': ba, 'ia': ia, 'aa': aa})


def calc(request, pok, score):
    qui = quiz.objects.get(id=pok)
    print(qui)
    if qui.basic_min_score <= int(score) <= qui.basic_max_score:
        co = course.objects.filter(level='BEGINNERS', category__name=qui)
        print(co)
        # return JsonResponse({'score': score})
        return render(request, 'result.html', context={'score': score, 'co': co})
    elif qui.medium_min_score <= int(score) <= qui.medium_max_score:
        co = course.objects.filter(level='INTERMEDIATE', category__name=qui)
        print(co)
        # return JsonResponse({'score': score})
        return render(request, 'result.html', context={'score': score, 'co': co})
    else:
        co = course.objects.filter(level='ADVANCE', category__name=qui)
        print(co)
        # return JsonResponse({'score': score})
        return render(request, 'result.html', context={'score': score, 'co': co})


def cont(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        mess = request.POST['mess']
        send_mail('', 'Name :' + name + '\nMessage: ' + mess, email, ['kmukund094@gmail.com'],
                  fail_silently=False)
        messages.success(request, 'Sent')
        return render(request, "contact.html")
    else:
        return render(request, "contact.html")
