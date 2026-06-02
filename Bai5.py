"""
INPUT:
===== HỆ THỐNG NGÂN HÀNG ĐIỂM SỐ RIKKEI ACADEMY =====
1. Hiển thị sao kê điểm số
2. Đổi điểm lấy phần thưởng
3. Phúc khảo bài thi (Hoàn điểm)
4. Kích hoạt (Hệ số nhân điểm)
5. Chấm bài (thêm điểm)
6. Thoát chương trình
=====================================================
Chọn chức năng (1-5):
CHO NGƯỜI DÙNG NHẬP VÀO LỰA CHỌN VÀ THỰC HIỆN CÁC CHÚC NĂNG ĐỀ BÀI YÊU CẦU
OUTPUT:
Yêu cầu: Viết hàm display_statements(records) để in ra toàn bộ dữ liệu. Quy định trạng thái:

Điểm hiện có < 500: "Cần tích lũy thêm "
500 <= Điểm hiện có <= 1500: "Thành viên tiềm năng "
Điểm hiện có > 1500: "Thành viên ưu tú "

*** Yêu cầu: Viết hàm appeal_score(records). Do hệ thống chấm nhầm, học viên phải "trả lại" quà đã đổi để lấy lại điểm, hoặc giáo vụ hoàn lại điểm đã trừ sai. Yêu cầu nhập:

Nhập mã học viên:
Nhập số điểm cần hoàn: Kiểm tra hợp lệ. Số điểm hoàn không được vượt quá số điểm đã tiêu (spent_points). Nếu hợp lệ: giảm spent_points, tăng current_points, tăng refunded_points.

*** Chức năng 4: Kích hoạt hệ số nhân điểm cho học viên trong các dịp lễ.  

*** Yêu cầu: Viết hàm activate_multiplier(records). Trong các tuần lễ đặc biệt, học viên làm bài sẽ được nhân hệ số điểm (x1.5, x2.0...). Yêu cầu nhập:

Nhập mã học viên:
Nhập hệ số nhân mới (Ví dụ 1.5): Hệ số phải là số thực (float) nằm trong khoảng từ 1.0 đến 3.0. Quá 3.0 không được phép (tránh lạm phát điểm).

** Yêu cầu: Viết hàm grade_assignment(records). Yêu cầu nhập:

Nhập mã học viên:
Nhập số điểm gốc đạt được: Hệ thống sẽ tự động tính: Điểm thực nhận = Điểm gốc * Hệ số nhân (multiplier). Sau đó cộng Điểm thực nhận vào current_points.
"""

student_records = [
    {
        "student_id": "RA01",
        "name": "Nguyễn Văn Code",
        "current_points": 1500,
        "spent_points": 500,
        "refunded_points": 0,
        "multiplier": 1.0
    },
    {
        "student_id": "RA02",
        "name": "Trần Thị Bug",
        "current_points": 800,
        "spent_points": 1200,
        "refunded_points": 100,
        "multiplier": 1.5
    },
    {
        "student_id": "RA03",
        "name": "Lê Văn Fix",
        "current_points": 300,
        "spent_points": 0,
        "refunded_points": 0,
        "multiplier": 2.0
    }
]

def display_statements(records):
    if not records:
        print('Danh sách hiện tại đang trống')
    else:
        print('--- SAO KÊ ĐIỂM SỐ ---')
        for i, item in enumerate(records, start=1):
            status = 'Thành viên ưu tú' if item['current_points'] > 1500 else ('Thành viên tiềm năng' if item['current_points'] >= 500 else 'Cần tích lũy thêm')
            print(f"{i}. Mã: {item['student_id']:<5} | Tên: {item['name']:<20} | Hiện có: {item['current_points']:<8} | Đã tiêu: {item['spent_points']:<8} | Hoàn trả: {item['refunded_points']:<8} | Hệ số: x{item['multiplier']:<8} | Trạng thái: {status:<30}")
        print('----------------------')

def redeem_rewards(records):
    input_id = input('Nhập mã học viên đổi quà: ')
    found = False
    
    for item in records:
        if input_id == item['student_id']:
            found = True  
            while True:
                input_point_str = input('Nhập số điểm cần tiêu: ')

                if input_point_str.isdigit():
                    input_point = int(input_point_str)
                    
                    if input_point > 0 and input_point <= item['current_points']:
                        item['current_points'] -= input_point
                        item['spent_points'] += input_point
                        
                        print(f">> Giao dịch thành công! {item['name']} đã tiêu {input_point} điểm. Số dư còn lại: {item['current_points']} điểm")
                        break 
                    else:
                        print(f"Số điểm không hợp lệ hoặc vượt quá số dư hiện có ({item['current_points']} điểm). Vui lòng nhập lại!")
                else:
                    print("Vui lòng chỉ nhập số nguyên dương!")
            break 
            
    if not found:
        print(f'Không tìm thấy học viên nào có mã {input_id}')

