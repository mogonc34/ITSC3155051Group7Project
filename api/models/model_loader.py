# from Code Skeleton

from . import customer, ingredient, menu_item, menu_item_ingredients, order, order_item, order_promotion, payment, promotions, rating_review

from ..dependencies.database import engine


def index():
    order_item.Base.metadata.create_all(engine)
    customer.Base.metadata.create_all(engine)
    ingredient.Base.metadata.create_all(engine)
    menu_item.Base.metadata.create_all(engine)
    menu_item_ingredients.Base.metadata.create_all(engine)
    order.Base.metadata.create_all(engine)
    order_promotion.Base.metadata.create_all(engine)
    payment.Base.metadata.create_all(engine)
    promotions.Base.metadata.create_all(engine)
    rating_review.Base.metadata.create_all(engine)
