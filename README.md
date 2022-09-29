# Product API Django REST
Product API Django REST Framework

## 🟢 GET - List products

Create product

###### Request Path
```
/api/products/
```
###### Request Headers
`Authorization` Token **{token}**

###### Response Example
```
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "ean": "7223820",
            "description": "Chocolate Dark Hazelnut Silver 300g",
            "category": "Foods",
            "price": 10.0,
            "images": [
                {
                    "id": 3,
                    "url": "https://m.media-amazon.com/images/I/41qjXGfmGRL.jpg"
                }
            ]
        }
    ]
}
```
## 🟢 GET - Get product 

Get just one product

###### Request Path
```
/api/products/1
```
###### Request Headers
`Authorization` Token **{token}**

###### Response Example
```
{
    "id": 1,
    "ean": "32131321",
    "description": "Perfume antonio bandeiras",
    "category": "Perfumes and Cosmetics",
    "price": 56.3,
    "images": []
}
```

## 🟡 POST - Create product 

Create product

###### Request Path
```
/api/products/
```
###### Request Headers
`Authorization` Token **{token}**

###### Request Body Example
```
{
    "ean": "7223820",
    "description": "Chocolate Dark Hazelnut Silver 300g",
    "price": 14.00,
    "category": "30"
}
```
###### Response Example
```
{
    "id": 2,
    "ean": "7223820",
    "description": "Chocolate Dark Hazelnut Silver 300g",
    "category": "Foods",
    "price": 14.0,
    "images": []
}
```
## 🔵 PUT - Update product 

Update product

###### Request Path
```
/api/products/2/
```
###### Request Headers
`Authorization` Token **{token}**

###### Request Body Example
```
{
    "ean": "7223820",
    "description": "Chocolate Dark Hazelnut Silver 300g",
    "price": 17.00,
    "category": "30"
}
```
###### Response Example
```
{
    "id": 2,
    "ean": "7223820",
    "description": "Chocolate Dark Hazelnut Silver 300g",
    "category": "Foods",
    "price": 17.0,
    "images": []
}
```