# CHỨC NĂNG 3: PHÚC KHẢO BÀI THI 
def appeal_score(records):
    input_id = input('Nhập mã học viên cần phúc khảo: ')
    found = False
    
    for item in records:
        if input_id == item['student_id']:
            found = True
            while True:
                refund_str = input('Nhập số điểm hoàn lại: ')
                if refund_str.isdigit():
                    refund_point = int(refund_str)
                    if 0 <= refund_point <= item['spent_points']:
                        item['spent_points'] -= refund_point
                        item['current_points'] += refund_point
                        item['refunded_points'] += refund_point
                        
                        print(f">> Hoàn điểm thành công! '{item['name']}' được cộng lại {refund_point} điểm.")
                        break
                    else:
                        print(f"Số điểm hoàn lại không hợp lệ hoặc vượt quá số điểm đã tiêu ({item['spent_points']} điểm). Vui lòng nhập lại!")
                else:
                    print("Vui lòng chỉ nhập số nguyên dương!")
            break
            
    if not found:
        print(f'Không tìm thấy học viên nào có mã {input_id}')

# CHỨC NĂNG 4: KÍCH HOẠT HỆ SỐ NHÂN ĐIỂM 
def activate_multiplier(records):
    input_id = input('Nhập mã học viên nhận hệ số: ')
    found = False
    
    for item in records:
        if input_id == item['student_id']:
            found = True
            while True:
                mul_str = input('Nhập hệ số nhân mới (1.0 - 3.0): ')
                try:
                    mul_value = float(mul_str)
                    if 1.0 <= mul_value <= 3.0:
                        item['multiplier'] = mul_value
                        print(f">> Đã kích hoạt hệ số x{mul_value} cho học viên '{item['name']}'.")
                        break
                    else:
                        print("Hệ số phải nằm trong khoảng từ 1.0 đến 3.0! Vui lòng nhập lại.")
                except ValueError:
                    print("Vui lòng nhập một số thực hợp lệ (Ví dụ: 1.5, 2.0)!")
            break
            
    if not found:
        print(f'Không tìm thấy học viên nào có mã {input_id}')

# CHỨC NĂNG 5: CHẤM BÀI
def grade_assignment(records):
    input_id = input('Nhập mã học viên vừa nộp bài: ')
    found = False
    
    for item in records:
        if input_id == item['student_id']:
            found = True
            while True:
                score_str = input('Nhập số điểm gốc đạt được: ')
                if score_str.isdigit():
                    base_score = int(score_str)
                    if base_score >= 0:
                        received_score = int(base_score * item['multiplier'])
                        item['current_points'] += received_score
                        
                        print(f">> Hệ số hiện tại của '{item['name']}' là x{item['multiplier']}. Điểm thực nhận: {received_score}.")
                        print(f">> Đã cộng {received_score} điểm vào tài khoản!")
                        break
                    else:
                        print("Điểm gốc không được là số âm!")
                else:
                    print("Vui lòng nhập một số nguyên dương hợp lệ!")
            break
            
    if not found:
        print(f'Không tìm thấy học viên nào có mã {input_id}')

def main():
    option = ''
    while option != '6':
        print('===== HỆ THỐNG NGÂN HÀNG ĐIỂM SỐ RIKKEI ACADEMY =====')
        print('1. Hiển thị sao kê điểm số')
        print('2. Đổi điểm lấy phần thưởng')
        print('3. Phúc khảo bài thi (Hoàn điểm)')
        print('4. Kích hoạt (Hệ số nhân điểm)')
        print('5. Chấm bài (thêm điểm)')
        print('6. Thoát chương trình')
        print('=====================================================')

        option = input('Nhập vào lựa chọn của bạn: ')

        match option:
            case '1':
                print()
                display_statements(student_records)
                print()
            case '2':
                print()
                redeem_rewards(student_records)
                print()
            case '3':
                print()
                appeal_score(student_records)
                print()
            case '4':
                print()
                activate_multiplier(student_records)
                print()
            case '5':
                print()
                grade_assignment(student_records)
                print()
            case '6':
                print('\nTạm biệt!')
            case _:
                print('\n[Lỗi] Lựa chọn của bạn không hợp lệ, vui lòng nhập lại lựa chọn của bạn\n')

if __name__ == '__main__':
    main()
