import requests 

product_resp=requests.get('https://dummyjson.com/products')
status_code=product_resp.status_code
print(status_code)  #200

product_data=product_resp.json()
print(type(product_data))

products=product_data['products']
print(type(products))