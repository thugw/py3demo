from inspect import signature


DUPEFILTER_KEY = 'dupefilter:%(timestamp)s'

print(DUPEFILTER_KEY %{'timestamp': 'test3'})


dd = {"a":3, "b":5}

def tt(**kwargs):
    print(kwargs)

tt(**dd)