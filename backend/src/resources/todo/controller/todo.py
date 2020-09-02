from flask import Blueprint, request

TODO_API = Blueprint('todos', __name__)


@TODO_API.route('/todo', methods=['GET'])
def get_all_todo():
    """
    Creates a todo list.
    :return: None
    """
    return {
        'data': 'hello'
    }
