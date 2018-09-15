# String's differences Between Python and Java

## From Leetcode 681

1. subString and string to int
    
    ```
    Python:
    cur = 60*int(time[:2])+int(time[3:])
    Java:
    cur = 60*Integer.parseInt(time.substring(0,2))+Integer.parseInt(time.substring(3));
    ```

2. String to Set

    ```
    Python:
    allowed = {int(x) for x in time if x!=":'}
    Java:
    Set<Integer> allowed = new Hashset();
    for(char c : time.toCharArray()) if(c!=":"){
        allowed.add(c-'0');
    }
    ```
    
    3. divmod to list or array

        ```
        Python:
        digits = [digit for block in divmod(cur,60) for digit in divmod(block,10))
        Java:
        int[] digits = new int[]{cur/60/10, cur/60%10, cur%60/10, cur%60%10};
        int candElapsed = Math.floorMod(cur-start,24*60)
        ```
    
    4. Wether all digits in allowed

        ```
        Python:
        if all(digit in allowed): return XX
        Java:
        search:{
            for (int digit: digits) if(!allowed.contains(d)) break search;
            return XX;
        }
        ```
    5.  String Format

        ```
        Python:
        "{:02d}:{:02d}".format(*divmod(cur,60))
        Java: 
        String.format("%02d:%02d", cur/60,cur%60);
        ```

