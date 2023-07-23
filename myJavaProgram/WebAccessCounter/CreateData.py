import random
from datetime import datetime, timedelta

# Danh sách các trang web
web_pages = ["/page1", "/page2", "/page3", "/page4", "/page5"]

# Số lần truy cập tối đa cho mỗi trang web
max_accesses = 100

# Ngày bắt đầu và ngày kết thúc
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 1, 31)

# Tạo dữ liệu giả
with open("input_log.txt", "w") as file:
    current_date = start_date
    while current_date <= end_date:
        for _ in range(max_accesses):
            # Tạo một truy cập ngẫu nhiên
            remote_host = "192.168.0." + str(random.randint(1, 100))
            timestamp = current_date.strftime("%d/%b/%Y:%H:%M:%S")
            web_page = random.choice(web_pages)
            status = random.choice([200, 404, 500])
            bytes_transferred = random.randint(100, 1000)
            log_entry = f"{remote_host} - - [{timestamp} +0000] \"GET {web_page} HTTP/1.1\" {status} {bytes_transferred}\n"
            
            # Ghi dòng nhật ký vào tệp tin
            file.write(log_entry)
        
        # Tăng ngày lên một
        current_date += timedelta(days=1)
