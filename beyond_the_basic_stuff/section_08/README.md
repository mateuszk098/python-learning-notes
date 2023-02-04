# **Common Python Gotchas:**

1. :x: **DO NOT APPEND AN ELEMENT TO THE LIST WHEN YOU ITERATE BY IT.**  
   WHY: Because such a loop can iterate forever.  
   :heavy_check_mark: Instead, do something like this:
    ```python
    # I want to have sock pairs.
    clothes = ["dress", "red sock"]
    new_clothes = []
 
    for cloth in clothes:
        if "sock" in cloth:
            new_clothes.append(cloth)
 
    clothes.extend(new_clothes)
    ```  
    ```python
    >>> print(clothes)
    ['dress', 'red sock', 'red sock']
    ```

2. :x: **DO NOT REMOVE ELEMENTS FROM THE LIST WHEN YOU ITERATE BY IT.**  
   WHY: Because some elements can be skipped due to indices shift.  
   :heavy_check_mark: Instead, do something like this:
    ```python
    # I want only "Hello" words.
    greetings = ["Hi", "Hello", "Cześć", "Welcome", "Hello"]
    greetings = [word for word in greetings if word == "Hello"]
    ```
    ```python
    >>> print(greetings)
    ['Hello', 'Hello']
    ```  
   Creating a new list is not wasting of memory because lists contain references to the objects, not the objects themselves.

3. :x: **WHEN YOU WANT TO CREATE A COPY OF MUTABLE OBJECT, USE `copy()` OR `deepcopy()` METHOD.**  
   WHY: Because ordinary assignment instruction copy only the reference to the mutable object.  
   :heavy_check_mark: Use `copy()` or `deepcopy()`:
    ```python
    import copy
    
    # Shallow copy of the list.
    spam = ["cat", "dog"]
    cheese = copy.copy(spam)
    
    # Deep copy of the list (use with nested lists).
    eggs = [[1, 2], [3, 4]]
    bacon = copy.deepcopy(eggs)
    ```

4. :x: **DO NOT USE A MUTABLE OBJECT AS A DEFAULT PARAMETER.**  
   WHY: Because the mutable object is created only once - when you define a function.  
   :heavy_check_mark: Use `None` instead:
    ```python
    def add_ingredient(ingredient, sandwich=None):
        if sandwich is None:
            sandwich = ["bread", "bread"]
        sandwich.insert(1, ingredient)
        return sandwich
    ```

5. :x: **DO NOT BUILD STRINGS WITH STRING CONCATENATION.**  
   WHY: Beacuse strings are not mutable. Each code, which apparently modifies the string, in fact, creates a new one.  
   :heavy_check_mark: Instead, use a list and `join()` method:
    ```python
    lst = ["spam" for _ in range(100_000)]
    my_str = " ".join(lst)
    ```

6. :x: **DO NOT EXPECT THAT `sort()` FUNCTION SORT THE LIST ALPHABETICALLY.**  
   WHY: Because `sort()` function sorts the list ascii-betically.  
   :heavy_check_mark: Define a key you want to sort the list with:
    ```python
    letters = ["a", "B", "b", "A"]
    letters.sort(key=str.lower)
    ```
7. :x: **DO NOT SUPPOSE FLOAT NUMBERS ARE IDEALLY ACCURATE.**  
   WHY: Because computers translate float numbers into binary under IEEE 754 standard. Such a representation is not always ideally consistent with decimal numbers.  
   :heavy_check_mark: If you need pure precision, use `decimal` module:
    ```python
    import decimal

    d = decimal.Decimal("0.1") # Pass as string.
    ```

8. :x: **DO NOT CHAIN INEQUALITY `!=` OPERATORS.**  
   WHY: Note the following expression:
    ```python
    >>> "cat" != "dog" != "cat"
    True
    ```
    That is equivalent to:
    ```python
    >>> ("cat" != "dog") and ("dog" != "cat")
    True
    ```

9. :x: **DO NOT FORGET ABOUT COMMA THE IN ONE-ELEMENT TUPLE.**  
    WHY: Because the following expression is treated as `str`.
    ```python
    >>> spam = ("cat")
    >>> spam[0]
    'c'
    ```
    That works:
    ```python
    >>> spam = ("cat", )
    >>> spam[0]
    'cat'
    ```