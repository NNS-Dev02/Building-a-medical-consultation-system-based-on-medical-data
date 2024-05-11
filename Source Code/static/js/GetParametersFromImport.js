function get12HourFormat() {
    const now = new Date();
    let hour = now.getHours();

    if (hour > 12) {
        hour -= 12;
    } else if (hour === 0) {
        hour = 12;
    }

    return hour;
}

function validateFields() {
    var fields = ['param1', 'param2', 'param3', 'param4', 'param5', 'param6'];
    for (var i = 0; i < fields.length; i++) {
        var value = parseFloat(document.getElementById(fields[i]).value);
        if (isNaN(value)) {
            return false; // Trường này chưa được điền dữ liệu
        }
    }
    return true; // Tất cả các trường đều đã có dữ liệu
}

function sendParams() {
    var isValid = validateFields(); // Kiểm tra trước khi gửi dữ liệu

    if (!isValid) {
        // Hiển thị thông báo khi có trường chưa được điền dữ liệu
        alert('Vui lòng nhập đầy đủ dữ liệu! Nếu chưa có dữ liệu, có thể bấm bỏ qua!');
        return; // Ngăn không gửi dữ liệu nếu có trường chưa được nhập liệu
    }

    var currentTime = get12HourFormat();

    var param1Value = parseFloat(document.getElementById('param1').value);
    if (param1Value < 2.5) {
        param1Value = 0;
    } else if (param1Value <= 7.5) {
        param1Value = 1;
    } else {
        param1Value = 2;
    }

    var param2Value = parseFloat(document.getElementById('param2').value);
    if (param2Value < 60) {
        param2Value = 0;
    } else if (param2Value <= 104) {
        param2Value = 1;
    } else {
        param2Value = 2;
    }

    var param3Value = parseFloat(document.getElementById('param3').value);
    if (param3Value < 50) {
        param3Value = 0;
    } else if (param3Value <= 200) {
        param3Value = 1;
    } else {
        param3Value = 2;
    }

    var param4Value = parseFloat(document.getElementById('param4').value);
    if (param4Value < 180) {
        param4Value = 0;
    } else if (param4Value <= 420) {
        param4Value = 1;
    } else {
        param4Value = 2;
    }

    var param5Value = parseFloat(document.getElementById('param5').value);
    if (param5Value < 50) {
        param5Value = 0;
    } else if (param5Value <= 137) {
        param5Value = 1;
    } else {
        param5Value = 2;
    }

    // Xử lý param6 theo điều kiện của bạn
    var param6Value = parseFloat(document.getElementById('param6').value);
    if (param6Value < 50) {
        param6Value = 0;
    } else if (param6Value <= 200) {
        param6Value = 1;
    } else {
        param6Value = 2;
    }

    var formData = new FormData();
    formData.append('current_time', currentTime);
    formData.append('param1', param1Value);
    formData.append('param2', param2Value);
    formData.append('param3', param3Value);
    formData.append('param4', param4Value);
    formData.append('param5', param5Value);
    formData.append('param6', param6Value);

    var xhr = new XMLHttpRequest();
    var url = '/write_params';

    xhr.open('POST', url, true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                alertWithOkButton('Dữ liệu đã được hệ thống ghi nhận!', function() {
                    hideForm();
                    window.location.href = '/show_results';
                });
            } else {
                alert('Có lỗi xảy ra ghi nhận dữ liệu!');
            }
        }
    };
    xhr.send(formData);
}

function alertWithOkButton(message, callback) {
    var confirmation = confirm(message);
    if (confirmation && typeof callback === 'function') {
        callback();
    }
}

function sendParamsAndHideForm() {
    sendParams();
}

function showForm() {
    document.getElementById('paramForm').style.display = 'block';
}

function hideForm() {
    document.getElementById('paramForm').style.display = 'none';
}

window.onload = function() {
    showForm();
};