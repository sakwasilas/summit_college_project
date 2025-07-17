from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    role = Column(Enum('student', 'lecturer', 'admin'), nullable=False)

    student_profile = relationship("StudentProfile", back_populates="user", uselist=False)
    lecturer_profile = relationship("LecturerProfile", back_populates="user", uselist=False)

# -----------------------------
class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)

    subjects = relationship("Subject", back_populates="course")

# -----------------------------
class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'))

    course = relationship("Course", back_populates="subjects")

# -----------------------------
class StudentProfile(Base):
    __tablename__ = 'student_profiles'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    full_name = Column(String(100))
    course = Column(String(100))
    module = Column(String(50))
    admission_number = Column(String(50))

    user = relationship("User", back_populates="student_profile")

# -----------------------------
class LecturerProfile(Base):
    __tablename__ = 'lecturer_profiles'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    full_name = Column(String(100))
    phone = Column(String(20))
    department = Column(String(100))
    subjects = Column(String(200))  # Can store comma-separated subject names

    user = relationship("User", back_populates="lecturer_profile")