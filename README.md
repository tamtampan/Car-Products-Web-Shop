# Project

### This is server-side web shop application for car products. 

## Endpoints
### This is list of all database tables and almost every route. 

Every table have CRUD operations (Create - Read by id - Read all - Update - Delete)
##
1) Users: CRUD + Create superuser + **Log in** + Update password
2) Customers: CRUD + **Create customer with shopping cart** + Get by phone / email
3) Employees: CRUD
4) Offices: CRUD + Get by name
5) Producers: CRUD + Get by name
6) Product categories: CRUD + Get by name like
7) Products: CRUD + Update quantity in stock + **Get products for car brand** + **Get products by category name** + **Get all sorted by price from lowest** + Get all sorted by price from highest + **Get all products alphabetically sorted** + Read by code + Read by name or initial letters
8) Shopping cart: CRUD + Get by customer id
9) Cart item: CRUD + Create with customer id + **Get all items for shopping cart**
10) Shopping order: CRUD + **Create shopping order automatically** + **Get order with items** + **Get today shopping orders** + **Sum today profit**
11) Shopping order items: CRUD + Get items by shopping order id
#

Log in with:   
email: admin@itbc.rs   
password: Admin123!
#

Easiest way to make order:
- Get customer id (or create one, with Create Customer with Shopping cart route)
###### customer:
###### 058d223b-df63-4ac0-a044-b355f75d7f77
- Put customer id in Create Cart Item and add product id you like
###### products:
###### 20ff0e12-6ab4-4fe6-a799-d1d760781549
###### 45e2b827-edc0-4306-b9ed-d2cd4ad62902
###### 96b94911-a46c-4d70-933c-29d8450e0a93
- Put customer id in Create Shopping Order Automatically and add office id:
###### office:
###### 4d1049f8-6442-4268-a4cd-f5f7279a2d0c

���