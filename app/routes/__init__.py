from app.routes.post_routes import post_routes


def init_app(app):
    post_routes(app)
