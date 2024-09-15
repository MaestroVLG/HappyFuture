def introspection_info(obj):
    """Проводит интроспекцию объекта и возвращает словарь с информацией о нем.

    Args:
        obj: Объект, для которого проводится интроспекция.

    Returns:
        Словарь с информацией об объекте, включая тип, атрибуты, методы, модуль и другие свойства.
    """

    info = {
        "type": type(obj),
        "attributes": dir(obj),
        "methods": [method for method in dir(obj) if callable(getattr(obj, method))],
    }

    # Добавление дополнительных свойств в зависимости от типа объекта

    if isinstance(obj, int):
        info["bit_length"] = obj.bit_length()
    elif isinstance(obj, str):
        info["length"] = len(obj)
    elif isinstance(obj, list):
        info["length"] = len(obj)

    return info


# Пример использования

number_info = introspection_info(42)
print(number_info)
print(number_info["type"])
print(number_info["attributes"])
print(number_info["methods"])
print(number_info["bit_length"])





