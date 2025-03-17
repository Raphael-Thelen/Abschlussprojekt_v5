def analyze_data(data):
    if not data:
        return "No data to analyze"
    return {"lines": len(data)}