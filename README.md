# Product API Django REST
Product API Django REST Framework

## 🟢 GET - List Products

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
## 🟢 GET - Get Product 

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

## 🟡 POST - Create Product 

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
