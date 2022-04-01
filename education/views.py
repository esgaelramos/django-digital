from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Q

# -------------------(DETAIL/LIST VIEWS) ------------------- #

def home(request):
    search = request.GET.get('search')

    searchList = False

    topicList = Topic.objects.all()
    lessonList = Lesson.objects.all()
	
    if search:
        searchList = Lesson.objects.filter(
            Q(title__icontains = search) |
            Q(subtitle__icontains = search) |
            Q(description__icontains = search) |
			Q(topic__title__icontains = search)
        ).distinct()


    context = {
        'searchList':searchList, 'topicList':topicList,
		'lessonList':lessonList,
    }

    return render(request, 'index.html', context)



# -------------------(CREATE VIEWS) ------------------- #
def createLesson(request):
	action = 'create'
	form = LessonForm()
	if request.method == 'POST':
		form = LessonForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context =  {
        'action':action, 'form':form
    }

	return render(request, 'forms/lesson_form.html', context)

def createTopic(request):
	action = 'create'
	form = TopicForm()
	if request.method == 'POST':
		form = TopicForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context =  {
        'action':action, 'form':form
    }

	return render(request, 'forms/topic_form.html', context)

def createOrganization(request):
	action = 'create'
	form = OrganizationForm()
	if request.method == 'POST':
		form = OrganizationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context =  {
        'action':action, 'form':form
    }

	return render(request, 'forms/organization_form.html', context)

def createHuman(request):
	action = 'create'
	form = HumanForm()
	if request.method == 'POST':
		form = HumanForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context =  {
        'action':action, 'form':form
    }

	return render(request, 'forms/human_form.html', context)



# -------------------(UPDATE VIEWS) ------------------- #

def updateLesson(request, pk):
	action = 'update'
	lesson = Lesson.objects.get(title=pk)
	form = LessonForm(instance=lesson)

	if request.method == 'POST':
		form = LessonForm(request.POST, instance=lesson)
		if form.is_valid():
			form.save()
			return redirect('/')

	context =  {
		'action':action, 'form':form
	}
	
	return render(request, 'forms/lesson_form.html', context)

def updateTopic(request, pk):
	action = 'update'
	topic = Topic.objects.get(title=pk)
	form = TopicForm(instance=topic)

	if request.method == 'POST':
		form = TopicForm(request.POST, instance=topic)
		if form.is_valid():
			form.save()
			return redirect('/')

	context =  {
		'action':action, 'form':form
	}
	
	return render(request, 'forms/topic_form.html', context)

def updateOrganization(request, pk):
	action = 'update'
	organization = Organization.objects.get(name=pk)
	form = OrganizationForm(instance=organization)

	if request.method == 'POST':
		form = OrganizationForm(request.POST, instance=organization)
		if form.is_valid():
			form.save()
			return redirect('/')

	context =  {
		'action':action, 'form':form
	}
	
	return render(request, 'forms/organization_form.html', context)

def updateHuman(request, pk):
	action = 'update'
	human = Human.objects.get(id=pk)
	form = HumanForm(instance=human)

	if request.method == 'POST':
		form = HumanForm(request.POST, instance=human)
		if form.is_valid():
			form.save()
			return redirect('/')

	context =  {
		'action':action, 'form':form
	}
	
	return render(request, 'forms/human_form.html', context)


# -------------------(DELETE VIEWS) ------------------- #

def deleteLesson(request, pk):
    lesson = Lesson.objects.get(title=pk)
    lesson.delete()
    
    return redirect('/')

def deleteTopic(request, pk):
    topic = Topic.objects.get(title=pk)
    topic.delete()
    
    return redirect('/')

def deleteOrganization(request, pk):
    organization = Organization.objects.get(name=pk)
    organization.delete()
    
    return redirect('/')

def deleteHuman(request, pk):
    human = Human.objects.get(id=pk)
    human.delete()
    
    return redirect('/')