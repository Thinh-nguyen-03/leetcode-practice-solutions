# Removing Duplicates from Sorted Array

## Problem Description

Remove the duplicates in-place from a sorted array such that each unique element appears only once. Then, return the new length of the array with unique elements.

## Approach

Since the array is sorted, any duplicates will be adjacent. A pointer is used to keep track of the position where the next unique element should be placed. 

## Solution Explanation

`count` is initialized to 1, since the first element is always unique. Loop through the array starting from the second element, if the current element is different from the previous one, place it at the current `count` position.
Increment the `count` after placing a unique element. Return `count`, which is the new length of the array with unique elements.
