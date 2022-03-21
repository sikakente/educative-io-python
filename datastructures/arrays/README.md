# Arrays

## Table of contents

- [What is an array?](#what-is-an-array)
- [Properties of an array](#properties-of-an-array)
- [Strengths](#strengths)
- [Weaknesses](#weaknesses)
- [Problems](#problems)
    - [Best Time to Buy and Sell Stocks](best_time_to_buy_sell_stocks.md)
    - [Contains Duplicate](contains_duplicate.md)
    - [Insert Intervals](insert_intervals.md)
    - [Matrix Zeroes](matrix_zeroes.md)
    - [Maximum Water Container](max_water_container.md)
    - [Maximum Product Subarray](maximum_product_subarray.md)
    - [Merge Intervals](merge_intervals.md)
    - [Minimum in Rotated Sorted Array](minimum_rotated_sorted_array.md)
    - [Missing Number](missing_number.md)
    - [Non-Overlapping Intervals](non_overlapping_intervals.md)
    - [Product of Array Except Self](product_of_array_except_self.md)
    - [Rotate Image](rotate_image.md)
    - [Spiral Matrix](spiral_matrix.md)
    - [Three Sum](three_sum.md)
    - [Two Sum](two_sum.md)

## What is an array?

## Properties of an array

<table>
<tr>
  <th colspan="2"></th>
  <th>Search</th>
  <th>Access</th>
  <th>Insert</th>
  <th>Remove/Delete</th>
</tr>
 <tr>
  <th rowspan="2">Time Complexity</th>
  <th>Average</th>
  <td>O(n)</td>
  <td>O(1)</td>
  <td>O(n)</td>
  <td>O(n)</td>
 </tr>
 <tr>
  <th>Worst</th>
  <td>O(n)</td>
  <td>O(1)</td>
  <td>O(n)</td>
  <td>O(n)</td>
 </tr>
 <tr>
  <th rowspan="2">Space Complexity</th>
  <th>Average</th>
  <td>&nbsp;</td>
  <td>&nbsp;</td>
  <td>&nbsp;</td>
  <td>&nbsp;</td>
 </tr>
 <tr>
  <th>Worst</th>
  <td>&nbsp;</td>
  <td>&nbsp;</td>
  <td>&nbsp;</td>
  <td>&nbsp;</td>
 </tr>
</table>

## Strengths

- Fast lookups: It takes constant time O(1) to retrieve an element from an array, given its index.
- Fast appends: Adding an item or element at the end of an array takes O(1) time, provided the array is not full.

## Weaknesses

- Insertion and deletion in an array can be quite costly especially in the following scenarios.
    1. Deleting or inserting at the beginning of an almost full array.

## Applications

- Implementing a queue
- Implementing a stack
