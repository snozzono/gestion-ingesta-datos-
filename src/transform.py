def transform_data(data):
    transformed = []
    for user in data:
        transformed.append({
            "id": user["id"],
            "name": user["name"],
            "email": user["email"],
            "city": user["address"]["city"]
        })
    return transformed