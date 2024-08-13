import importlib
import traceback

from utils.naming_utils import pascal_case_to_snake_case, snake_case_to_pascal_case

CLASS_SEPARATOR = "_"
MODULE_SEPARATOR = "."


class DynamicImportException(Exception):
    """
    Raise it when having issues dynamically importing objects
    """


def import_from_module(key: str):
    """
    Dynamically import an object from a module path
    """

    try:
        module_name, obj_name = key.rsplit(MODULE_SEPARATOR, 1)
        obj = getattr(importlib.import_module(module_name), obj_name)
        return obj
    except Exception as err:
        print(traceback.format_exc())
        raise DynamicImportException(f"Cannot load object from {key} due to {err}")


def import_widget_class(action_object_name):
    module_name = pascal_case_to_snake_case(action_object_name).removeprefix("action_")
    module_package_name = module_name.split(CLASS_SEPARATOR)[0]
    class_name = snake_case_to_pascal_case(module_name)

    return import_from_module(
        "widgets.{}.{}.{}Window".format(module_package_name, module_name, class_name)
    )
