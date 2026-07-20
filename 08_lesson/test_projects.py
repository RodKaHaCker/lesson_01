import pytest
from project_api import ProjectAPI


@pytest.fixture
def api():
    return ProjectAPI()


@pytest.fixture
def new_project(api):
    resp = api.create_project("Тестовый проект")
    assert resp.status_code == 201
    project_id = resp.json()["id"]
    yield project_id


# ===== POST /projects =====

def test_create_project_positive(api):
    resp = api.create_project("Мой новый проект")
    assert resp.status_code == 201
    assert "id" in resp.json()


def test_create_project_negative_no_title(api):
    resp = api.create_project("")
    assert resp.status_code == 400
    assert "error" in resp.json()


# ===== PUT /projects/{id} =====

def test_update_project_positive(api, new_project):
    resp = api.update_project(new_project, "Обновлённый проект")
    assert resp.status_code == 200
    # Yougile может не возвращать title, поэтому проверяем наличие id
    assert "id" in resp.json()


def test_update_project_negative_not_found(api):
    fake_id = "00000000-0000-0000-0000-000000000000"
    resp = api.update_project(fake_id, "Новый заголовок")
    assert resp.status_code == 404
    assert "error" in resp.json()


# ===== GET /projects/{id} =====

def test_get_project_positive(api, new_project):
    resp = api.get_project(new_project)
    assert resp.status_code == 200
    assert resp.json()["id"] == new_project


def test_get_project_negative_not_found(api):
    fake_id = "00000000-0000-0000-0000-000000000000"
    resp = api.get_project(fake_id)
    assert resp.status_code == 404
    assert "error" in resp.json()
