from flask import Blueprint, request
from models import db, Task
from flask_jwt_extended import jwt_required, get_jwt_identity

task_bp = Blueprint("tasks", __name__, url_prefix="/api/tasks")


# Get all tasks for current user
@task_bp.route("", methods=["GET"])
@jwt_required()
def get_tasks():
    user_id = int(get_jwt_identity())

    tasks = Task.query.filter_by(user_id=user_id).all()

    return [
        {
            "id": t.id,
            "title": t.title,
            "description": t.description
        } for t in tasks
    ]


# Create task
@task_bp.route("", methods=["POST"])
@jwt_required()
def create_task():
    user_id = int(get_jwt_identity())
    data = request.get_json()

    if not data.get("title"):
        return {"error": "Title is required"}, 400

    new_task = Task(
        title=data.get("title"),
        description=data.get("description"),
        user_id=user_id
    )

    db.session.add(new_task)
    db.session.commit()

    return {"message": "Task created"}, 201


# Update task
@task_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_task(id):
    user_id = int(get_jwt_identity())
    data = request.get_json()

    task = Task.query.get(id)

    if not task:
        return {"error": "Task not found"}, 404

    if task.user_id != user_id:
        return {"error": "Unauthorized"}, 403

    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)

    db.session.commit()

    return {"message": "Task updated"}


# Delete task
@task_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_task(id):
    user_id = int(get_jwt_identity())

    task = Task.query.get(id)

    if not task:
        return {"error": "Task not found"}, 404

    if task.user_id != user_id:
        return {"error": "Unauthorized"}, 403

    db.session.delete(task)
    db.session.commit()

    return {"message": "Task deleted"}