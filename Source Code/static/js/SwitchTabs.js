function openTabNumber(evt, TabNumber) {
  var i;
  var tabcontent = document.getElementsByClassName("tabcontent");
  
  // Ẩn tất cả các tabcontent
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  var tablinks = document.getElementsByClassName("tablinks");

  // Xóa lớp active khỏi tất cả các tablinks
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].classList.remove("active");
  }

  // Hiển thị tabcontent của tab được chọn và thêm lớp active vào tablinks tương ứng
  document.getElementById(TabNumber).style.display = "block";
  evt.currentTarget.classList.add("active");
}
