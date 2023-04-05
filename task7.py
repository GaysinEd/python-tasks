"""
Бесконечное количество полок расположены одна над другой в шахматном порядке.
Кошка может прыгать на одну или три полки одновременно: с полки i на полку i+1 или i+3
(кошка не может залезть на полку прямо над своей головой), согласно иллюстрации:

                 ┌────────┐
                 │-6------│
                 └────────┘
┌────────┐
│------5-│
└────────┘  ┌─────► OK!
            │    ┌────────┐
            │    │-4------│
            │    └────────┘
┌────────┐  │
│------3-│  │
BANG!────┘  ├─────► OK!
  ▲  |\_/|  │    ┌────────┐
  │ ("^-^)  │    │-2------│
  │ )   (   │    └────────┘
┌─┴─┴───┴┬──┘
│------1-│
└────────┘
Input
Start and finish shelf numbers (always positive integers, finish no smaller than start)

Task
Find the minimum number of jumps to go from start to finish

Example
Start 1, finish 5, then answer is 2 (1 => 4 => 5 or 1 => 2 => 5)
"""

def solution(start, finish):
    difference = finish - start
    return difference // 3 + difference % 3
