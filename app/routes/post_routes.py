from app.controllers import post_controller
from app.models.post_model import Post


def post_routes(app):
    @app.get("/")
    def home():
        return "ok"

    @app.post("/posts")
    def new_post():

        return post_controller.add_post()

    @app.get("/posts")
    def get_all():

        return post_controller.get_all()

    @app.get("/posts/<int:id>")
    def get_post_by_id(id: int):
        return post_controller.get_by_id(id)

    @app.patch("/posts/<int:id>")
    def update_post(id: int):
        return post_controller.update_post(id)

    @app.delete("/posts/<int:id>")
    def delete_post(id: id):
        return post_controller.delete_post(id)
