from app.controllers import post_controller
from app.models.post_model import Post


def post_routes(app):
    @app.get("/")
    def home():
        return "ok"

    @app.post("/post")
    def new_post():

        return post_controller.add_post()

    @app.get("/post")
    def get_all():

        return post_controller.get_all()

    @app.get("/post/<int:id>")
    def get_post_by_id(id: int):
        return post_controller.get_by_id(id)

    @app.patch("/post/<int:id>")
    def update_post(id: int):
        return post_controller.update_post(id)

    @app.delete("/post/<int:id>")
    def delete_post(id: id):
        return post_controller.delete_post(id)
