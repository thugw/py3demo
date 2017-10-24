from inspect import signature


DUPEFILTER_KEY = 'dupefilter:%(timestamp)s'

print(DUPEFILTER_KEY %{'timestamp': 'hh'})


dd = {"a":1, "b":2}

def tt(**kwargs):
    print(kwargs)

tt(**dd)