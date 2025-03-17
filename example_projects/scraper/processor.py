def process_data(raw_data):
    if not raw_data:
        return []
    return raw_data.split("\n")