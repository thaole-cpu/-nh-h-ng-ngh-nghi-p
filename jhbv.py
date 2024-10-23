# Import thư viện ngẫu nhiên
import random


# Bước 1: Thu thập thông tin người dùng
def get_user_info():
    print("Chào mừng bạn đến với bài kiểm tra MBTI!")
    name = input("Vui lòng nhập tên của bạn: ")
    age = int(input("Vui lòng nhập tuổi của bạn: "))

    user_info = {
        "name": name,
        "age": age
    }

    return user_info


# Bước 2: Bài test MBTI 50 câu với các tùy chọn a, b, c, d
def run_mbti_test():
    print("\nBài test MBTI gồm 50 câu. Chọn một phương án phù hợp với bạn nhất: a, b, c, d.\n")

    # Danh sách câu hỏi MBTI (tổng cộng 50 câu hỏi đã được đánh số)
    questions = [
        ("1. Bạn có xu hướng tập trung vào thực tế hơn là lý thuyết?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("2. Bạn cảm thấy thoải mái khi giao tiếp với người lạ?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("3. Bạn thường lập kế hoạch cụ thể trước khi thực hiện công việc?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("4. Bạn thích tìm hiểu và khám phá những ý tưởng mới?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("5. Bạn thích làm việc theo kế hoạch hơn là làm việc ngẫu hứng?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("6. Bạn có xu hướng phân tích sự việc một cách logic và lý trí?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("7. Bạn thường dựa trên cảm xúc để ra quyết định?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("8. Bạn thích các hoạt động xã hội và thường chủ động giao tiếp với mọi người?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("9. Bạn có xu hướng hướng nội, thích ở một mình để suy ngẫm?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("10. Bạn thích làm việc với dữ liệu và sự thật hơn là tưởng tượng?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("11. Bạn cảm thấy thoải mái khi làm việc theo kế hoạch dài hạn?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("12. Bạn có xu hướng suy nghĩ về tương lai nhiều hơn hiện tại?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("13. Bạn thích ra quyết định nhanh chóng?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("14. Bạn thích tìm hiểu sâu về một chủ đề cụ thể?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("15. Bạn thường quan tâm đến cảm xúc của người khác trong các quyết định của mình?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("16. Bạn có xu hướng quản lý thời gian chặt chẽ và kỷ luật?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("17. Bạn thích khám phá và thay đổi, hơn là duy trì mọi thứ như hiện tại?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("18. Bạn thường cảm thấy thoải mái khi làm việc dưới áp lực thời gian?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("19. Bạn thường cảm thấy kiên nhẫn trong các tình huống căng thẳng?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("20. Bạn thích làm việc trong môi trường yên tĩnh, ít bị phân tâm?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("21. Bạn thường lên kế hoạch chi tiết cho các hoạt động hàng ngày?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("22. Bạn thích có thời gian tự do để linh hoạt sáng tạo?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("23. Bạn có xu hướng đặt mục tiêu cụ thể và rõ ràng?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("24. Bạn cảm thấy thoải mái khi đối mặt với những thay đổi đột ngột?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("25. Bạn thích thực hiện những kế hoạch lâu dài hơn là những công việc ngắn hạn?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("26. Bạn cảm thấy hứng thú khi giải quyết các vấn đề phức tạp?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("27. Bạn thường ưu tiên cho các hoạt động cá nhân hơn là nhóm?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("28. Bạn cảm thấy dễ dàng làm việc theo nhóm?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("29. Bạn có xu hướng tránh né những tình huống căng thẳng xã hội?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("30. Bạn thích học hỏi thông qua trải nghiệm thực tế?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("31. Bạn cảm thấy thoải mái khi làm việc với dữ liệu và phân tích?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("32. Bạn có xu hướng suy nghĩ chi tiết trước khi ra quyết định?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("33. Bạn cảm thấy hứng thú khi khám phá những ý tưởng mới lạ?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("34. Bạn có xu hướng suy nghĩ chiến lược khi đối mặt với các vấn đề?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("35. Bạn thích làm việc với các con số hơn là với con người?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("36. Bạn thích những công việc đòi hỏi sự chi tiết và tỉ mỉ?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("37. Bạn có xu hướng tự động điều chỉnh theo môi trường làm việc?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("38. Bạn thích dành thời gian suy nghĩ về ý tưởng trước khi thực hiện?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("39. Bạn cảm thấy thoải mái khi làm việc dưới thời gian gấp rút?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("40. Bạn thích các hoạt động yêu cầu sự sáng tạo và linh hoạt?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),
        ("41. Bạn thích lập kế hoạch mọi thứ từ trước thay vì hành động theo cảm hứng?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),
        ("42. Bạn có xu hướng dễ thích nghi với những thay đổi trong cuộc sống?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),
        ("43. Bạn thích làm việc với các con số và phân tích số liệu?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),
        ("44. Bạn có xu hướng ưu tiên cảm xúc hơn là lý trí khi đưa ra quyết định?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),
        ("45. Bạn có xu hướng giữ im lặng trong những cuộc thảo luận nhóm?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),
        ("46. Bạn thích tìm hiểu về tương lai và những khả năng mới hơn là tập trung vào hiện tại?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),
        ("47. Bạn có xu hướng làm việc nhóm tốt hơn làm việc độc lập?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),
        ("48. Bạn thích xử lý các vấn đề dựa trên dữ liệu và sự kiện hơn là dựa trên cảm nhận?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),
        ("49. Bạn có xu hướng giải quyết các vấn đề theo trình tự rõ ràng?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("50. Bạn có xu hướng tránh rủi ro và luôn muốn an toàn trong công việc?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý")
    ]

    # Dữ liệu lưu trữ kết quả (tính cho 4 nhóm MBTI chính)
    score = {
        "E": 0,  # Extraversion
        "I": 0,  # Introversion
        "S": 0,  # Sensing
        "N": 0,  # Intuition
        "T": 0,  # Thinking
        "F": 0,  # Feeling
        "J": 0,  # Judging
        "P": 0  # Perceiving
    }

    # Mapping câu trả lời với nhóm MBTI
    answer_map = {
        "a": {"E": 1, "S": 1, "T": 1, "J": 1},
        "b": {"E": 0.5, "S": 0.5, "T": 0.5, "J": 0.5},
        "c": {"I": 0.5, "N": 0.5, "F": 0.5, "P": 0.5},
        "d": {"I": 1, "N": 1, "F": 1, "P": 1}
    }

    # Chạy qua tất cả các câu hỏi
    for i, question in enumerate(questions, start=1):
        print(f"\n{question[0]}")
        print(question[1])
        print(question[2])
        print(question[3])
        print(question[4])

        answer = input("Chọn câu trả lời (a, b, c, d): ").lower()

        # Cập nhật điểm theo nhóm MBTI
        if answer in answer_map:
            for key in answer_map[answer]:
                score[key] += answer_map[answer][key]

    return score


# Bước 3: Gợi ý kết quả MBTI
def suggest_mbti_result(score):
    # Tính toán nhóm MBTI dựa trên điểm số
    personality = ""
    personality += "E" if score["E"] >= score["I"] else "I"
    personality += "S" if score["S"] >= score["N"] else "N"
    personality += "T" if score["T"] >= score["F"] else "F"
    personality += "J" if score["J"] >= score["P"] else "P"

    print(f"\nDựa trên kết quả bài kiểm tra, kiểu MBTI của bạn là: {personality}")

    # Gợi ý nghề nghiệp hoặc trường đại học phù hợp với kiểu MBTI
    if personality == "INTJ":
        suggestion = "Bạn có thể phù hợp với các ngành nghề kỹ thuật, quản lý, hoặc nghiên cứu khoa học."
    elif personality == "ENTP":
        suggestion = "Bạn có thể phù hợp với các ngành nghề về marketing, kinh doanh, hoặc công nghệ thông tin."
    # Thêm các kiểu MBTI khác và gợi ý tương ứng
    else:
        suggestion = "Bạn có thể xem xét các ngành nghề hoặc trường học phù hợp với tính cách của mình."

    print(f"Gợi ý cho bạn: {suggestion}")


# Chương trình chính
def mbti_test_program():
    user_info = get_user_info()
    score = run_mbti_test()
    suggest_mbti_result(score)


# Khởi chạy chương trình
mbti_test_program()
