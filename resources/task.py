from flask import Response, jsonify, abort
from data.tasks import tasks
from flask_restful import Resource
from resources.errors import NotFoundError


class TasksAPI(Resource):
    def get(self):
        return jsonify(tasks)


class TaskAPI(Resource):
    def get(self, id):
        task = [task for task in tasks if task['id'] == id]
        if len(task) == 0:
            raise NotFoundError
        return jsonify(task[0])
