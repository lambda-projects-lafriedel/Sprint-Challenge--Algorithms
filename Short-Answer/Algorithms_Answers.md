Add your answers to the Algorithms exercises here.

a)  a = 0 --- O(c) -- runs only once in isoliation
    while (a < n^3): --- O(n)
      a = a + n^2 --- O(c), runs only once in isolation

The isolated amounts are c + n * c, which is O(c + nc) but simplifies to O(n), or linear. The amount of operations equals n.

For example:
n = 3: 
(1.) a = 0, 0 < 27, a = 0 + 9 // 
(2.) a = 9, 9 < 27, a = 9 + 9 // 
(3.) a = 18, 18 < 27, a = 18 + 9 // a = 27, while loop breaks.

b)  n = 5

  sum = 0 --- O(c), runs only once in isolation
    for i in range(n): --- O(n) -- runs as many times as val of n
      i += 1
                      2     5
      for j in range(i + 1, n): --- O(n), runs as many times as val of n
        j += 1
                        2     10
        for k in range(j + 1, n): --- O(n), runs as many times as val of n
          k += 1
                          2       11
          for l in range(k + 1, 10 + k): --- O(10 + k), runs as many times as val of k + 10
            l += 1
            sum += 1

The isolated amounts are c + n * n * n * (k + 10), which is O(c + n^3 * (k + 10)). Even though the range is a different variable than n, I'm going to say this is O(n^4) and not O(n^3) because the final for loop will run a linear amount of times based on the size of n. Sicne the third for loop will run longer depending on the size of n, thus making the value of k higher, then the last for loop will run longer as well.


Exercise II

Notes:
Building is n stories tall (a finite amount)
Egg breaks if thrown off floor f or greater than floor f. So Floors f --> n is when the egg will break.

I'd use a binary search/divide and conquer algorithm to find at what floor the eggs would break. If I had a building of 10 floors, I'd divide the list in half and start with floor 5. If I drop an egg from there and it doesn't break, I'd discard the lower half of the floors and only search in floors 6 - 10. I'd divide that half of the list in half, and test my dropped egg at floor 8. If it breaks, I'd discard the floors higher than 8 and search within floors 6 and 7. Since I'd divide this in half, I'd test floor 7. If it breaks there, we know we need to test floor 6, and if it breaks on floor 6 then that's the floor at which an egg first breaks. If we test floor 7 and it doesn't break, then we know that it also wouldn't break at floor 6, meaning the first floor at which an egg would break is 8.