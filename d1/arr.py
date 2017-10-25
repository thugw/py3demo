from inspect import signature


DUPEFILTER_KEY = 'dupefilter:%(timestamp)s'

print(DUPEFILTER_KEY %{'timestamp': 'test2'})


dd = {"a":2, "b":5}

def tt(**kwargs):
    print(kwargs)

tt(**dd)