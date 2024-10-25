def check_digits(n):
    n_str = str(n)
    # Lấy 2 chữ số đầu và 2 chữ số cuối
    first_two = n_str[:2]
    last_two = n_str[-2:]
    # Kết hợp cả 4 chữ số
    combined = first_two + last_two
    # Kiểm tra nếu có bất kỳ 2 chữ số nào giống nhau
    if len(set(combined)) < 4:
        return "YES"
    return "NO"

# Xử lý đầu vào
t = int(input())  # Số lượng bộ test
for _ in range(t):
    n = input().strip()  # Đọc từng số
    print(check_digits(n))