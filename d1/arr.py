from inspect import signature


DUPEFILTER_KEY = 'dupefilter:%(timestamp)s'

print(DUPEFILTER_KEY %{'timestamp': 'abc'})


dd = {"a":1, "b":5}

def tt(**kwargs):
    print(kwargs)

tt(**dd)