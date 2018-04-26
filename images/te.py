import sys

print('version: %s' % sys.version_info.major)

i = 100
print('before loop, i=%d' % i)
for i in range(10):
    pass

print('after loop, i=%d' % i)

i = 100
print('before conprehension, i=%d' % i)
# _ = [i for i in range(10)]
print('after conprehension, i=%d' % i)


a = 'string'
b = 100


def foo():
    c = 'string'
    d = 100
    print(a is c)
    print(b is d)


foo()
