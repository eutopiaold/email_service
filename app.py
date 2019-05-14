from flask import Flask
from flask_graphql import GraphQLView
import flask_cors

import sendmail_schema as sendmail
import config

app = Flask(__name__)
app.debug = True
flask_cors.CORS(app)

app.add_url_rule(
    '/send-mail',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=sendmail.schema,
        graphiql=True, # GraphiQL interface
    )
)

if __name__ == '__main__':
    app.run(
        host=config.flask_host,
        port=config.flask_port
    )
