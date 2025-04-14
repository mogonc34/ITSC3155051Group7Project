# init_db.py

from api.dependencies.database import engine
from api.models import (
    customer, ingredient, menu_item, menu_item_ingredients,
    order, order_item, order_promotion, payment,promotions, rating_review
)

# Call create_all() for all Base metadata
customer.Base.metadata.create_all(engine)
ingredient.Base.metadata.create_all(engine)
menu_item.Base.metadata.create_all(engine)
menu_item_ingredients.Base.metadata.create_all(engine)
order.Base.metadata.create_all(engine)
order_item.Base.metadata.create_all(engine)
order_promotion.Base.metadata.create_all(engine)
payment.Base.metadata.create_all(engine)
promotions.Base.metadata.create_all(engine)
rating_review.Base.metadata.create_all(engine)

print("Tables created successfully!")
