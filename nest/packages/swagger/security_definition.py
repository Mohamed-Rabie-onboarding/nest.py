def security_definition(type: str = None, found_in: str = None, name: str = None, description: str = None):
    return {
        "type": type,
        "in": found_in,
        "name": name,
        "description": description
    }
