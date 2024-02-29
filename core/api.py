from ninja import NinjaAPI
from produtos.api import produtos_router

api = NinjaAPI()

api.add_router('/produtos/', produtos_router)
