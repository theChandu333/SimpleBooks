import json
import requests
import jsonpath
import random
from urllib.parse import urljoin


class Simplebooks:
    baseUrl = "https://simple-books-api.glitch.me"

    def get_status(self):
        endpoint = "/status"
        response = requests.get(urljoin(Simplebooks.baseUrl, endpoint))
        res = json.loads(response.text)
        return res

    def get_all_books(self):
        endpoint = "/books"
        response = requests.get(urljoin(Simplebooks.baseUrl, endpoint))
        res = json.loads(response.text)
        return res

    def get_book(self, book_id):
        endpoint = f"/books/{book_id}"
        response = requests.get(urljoin(Simplebooks.baseUrl,endpoint))
        res = json.loads(response.text)
        return res

    def authenticate(self):
        global token
        endpoint = "/api-clients/"
        num = random.randint(1, 100000)
        body = {"clientName": "Chandu", "clientEmail": f"Chand+{num}@example.com"}
        response = requests.post(urljoin(Simplebooks.baseUrl, endpoint), json=body)
        res = json.loads(response.text)
        token_list = jsonpath.jsonpath(res, "accessToken")
        token = token_list[0]
        return token


    def orders(self):
        endpoint = "/orders"
        url = urljoin(Simplebooks.baseUrl, endpoint)
        auth = {"Authorization": f"Bearer {token}"}
        response = requests.get(url, headers=auth)
        res = json.loads(response.text)
        return res


    def place_order(self):
        global order_id
        endpoint = "/orders"
        url = urljoin(Simplebooks.baseUrl, endpoint)
        body = {"bookId": 1, "customerName": "John"}
        auth = {'Authorization':"Bearer "+token}
        response = requests.post(url, headers=auth, json=body)
        res = json.loads(response.text)
        orders = jsonpath.jsonpath(res, "orderId")
        order_id = orders[0]
        return order_id


    def get_order_details(self):
        endpoint = f"/orders/{order_id}"
        url = urljoin(Simplebooks.baseUrl, endpoint)
        auth = {'Authorization': "Bearer " + token}
        response = requests.get(url,headers=auth)
        res = json.loads(response.text)
        return res


    def update_order(self):
        # global order_id
        endpoint = f"/orders/{order_id}"
        url = urljoin(Simplebooks.baseUrl, endpoint)
        body = {"customerName": "UpdatedUser"}
        auth = {"Authorization": f"Bearer {token}"}
        response = requests.patch(url, headers=auth, json=body)
        return response
        # order_list = jsonpath.jsonpath(res, "orderId")
        # order_id = order_list[0]
        # print(f"orderId: {order_id}")

    def del_order(self):
        # global order_id
        endpoint = f"/orders/{order_id}"
        url = urljoin(Simplebooks.baseUrl, endpoint)
        auth = {"Authorization": f"Bearer {token}"}
        response = requests.delete(url, headers=auth)
        return response


a = Simplebooks()
print(a.get_status())
print(a.get_all_books())
print(a.get_book(1))
print(a.authenticate())
print(a.orders())
print(a.place_order())
print(a.orders())
print(a.get_order_details())
print(a.update_order())
print(a.del_order())

