from datetime import timedelta

def period_is_late(last,today,cycle_length):
    delta = timedelta(days=cycle_length) + last
    return delta < today