from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.task import Task
from app.models.user import User


def create_task(db: Session, user: User, title: str) -> Task:
    task = Task(title=title, owner_id=user.id)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_tasks(
    db: Session,
    user: User,
    limit: int = 10,
    offset: int = 0,
):
    stmt = (
        select(Task)
        .where(Task.owner_id == user.id)
        .limit(limit)
        .offset(offset)
    )
    return db.scalars(stmt).all()