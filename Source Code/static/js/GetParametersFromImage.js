let params = [];

function getParams(param) {
    params.push(param);

    if (params.length === 6) {
        sendParamsToServer();
    }
}

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

function sendParamsToServer() {
    const hour = get12HourFormat();

    params.unshift(hour);

    const data = new Blob([params.join(', ')], { type: 'text/plain' });

    const formData = new FormData();
    formData.append('file', data, 'params.txt');

    fetch('/upload', {
        method: 'POST',
        body: formData,
    })
    .then(response => {
    })
    .catch(error => {
        console.error('Lỗi:', error);
    });
}
