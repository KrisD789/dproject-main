from .views import add_todo, cancel_edit, delete_todo, edit_todo, edit_todo_form, index, toggle_todo, update, update2
from django.contrib import admin
from django.urls import path

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', index, name='index'),
    path('update/',update, name='update-content'),
    path('update2',update2, name='update-content2'),
    path('add/',add_todo, name='add_todo'),
    path('delete/<int:todo_id>',delete_todo, name='delete_todo'),
    path('toggle/<int:todo_id>',toggle_todo, name='toggle_todo'),
    path('edit/<int:todo_id>',edit_todo, name='edit_todo'),
    path('edit_form/<int:todo_id>',edit_todo_form, name='edit_todo_form'),
    path('cancel/<int:todo_id>',cancel_edit, name='cancel_edit'),
]
