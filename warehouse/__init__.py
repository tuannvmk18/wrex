import os

from dotenv import load_dotenv
from flask import Flask
from sqlmodel import create_engine, SQLModel
from flask_restx import Api

load_dotenv()

postgresql_url = f"postgresql://{os.environ.get('DB_USERNAME')}:{os.environ.get('DB_PASSWORD')}@" \
                 f"{os.environ.get('DB_HOST')}:{os.environ.get('DB_PORT')}/" \
                 f"{os.environ.get('DB_NAME')}"

engine = create_engine(postgresql_url, echo=True)

api = Api()


def create_app() -> Flask:
    app = Flask(__name__)
    api.init_app(app)

    from warehouse.route import product_ns
    api.add_namespace(product_ns)

    SQLModel.metadata.create_all(engine)
    return app
