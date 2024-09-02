
# Python One shot Notes

#### Function to create an empty file

The pass statement is used as a placeholder for future code. When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed. 

```
def create_file(filename);
    # create a blank file 
    print("Creating filename")
    with open(filename, 'w') as file:
        pass
```
