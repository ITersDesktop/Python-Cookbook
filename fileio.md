# How does often python flush a file?

As you know, Python does flush to stdout every new line in real time while it uses the operating system's default buffering settings to flush file operations unless we configur it do otherwise. We can specify a buffer size, unbuffered or line buffered. The `open` function is an example of facilitating these configurations. Read [more](http://docs.python.org/library/functions.html#open) in The Python Language Reference.
```
buffer_size = 1024
f = open("file.txt", "w", buffering=buffer_size)
```
where the `buffer_size` variable can be
* 0 means unbuffered
* 1 means line buffered
* any other positive value means use a buffer of (approximately) that size
* a negative buffering means to use the system default, which is usually line buffered for tty (aka. stdout) devices and fully buffered for other files.
* if omitted, the system default is used

# How can we check the extension of a file?
Credit at [Stackoverflow](https://stackoverflow.com/questions/5899497/how-can-i-check-the-extension-of-a-file). Assuming `filename` is defined as the variable of a file name. We can use `endswith` function:
```
if m.endswith('.mp3'):
...
elif m.endswith('.flac'):
...
```

To be case-insensitive, and to eliminate a pententially large else-if chain: `m.lower().endswith(('.png', '.jpg', '.jpeg'))
`. Voilà!

However, we often get the list of file paths. The better way to get the file extension is to use `os.path.splitext(filepath)[1]` or `Path(filename).suffix`, so on. The `os.path.splitext` function takes a path and splits the file extension from the end of it.
```
import os

filepaths = ["/folder/soundfile.mp3", "folder1/folder/soundfile.flac"]

for fp in filepaths:
    # Split the extension from the path and normalise it to lowercase.
    ext = os.path.splitext(fp)[-1].lower()

    # Now we can simply use == to check for equality, no need for wildcards.
    if ext == ".mp3":
        print("{} is an mp3!".format(fp))
    elif ext == ".flac":
        print("{} is a flac file!".format(fp))
    else:
        print("{} is an unknown file format.".format(fp))
```

The `pathlib` comes to exist from Python 3.4 or newer versions.
```
from pathlib import Path
Path('my_file.mp3').suffix == '.mp3'
```

Look at module fnmatch. That will do what you're trying to do.
```
import fnmatch
import os

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.txt'):
        print(file)
```

Using `glob` module, we can do like:
```
from glob import glob
...
for files in glob('path/*.mp3'): 
  do something
for files in glob('path/*.flac'): 
  do something else
```

# How can we generate random file names?
Credit [here on stackoverflow](). We can use either of the following solutions:

Using the [UUID module](http://docs.python.org/library/uuid.html) module for generating a random string:
```
import uuid
filename = str(uuid.uuid4())
```

Using `tempfile` module:
Python has facilities to generate temporary file names, see [tempfile](http://docs.python.org/library/tempfile.html). For instance:
```
import tempfile
tf = tempfile.NamedTemporaryFile()
print(tf.name) # output: /tmp/tmptjfxgqtc
tf = tempfile.NamedTemporaryFile()
print(tf.name) # output: /tmp/tmp9opi3hza
```

# How do we copy files and directories?
References: [Copy Files and Directories in Python](https://pynative.com/python-copy-files-and-directories/), [How to copy files from one folder to another using Python?](https://www.tutorialspoint.com/How-to-copy-files-from-one-folder-to-another-using-Python), [Python Copy File – Copying Files to Another Directory](https://www.freecodecamp.org/news/python-copy-file-copying-files-to-another-directory/), [copydir](https://gist.github.com/dreikanter/5650973).

# How can we change permissions on files and a directory?
References: [Setting Chmod Value with Python](https://ismailtasdelen.medium.com/setting-chmod-value-with-python-7e14daaf09b3), [https://stackoverflow.com/questions/12791997/how-do-you-do-a-simple-chmod-x-from-within-python](https://stackoverflow.com/questions/12791997/how-do-you-do-a-simple-chmod-x-from-within-python), [Working with Files and Directories in Python
](https://www.devdungeon.com/content/working-files-and-directories-python)

# How can we set permissions recursively for a directory?
I found [here](https://www.adamsmith.haus/python/examples/4291/os-set-permissions-recursively-for-a-directory) working like a charm.

Using subprocess module to call any OS command like
```
>>> import subprocess
>>> subprocess.call(['chmod', '-R', '+w', 'biomodels-jummp'])
```

If you want to use the os module, you'll have to recursively write it:
```
import os
def change_permissions_recursive(path, mode):
    for root, dirs, files in os.walk(path, topdown=False):
        for dir in [os.path.join(root,d) for d in dirs]:
            os.chmod(dir, mode)
    for file in [os.path.join(root, f) for f in files]:
            os.chmod(file, mode)
change_permissions_recursive('my_folder', 0o777)
```

# How to move files
The whole receipt is copied from [this thread](https://stackoverflow.com/questions/8858008/how-do-i-move-a-file-in-python).
## Method 1: Using either `os.rename()`, `os.replace()`, or `shutil.move()` with the same syntax.
```
import os
import shutil

os.rename("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
os.replace("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
```
Remember: 
* The filename (`"file.foo"`) must be included in both the source and destination arguments. If it differs between the two, the file will be renamed as well as moved.
* The directory within which the new file is being created must already exist.
* On Windows, a file with that name must not exist or an exception will be raised, but `os.replace()` will silently replace a file even in that occurrence.
* `shutil.move` simply calls `os.rename` in most cases. However, if the destination is on a different disk than the source, it will instead copy and then delete the source file.

Source: [here](https://stackoverflow.com/a/8858026)

## Method 2: Using `os.system` to call `mv` command in Linux
If you don't care about the returned value, you can do
```
import os
os.system("mv src/* dest/") 
```

## Method 3: Using `pathlib` of class `Path` after Python 3.4
After Python 3.4, you can also use `pathlib`'s class `Path` to move file.

```
from pathlib import Path

Path("path/to/current/file.foo").rename("path/to/new/destination/for/file.foo")
```
More reading: [pathlib.Path.rename](https://docs.python.org/3.4/library/pathlib.html#pathlib.Path.rename)