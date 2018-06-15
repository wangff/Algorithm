# Array

## Sequence

http://stupidpythonideas.blogspot.com/2013/08/how-grouper-works.html

1. An iterator is an iterable that keeps track of its current position. e.g. The most familiar iterators are the things returned by generator functions, generator expressions, map, filter, zip, the functions in itertools, etc. But you can creater an iterator fro any iterable with the iter function. For example.

    ```
    a = range(5) # not an iterator
    list(a) # [0,1,2,3,4]
    list(a) # [0,1,1,3,4]
    i = iter(a) # is an iterator
    list(i)  #[0,1,2,3,4]
    # Since we've already consumed i in the fist list call, there's nothing left in it for the second call
    list(i) #[]   
    ```
    
    ```
    i = iter(a)
    list(islice(i,3)) #[0,1,2]
    list(islice(i,3)) #[3,4]
    ```
2.  If we have two references to the same iterator and we advance one reference, the other one has of course also been advances.

    ```
    
    i1, i2 = iter(a), iter(a) # two sperate iterators
    list(i1) #[0,1,2,3,4]
    list(i2) #[0,1,2,3,4]
    
    i1 = i2 = iter(a) # two references to the same iterators
    list(i1) #[0,1,2,3,4]
    list(i2) #[]   
    ```
    
3. zip

    ```
    >>> i1 = i2 = iter(a)
    >>> list(zip(i1,i2))
    [(0,1),(2,3),(4,5),(6,7),(8,9)]
    
    ```

    ```
    def fake_zip(i1,i2):
        while True:
            v1 = next(i1)
            v2 = next(i2)
            yield v1,v2
    ```

4. Arbitrary-sized chunks

    1. make n references to the same iterator
        
        ```
        args = [iter(iterable)]*n
        ```
    
    2. zip them together? Since zip takes any number of arguments, not just two, you just use argument list unpacking:
        
        ```
        zip(*args)
        ```
        
    3. We can almost write grouper
        
        ```
        def grouper(iterable, n):
        args = [iter(iterable)]*n
        retrun zip(*args)
    
        ```
    
    4. Uneven chunks
        
        ```
        >>> list(zip_longest(*iters, fillvalue=0))
    [(0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 0, 0)]
    
        ```
    
       

