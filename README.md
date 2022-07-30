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
