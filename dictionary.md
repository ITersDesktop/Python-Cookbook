# How to check a key existing or not in JSON object
Credit [Check if key exists and iterate the JSON](https://stackoverflow.com/questions/24898797/check-if-key-exists-and-iterate-the-json-array-using-python/24898931).
```
>>> h = {'a': 1, 'b': 2}
>>> 'b' in h    # returns True
>>> 'c' in h    # return False
>>> h.get('c')  # returns None
>>> h.get('c', 3) # returns a default value if 'c' doesn't exist
```

