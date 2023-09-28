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