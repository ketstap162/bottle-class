# Bottle Class

Read this guideline before completing the task:  
[Guideline](https://github.com/ketstap162/tasks-guideline)

## Task  

Implement the `Bottle` class that will take one argument - the `size`.  
Note that:
- The bottle `size` cannot be lower than `0`. Otherwise, a `ValueError` should be raised.
- The bottle size must be an `integer`. Otherwise, a `TypeError` must be raised.
- When instantiated, the bottle must create 
a **protected** attribute `water` with a value of `0`

Implement a bottle property `water` and property setter.  
Note that:
- Value of `water` should store in protected attribute.
- The `water` can't be lower than `0` and greater than `bottle size`. Otherwise, a `ValueError` should be raised.
- The `water` must be an (ml) `integer`. Otherwise, a `TypeError` must be raised.

Run command `pytest` in terminal before pushing solution.
