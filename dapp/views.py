from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import Todo
def index(request):
	return render(request, 'index.html')

def update(request):
	return HttpResponse('<div>Hello HTMX</div>')

def update2(request):
	if request.method == 'POST':
		data = request.POST.get('data')
		return render(request, 'partial_content.html', {'data':data})
	
def add_todo(request):
	if request.method == 'POST':
		title = request.POST.get('title')
		new_todo = Todo.objects.create(title=title)
		return render(request, 'todo_item.html', {'todo' : new_todo})
	
def delete_todo(request,todo_id):
	todo = get_object_or_404(Todo, id=todo_id)
	todo.delete()
	return HttpResponse(status=200)

def toggle_todo(request, todo_id):
	todo = get_object_or_404(Todo, id=todo_id)
	todo.completed = not todo.completed
	todo.save()
	return render(request, 'todo_item.html', {'todo':todo})

def edit_todo(request, todo_id):
	if request.method == 'POST':
		todo = get_object_or_404(Todo, id=todo_id)
		todo.title = request.POST.get('title')
		todo.save()
		return render(request, 'todo_item.html', {'todo' : todo})
	
def edit_todo_form(request, todo_id):
	todo = get_object_or_404(Todo, id=todo_id)
	title = todo.title
	return render(request, 'todo_item_form.html', {'todo' : todo, 'title' : title})

def cancel_edit(request, todo_id):
	todo = get_object_or_404(Todo, id=todo_id)
	return render