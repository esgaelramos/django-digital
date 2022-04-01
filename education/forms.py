from django.forms import ModelForm

from .models import Human, Organization, Subject, Topic, Lesson

class HumanForm(ModelForm):
	class Meta:
		model = Human
		fields = '__all__'

class OrganizationForm(ModelForm):
	class Meta:
		model = Organization
		fields = '__all__'

class SubjectForm(ModelForm):
	class Meta:
		model = Subject
		fields = '__all__'

class TopicForm(ModelForm):
	class Meta:
		model = Topic
		fields = '__all__'

class LessonForm(ModelForm):
	class Meta:
		model = Lesson
		fields = '__all__'
