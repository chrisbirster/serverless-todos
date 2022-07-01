import json
import os

from todos.todo_model import TodoModel


def todo_list(event, context):
    # fetch all todos from the database

    results = TodoModel.scan()

    # create a response
    return {'statusCode': 200,
            'body': json.dumps({'items': [dict(result) for result in results]})}
#     return {'statusCode': 200, 'body': json.dumps("ENV: %s" % os.environ)}
