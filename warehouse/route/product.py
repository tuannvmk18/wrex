from flask_restx import Namespace, Resource, fields
from warehouse import api
from warehouse.service import product as product_service

product_ns = Namespace('product', description='product api')


@product_ns.route('/')
class ProductList(Resource):

    @product_ns.doc('list_products')
    def get(self):
        return product_service.get_all()

    def post(self):
        payload = api.payload
        return product_service.create(payload)


@product_ns.route("/<int:product_id>")
class ProductWithP(Resource):

    def get(self, product_id):
        return product_service.get_by_id(product_id)

    def delete(self, product_id):
        return product_service.delete(product_id)

    def patch(self, product_id):
        payload = api.payload
        return product_service.update(product_id, payload)
