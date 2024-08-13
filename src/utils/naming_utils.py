import re


def pascal_case_to_snake_case(camel_case: str):
    """驼峰转下划线"""
    snake_case = re.sub(r"(?P<key>[A-Z])", r"_\g<key>", camel_case)
    return snake_case.lower().strip('_')


def snake_case_to_pascal_case(snake_case: str):
    """下划线转驼峰"""
    words = snake_case.split('_')
    return ''.join(word.title() for word in words)