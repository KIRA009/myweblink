import jsonschema
from collections import ChainMap

from .exceptions import AccessDenied


def decorator(func, test_func):
    def inner(*args, **kwargs):
        request = args[0]
        if 'User' in request.__dict__:
            if test_func(request.User):
                return func(*args, **kwargs)
        elif request.user.is_authenticated:
            if test_func(request.user):
                return func(*args, **kwargs)
        raise AccessDenied()

    return inner


def login_required(func):
    return decorator(func, lambda u: u.is_authenticated)


def validate(*_properties):
    def inner(func):
        def inner2(cls, request, **kwargs):
            if 'json' in request.__dict__:
                properties = dict(ChainMap(*_properties))
                required = []
                for k, v in properties.items():
                    if 'required' in v:
                        if v['required']:
                            required.append(k)
                        del v['required']
                schema = dict(
                    type="object",
                    properties=properties,
                    required=required
                )
                try:
                    jsonschema.validate(request.json, schema)
                except jsonschema.exceptions.ValidationError as e:
                    raise AccessDenied(e.message)
            return func(cls, request, **kwargs)
        return inner2
    return inner
