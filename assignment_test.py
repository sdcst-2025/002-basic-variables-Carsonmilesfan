#! python3

import assignment1
import assignment2
import assignment3

def test1():
  assert assignment1.x == 10
  assert assignment1.y == 2.4

def test2():
  assert assignment2.fname == "Mr"
  assert assignment2.lname == "Yang"

def test3():
  assert assignment3.value1 == 10
  assert assignment3.value2 == "10"