def validate_required_fields(data, required_fields: list) -> bool:
    """Valida que los datos recibidos del 'Body' de la petición exista en la lista de campos requeridos."""
    return all(field in data for field in required_fields)