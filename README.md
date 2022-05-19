# General

This is my project for the 14 assignment in Manma course in the Open University.

## Requirements

In order to use this code you need to have the following:
- python 3.10
  - numpy
  - pytest
  - typing


## How to use UI mode

To use the UI mode of this program you just need to run the main.py

## How to use CLI mode

To use the CLI mode of this program you can just easily run the "test_my_func.py" file.
If you want to change the possible values of 'n' or 'k' you can just easily change the values in the fixture:
```python
@pytest.fixture(params=[8, 50, 100])
def k(self, request) -> int:
```
Just change or add numbers to the array of the params
