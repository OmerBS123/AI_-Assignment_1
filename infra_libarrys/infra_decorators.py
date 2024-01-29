from infra_libarrys.infra_classes.CustomException import CounterLimitExceeded

counter = 0
limit = 10000


def counter_decorator():
    def decorator(func):
        def wrapper(*args, **kwargs):
            global counter, limit
            counter += 1
            if limit is not None and counter > limit:
                print(f"Counter exceed limit of {limit} executing no step")
                raise CounterLimitExceeded("Exceed limit exception")
            return func(*args, **kwargs)

        return wrapper

    return decorator
