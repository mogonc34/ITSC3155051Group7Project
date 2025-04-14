# from Code Skeleton

from api.models import order_promotion, payment_model
from . import customer, ingredient, menu_item, menu_item_ingredients, 
    order, order_item, order_promotion, payment, payment_model, promotions, rating_review

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    customer.Base.metadata.create_all(engine)
    ingredient.Base.metadata.create_all(engine)
    menu_item.Base.metadata.create_all(engine)
    menu_item_ingredients.Base.metadata.create_all(engine)
    order.Base.metadata.create_all(engine)
    order_promotion.Base.metadata.create_all(engine)
    payment.Base.metadata.create_all(engine)
    payment_model.Base.metadata.create_all(engine)
    promotions.Base.metadata.create_all(engine)
    rating_review.Base.metadata.create_all(engine)
