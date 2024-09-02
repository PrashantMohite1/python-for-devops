


# Example of using 'with' to create an empty file

```
def create_file(filename);
    # create a blank file 
    print("Creating filename")
    with open(filename, 'w') as file:
        pass
```
