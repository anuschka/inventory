Inventory management system using Django REST framework

How to setup:
- install the requirements
- run makemigrations
- run migrate
- createsuperuser (not necessary)

Load initial data:
python manage.py loaddata db.json

RESTful Structure:
    products -> GET all products
    products/:id -> GET single product
    products -> POST add a single product
    products/:id -> PUT update a single product
    products/:id -> DELETE delete a single product

    batches -> GET all batches
    batches/:id -> GET single batch
    batches -> POST add a single batch
    batches/:id -> PUT update a single batch
    batches/:id -> DELETE delete a single batch

    orders -> GET all orders
    orders -> POST add a single order
    
    expired -> GET all expired batches
    expiring -> GET all expiring batches
    fresh -> GET all fresh batches
    
   