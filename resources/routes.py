from .task import TasksAPI, TaskAPI


def initialize_routes(api):
    api.add_resource(TasksAPI, '/api/v1.0/todo/tasks', methods=['GET'])
    api.add_resource(TaskAPI, '/api/v1.0/todo/task/<int:id>', methods=['GET'])
