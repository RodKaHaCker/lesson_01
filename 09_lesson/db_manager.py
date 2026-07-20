from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student


class DBManager:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.SessionLocal = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.SessionLocal()

    def add_student(self, name, email):
        session = self.get_session()
        student = Student(name=name, email=email)
        session.add(student)
        session.commit()
        session.refresh(student)
        session.close()
        return student

    def update_student(self, student_id, new_name=None, new_email=None):
        session = self.get_session()
        student = session.query(Student).filter(
            Student.id == student_id
        ).first()
        if student:
            if new_name:
                student.name = new_name
            if new_email:
                student.email = new_email
            session.commit()
            session.refresh(student)
        session.close()
        return student

    def delete_student(self, student_id, soft=True):
        session = self.get_session()
        student = session.query(Student).filter(
            Student.id == student_id
        ).first()
        if student:
            if soft:
                student.is_active = False
                session.commit()
            else:
                session.delete(student)
                session.commit()
        session.close()
        return student

    def get_student(self, student_id):
        session = self.get_session()
        student = session.query(Student).filter(
            Student.id == student_id
        ).first()
        session.close()
        return student
