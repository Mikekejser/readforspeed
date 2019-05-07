from django.shortcuts import render, redirect, get_object_or_404
from .models import Text, UserText
from .forms import UserTextForm
import random
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Choose text size:
# def main (request, text_size=500):
# 	if text_size == 500:
# 		pass
# field Text: Charfield choices small medium large.
def main(request, textid=0):
	user = request.user
	if textid == 0:
		my_ids = Text.objects.all().values_list('id', flat=True)
		random_id = random.choice(my_ids)
		text = get_object_or_404(Text, id=random_id)
	else:
		text = UserText.objects.get(id=textid)
	
	context = {'text': text, 'user': user}

	return render(request, 'core/main.html', context)


@login_required
def add_text(request):
	user = request.user
	if len(UserText.objects.filter(user=user)) == 50:
		messages.success(request, 'You can have up to 50 texts on your account. Delete one if you want to add another.')
		return redirect('my_texts')

	if request.method == 'POST':
		form = UserTextForm(request.POST)
		if form.is_valid():
			form.save()
			title = form.cleaned_data['title']
			messages.success(request, f'{title} has been added.')
			return redirect('my_texts')

	else:
		data = {'user': user}
		form = UserTextForm(initial=data)

	return render(request, 'core/add_text.html', {'form': form})


@login_required
def my_texts(request):
	user = request.user
	texts = UserText.objects.filter(user=user)
	return render(request, 'core/my_texts.html', {'texts': texts})


@login_required
def edit_text(request, textid):
	text = UserText.objects.get(pk=textid)
	if request.method == 'POST':
		form = UserTextForm(request.POST)
		if form.is_valid():
			text_title = form.cleaned_data['title']
			text_text = form.cleaned_data['text']
			text.title = text_title
			text.text = text_text
			text.save()
			messages.success(request, f'{text_title} has been edited.')
			return redirect('my_texts')
	else:
		user = request.user
		data = {'user': user, 'title': text.title, 'text': text.text}
		form = UserTextForm(initial=data)
	return render(request, 'core/edit_text.html', {'form': form})


@login_required
def delete_text(request, textid):
	text = UserText.objects.get(pk=textid)
	messages.success(request, f'{text.title} has been deleted.')
	text.delete()
	return redirect('my_texts')
