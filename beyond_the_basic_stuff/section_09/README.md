# **Esoteric Python Oddities:**

1. **WHY 256 is 256, BUT 257 is not 257.**  
    ```python
    >>> a = 256
    >>> b = 256
    >>> a is b
    True
    ```
    ```python
    >>> c = 257
    >>> d = 257
    >>> c is d
    False
    ```  
    In order to optimise, CPython (interpreter) creates integer objects with values from -5 to 256. It happens because there is a huge probability that the program will use integer 1 or 2 than 1953. While creating a new integer object, CPython checks if it is between -5 and 256. If yes, CPython returns the existing object instead of creating a new one. Therefore,  a situation like the above may arise.

2. **STRING INTERNING.**  
    ```python
    >>> spam = "cat"
    >>> eggs = "cat"
    >>> spam is eggs
    True
    ```
    This is a similar optimisation as in the first point. However, never write code which is based on that. Moreover, this optimisation does not capture all possible same strings.

3. **ARTIFICIAL INCREMENT AND DECREMENT OPERATORS.**  
    ```python
    >>> eggs = 42
    >>> eggs = --eggs
    >>> eggs
    42
    ```  
    This is nothing more than the following
    ```python
    >>> eggs = 42
    >>> eggs = -(-eggs)
    >>> eggs
    42
    ```  

4. **ALL OF NOTHING.**  
   The `all()` function returns `False` if one or more values in the passed list represent `False`. Otherwise, it returns `True`.  
   Note the following:
    ```python
    >>> all([False, False, True])
    False
    ```  
    For the empty list, the result is as follows.
    ```python
    >>> all([])
    True
    ```
    The best way to interpret this is to think that none of the elements represents `False`.

5. **BOOLEANS ARE INTEGERS.**
    ```python
    >>> False == 0
    True
    >>> True == 1
    True
    ```
    ```python
    >>> isinstance(False, int)
    True
    >>> isinstance(True, int)
    True
    ```
    ```python
    >>> False + True + True + True
    3
    ```
    ```python
    >>> spam = "Hello"
    >>> spam[-True]
    'o'
    ```

6.  **CHAIN OF DIFFERENT OPERATORS.**
    ```python
    >>> False == False in [False]
    True
    ```
    The above expression is equivalent to:
    ```python
    >>> (False == False) and (False in [False])      
    True
    ```

7. **ANTIGRAVITY.**  
   Check this:
   ```python
   >>> import antigravity
   ```
   This is a joke and it is equivalent to:
   ```python
   >>> import webbrowser
   >>> webbrowser.open("https://xkcd.com/353/")
   ```  