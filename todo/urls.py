from django.urls import path
from .views import (
    IndexView,
    TagListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    toggle_task_status
)

urlpatterns = [
    path(
        "",
        IndexView.as_view(),
        name="index"
    ),
    path(
        "tags/",
        TagListView.as_view(),
        name="tags-list"),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tags-create"
    ),
    path(
        "tags/update/<int:pk>/",
        TagUpdateView.as_view(),
        name="tags-update"
    ),
    path(
        "tags/delete/<int:pk>/",
        TagDeleteView.as_view(),
        name="tags-delete"
    ),
    path(
        "task/create/",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "task/update/<int:pk>/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "task/delete/<int:pk>/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "tasks/<int:pk>/toggle/",
        toggle_task_status,
        name="toggle-task-status"
    ),
]

app_name = "todo"
