print ("cwiczenie 4.1")

is_in_unit_circle = lambda p: p[0]**2 + p[1]**2 <= 1

coordinates_positive = lambda p: p[0] > 0 and p[1] > 0

sorting_key_y_decreasing_x_increasing = lambda p: (-p[1], p[0])

sorting_key_sum_abs_x_y = lambda p: abs(p[0]) + abs(p[1])

point_list = [(0.5, 0.5), (1, 2), (-3, 4), (0, 0), (-1, -1), (3, -2)]

points_in_unit_circle = list(filter(is_in_unit_circle, point_list))
points_positive_coordinates = list(filter(coordinates_positive, point_list))
print("Points in unit circle:", points_in_unit_circle)
print("Points with positive coordinates:", points_positive_coordinates)

point_list.sort(key=sorting_key_y_decreasing_x_increasing)
print("Sorted by (y decreasing, x increasing):", point_list)
point_list.sort(key=sorting_key_sum_abs_x_y)
print("Sorted by the sum of absolute values of coordinates:", point_list)

print("cwiczenie 4.2")

def reverse_range_iterative(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

def reverse_range_recursive(L, left, right):
    if left >= right:
        return
    L[left], L[right] = L[right], L[left]
    reverse_range_recursive(L, left + 1, right - 1)


L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
reverse_range_iterative(L, 3, 6)
print("Iterative reverse:", L)  # [0, 1, 2, 6, 5, 4, 3, 7, 8, 9]

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  
reverse_range_recursive(L, 3, 6)
print("Recursive reverse:", L)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print ("ćwiczenie 4.3")
print ("a")
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 2

gen = infinite_sequence()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print("b")

def iter_odd():
    num = 1
    while True:
        yield num
        num += 2

gen =  iter_odd()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print("c")
def iter_power(k):
    num = 1
    while True:
        yield num
        num = num*k

gen =  iter_power(3)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))