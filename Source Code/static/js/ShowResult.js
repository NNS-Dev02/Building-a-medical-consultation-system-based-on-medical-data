fetch('/get_result_content')  // Endpoint để lấy nội dung từ result.txt
    .then(response => response.text())
    .then(content => {
        // Tách nội dung thành mảng các dòng để lấy dòng thứ hai
        const lines = content.trim().split('\n');
        
        // Kiểm tra xem liệu có đủ dòng để lấy dòng thứ hai không
        if (lines.length >= 2) {
            const divNumber = parseInt(lines[0]); // Chuyển đổi dòng thứ nhất thành số nguyên
            const secondParam = lines[1].trim(); // Lấy dòng thứ hai và loại bỏ khoảng trắng đầu cuối

            // Hiển thị div tương ứng dựa trên số từ dòng thứ nhất
            switch (divNumber) {
                case 1:
                    document.getElementById('div1').style.display = 'block';
                    break;
                case 2:
                    document.getElementById('div2').style.display = 'block';
                    break;
                case 3:
                    document.getElementById('div3').style.display = 'block';
                    break;
                case 4:
                    document.getElementById('div4').style.display = 'block';
                    break;
                default:
                    // Nếu không phù hợp với bất kỳ điều gì, có thể ẩn tất cả các div hoặc xử lý theo cách khác
                    console.error('Không tìm thấy nội dung phù hợp');
            }

            // Sử dụng tham số từ dòng thứ hai tại đây (secondParam)
            console.log('Tham số từ dòng thứ hai:', secondParam);
        } else {
            console.error('Không có đủ dữ liệu để lấy dòng thứ hai');
        }
    })
    .catch(error => console.error('Có lỗi xảy ra:', error));
