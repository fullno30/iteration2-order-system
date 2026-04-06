from domain.product import Product
from domain.order_item import OrderItem
from domain.order import Order

from repository.product_repo import ProductRepository
from repository.order_repo import OrderRepository


def main():
    # Create repositories
    product_repo = ProductRepository()
    order_repo = OrderRepository()

    # Create products (same as your Iteration 1, just with IDs added)
    mug = Product(1, "Mug", 12.50)
    scarf = Product(2, "Scarf", 25.00)

    # Store products in the repository
    product_repo.add(mug)
    product_repo.add(scarf)

    # Create an order (Iteration 1 had no ID, so we add one for repo storage)
    order = Order(order_id=100)

    # Add items to the order using products retrieved from the repository
    order.add_item(OrderItem(product_repo.get(1), 2))  # 2 mugs
    order.add_item(OrderItem(product_repo.get(2), 1))  # 1 scarf

    # Save the order in the repository
    order_repo.save(order)

    # Print subtotals (same output style as your Iteration 1)
    for item in order.items:
        print(f"Item: {item.product.name}x{item.quantity} = ${item.subtotal():.2f}")

    # Print total
    print(f"Total = ${order.total():.2f}")


if __name__ == "__main__":
    main()
