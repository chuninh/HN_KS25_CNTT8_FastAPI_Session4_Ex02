"""
1.Endpoint hiện tại có Path Parameter là:{status}
2. Khi gọi /orders/status/pending, biến status nhận giá trị : pending 
3.API hiện tại trả về sai dữ liệu vì mặc dù đã nhận được giá trị status từ URL,
nhưng chương trình không sử dụng biến status để lọc dữ liệu
4.Dòng code đang khiến API bỏ qua giá trị status là: return orders

"""

from fastapi import FastAPI

app = FastAPI()

orders = [
    {"id": 1, "customer_name": "Nguyễn Văn An", "total": 250000, "status": "pending"},
    {"id": 2, "customer_name": "Trần Thị Bình", "total": 500000, "status": "paid"},
    {"id": 3, "customer_name": "Lê Văn Cường", "total": 150000, "status": "cancelled"},
    {"id": 4, "customer_name": "Phạm Thị Dung", "total": 320000, "status": "pending"}
]


@app.get("/orders/status/{status}")
def get_orders_by_status(status: str):
    valid_status = ["pending", "paid", "cancelled"]

    if status not in valid_status:
        return {
            "message": "Trạng thái đơn hàng không hợp lệ"
        }

    result = []

    for order in orders:
        if order["status"] == status:
            result.append(order)

    return result
