def transform_weather(data):
    current = data.get("current_weather", {})
    
    transformed = [{
        "temperature": current.get("temperature"),
        "windspeed": current.get("windspeed"),
        "winddirection": current.get("winddirection"),
        "time": current.get("time")
    }]
    
    return transformed