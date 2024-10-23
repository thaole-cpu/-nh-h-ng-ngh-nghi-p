import heapq
import sys

def smallest_sum_of_three(arr):
    # Tìm 3 số nhỏ nhất từ mảng
    three_smallest = heapq.nsmallest(3, arr)

    # Trả về tổng của ba số nhỏ nhất
    return sum(three_smallest)

# Đọc tất cả dữ liệu vào một lần
input = sys.stdin.read
data = input().split()

# Lấy số lượng bộ test
T = int(data[0])

index = 1
for _ in range(T):
    # Đọc số lượng phần tử trong mảng
    N = int(data[index])

    if N >= 3:
        # Lấy các phần tử của mảng
        A = list(map(int, data[index + 1:index + 1 + N]))
        print(smallest_sum_of_three(A))
    else:
        print("Không đủ phần tử")

    # Cập nhật vị trí index
    index += N + 1