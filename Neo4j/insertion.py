from py2neo import Graph, Node, Relationship, NodeMatcher, RelationshipMatcher
import csv


if __name__ == "__main__":

    g = Graph(host='localhost', auth=("neo4j", "streams"))

    tx = g.begin()
    with open('../store_dataset/users.csv', 'r') as user_file:
        user_data = csv.DictReader(user_file)
        for user in user_data:
            user = Node(
                "User", id=user['user_id'], name=user['name'],
                age=int(float(user['age'])), gender=user['gender'],
                email=user['email'], username=user['username']
            )
            tx.create(user)
        g.commit(tx)

    tx = g.begin()
    with open('../store_dataset/product.csv', 'r') as product_file:
        products = csv.DictReader(product_file)
        for product in products:
            product_node = Node(
                "Product",
                id=product['id'],
                product_title_fa=product['product_title_fa'],
                product_title_en=product['product_title_en'],
                url_code=product['url_code'],
                product_attributes=product['product_attributes'],
            )
            tx.create(product_node)
        g.commit(tx)

    tx = g.begin()
    with open('../store_dataset/product.csv', 'r') as product_file:
        products = csv.DictReader(product_file)
        for brand in set([product['brand_name_en'] for product in products]):
            node = Node('Brand', name=brand)
            tx.create(node)
        g.commit(tx)

    tx = g.begin()
    matcher = NodeMatcher(g)
    product_set = matcher.match("Product")
    brand_set = matcher.match("Brand")
    category_set = matcher.match("Category")

    tx = g.begin()
    with open('../store_dataset/product.csv', 'r') as product_file:
        products = csv.DictReader(product_file)
        for category in set([product['category_title_fa'] for product in products]):
            node = Node('Category', name=category)
            tx.create(node)
        g.commit(tx)

    tx = g.begin()
    with open('../store_dataset/product.csv', 'r') as product_file:
        products = csv.DictReader(product_file)
        for product in products:
            brand_node = brand_set.where(name=product['brand_name_en']).first()
            category_node = category_set.where(name=product['category_title_fa']).first()
            product_node = product_set.where(id=product['id']).first()

            brand_relation = Relationship(brand_node, 'have', product_node)
            category_relation = Relationship(product_node, 'member', category_node)
            tx.create(brand_relation)
            tx.create(category_relation)
        g.commit(tx)

    tx = g.begin()
    with open('../store_dataset/orders.csv', 'r') as f:
        orders = csv.DictReader(f)
        for city in set([order['city_name_fa'] for order in orders]):
            node = Node('City', name=city)
            tx.create(node)
        g.commit(tx)

    tx = g.begin()
    matcher = NodeMatcher(g)
    user_set = matcher.match("User")
    product_set = matcher.match("Product")
    city_set = matcher.match("City")

    with open('../store_dataset/orders.csv', 'r') as f:
        orders = csv.DictReader(f)
        for order in orders:
            node = Node(
                "Receipt",
                id=order['ID_Order'],
                date=order['DateTime_CartFinalize'],
                amount=float(order['Amount_Gross_Order'])
            )

            user_node = user_set.where(id=order['ID_Customer']).first()
            product_node = product_set.where(id=order['ID_Item']).first()
            city_node = city_set.where(name=order['city_name_fa']).first()

            buy_rel = Relationship(user_node, "buy", node)
            city_rel = Relationship(node, 'location', city_node)
            product_rel = Relationship(node, 'contain', product_node)

            tx.create(node)
            tx.create(buy_rel)
            tx.create(city_rel)
            tx.create(product_rel)

        g.commit(tx)

    matcher = NodeMatcher(g)
    user_set = matcher.match("User")
    product_set = matcher.match("Product")

    tx = g.begin()
    with open('../store_dataset/keifiat.csv', 'r') as f:
        comments = csv.DictReader(f)
        for comment in comments:
            user_node = user_set.where(id=comment['user_id']).first()
            product_node = product_set.where(id=comment['product_id']).first()
            comment_relation = Relationship(user_node, 'commented', product_node)
            comment_relation['score'] = int(comment['score'])
            tx.create(comment_relation)
        g.commit(tx)



