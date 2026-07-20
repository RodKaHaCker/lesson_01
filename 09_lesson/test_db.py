import pytest
from db_manager import DBManager


@pytest.fixture
def db():
    db_url = "postgresql://postgres:Korol_stah1@127.0.0.1:5432/mydatabase"
    return DBManager(db_url)


def test_add_student(db):
    student = db.add_student("Иван Петров", "ivan@test.com")
    assert student.id is not None
    assert student.name == "Иван Петров"
    assert student.email == "ivan@test.com"
    assert student.is_active is True
    db.delete_student(student.id, soft=False)


def test_update_student(db):
    student = db.add_student("Петр Сидоров", "petr@test.com")
    original_id = student.id
    updated = db.update_student(original_id, new_name="Петр Иванов")
    assert updated.name == "Петр Иванов"
    db.delete_student(original_id, soft=False)


def test_soft_delete_student(db):
    import time
    unique_email = f"maria_{int(time.time())}@test.com"
    student = db.add_student("Мария Смирнова", unique_email)
    student_id = student.id

    deleted = db.delete_student(student_id, soft=True)
    assert deleted is not None

    student_from_db = db.get_student(student_id)
    assert student_from_db.is_active is False

    db.delete_student(student_id, soft=False)
