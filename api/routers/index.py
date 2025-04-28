from . import (customers, ingredient, menu_item, menu_item_ingredients, orders,
    order_item, order_promotion, payment, promotions, rating_review)

def load_routes(app):
    app.include_router(customers.router)
    app.include_router(ingredient.router)
    app.include_router(menu_item.router)
    app.include_router(menu_item_ingredients.router)
    app.include_router(orders.router)
    app.include_router(order_item.router)
    app.include_router(order_promotion.router)
    app.include_router(payment.router)
    app.include_router(promotions.router)
    app.include_router(rating_review.router)
