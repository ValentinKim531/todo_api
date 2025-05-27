import pytest
from tasks.models import Task


@pytest.mark.django_db
def test_create_task(auth_client):
    resp = auth_client.post("/tasks/", {"title": "test task"}, format="json")
    assert resp.status_code == 201
    assert Task.objects.filter(title="test task").exists()


@pytest.mark.django_db
def test_update_task(auth_client):
    task = auth_client.post(
        "/tasks/", {"title": "initial"}, format="json"
    ).data
    task_id = task["id"]
    resp = auth_client.patch(
        f"/tasks/{task_id}/", {"completed": True}, format="json"
    )
    assert resp.status_code == 200
    assert resp.data["completed"] is True


@pytest.mark.django_db
def test_delete_task(auth_client):
    task = auth_client.post(
        "/tasks/", {"title": "to delete"}, format="json"
    ).data
    task_id = task["id"]
    resp = auth_client.delete(f"/tasks/{task_id}/")
    assert resp.status_code == 204
    assert not Task.objects.filter(id=task_id).exists()
