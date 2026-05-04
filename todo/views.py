from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from todo.forms import TaskForm
from todo.models import Task, Tag


class IndexView(generic.ListView):
    model = Task
    template_name = "todo/index.html"
    context_object_name = "tasks"


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"
    context_object_name = "tags"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = "todo/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("todo:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo/task_confirm_delete.html"
    success_url = reverse_lazy("todo:index")


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ["name"]
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tags-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ["name"]
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tags-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo/tag_confirm_delete.html"
    success_url = reverse_lazy("todo:tags-list")


class ToggleTaskStatusView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        task.done_or_not = not task.done_or_not
        task.save()
        return redirect("todo:index")
