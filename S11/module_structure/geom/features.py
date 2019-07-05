from . import shapes


class Area:
    def __get__(self, instance, owner):
        if isinstance(instance, shapes.Rectangle):
            return instance.width * instance.height

        elif isinstance(instance, shapes.Circle):
            return 3.1415 * instance.radius ** 2

    def __set__(self, instance, value):
        ratio = (value / instance.area) ** 0.5

        if isinstance(instance, shapes.Rectangle):
            instance.width *= ratio
            instance.height *= ratio

        elif isinstance(instance, shapes.Circle):
            instance.radius *= ratio


class Perimeter:
    def __get__(self, instance, owner):
        if isinstance(instance, shapes.Rectangle):
            return 2 * (instance.width + instance.height)

        elif isinstance(instance, shapes.Circle):
            return 3.1415 * instance.radius * 2

    def __set__(self, instance, value):
        ratio = value / instance.perimeter

        if isinstance(instance, shapes.Rectangle):
            instance.width *= ratio
            instance.height *= ratio

        elif isinstance(instance, shapes.Circle):
            instance.radius *= ratio
