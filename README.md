# Product API Django REST
Product API Django REST Framework

## 🟢 GET - List Products

Get list of products

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
