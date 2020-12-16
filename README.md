# 20201_PTPMPT_LTU15C_Nhom4
## Đề tài
```
Hệ thống phát hiện đối tượng trong ảnh.
Sử dụng Socket nhận ảnh từ máy thứ nhất chuyển dữ liệu qua máy thứ 2.
Máy thứ 2 sẽ dùng thuật toán để phát hiện đối tượng trong ảnh.
```
## Thành viên
```
Nguyễn Xuân Phú – 20168411
Nguyễn Hải Anh - 20168619
Nguyễn Kỳ Thông – 20168807
Nguyễn Lê Quang Huy - 20168230
```
## Công nghệ sử dụng
```
Server: Python, OpenCV(https://opencv.org/), Socket
Client: Python, Socket
```

## Cài đặt
```
- Cài đặt docker (https://docs.docker.com/get-docker/)
- Clone project về máy
- Mở hai terminal ở hai folder /backend và /frontend
- Ở terminal của backend, dùng lệnh "docker network create mynetwork" để tạo mạng giữa hai container.
  Tiếp theo dùng "docker build -t serversocket ." để build container.
  Cuối cùng dùng "docker run --rm --network=mynetwork --name myserver serversocket" để chạy container.
- Ở terminal của frontend dùng "docker build -t clientsocket ." để build container.
  Cuối cùng dùng "docker run --rm --network=mynetwork clientsocket" để chạy container.
- Ở terminal của frontend sẽ hiện kết quả các đối tượng phát hiện trong ảnh
```
