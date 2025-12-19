from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.schemas.task import TaskCreate, TaskOut
from app.services.tasks import create_task, get_tasks


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/", response_model=TaskOut)
def create_task_endpoint(
    payload: TaskCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return create_task(db, current_user, payload.title)


@router.get("/", response_model=list[TaskOut])
def list_tasks(
    limit: int = 10,
    offset: int = 0,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return get_tasks(db, current_user, limit, offset)