function startTime() {
    var today = new Date();
    var h = today.getHours();
    h = h % 12;
    h = h ? h : 12;
    var m = today.getMinutes();
    var s = today.getSeconds();
    var n = today.toDateString(); 
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('live_time').innerHTML = "<i class='fa fa-clock-o'></i>" + ": " + h + ":" + m + ":" + s;
    document.getElementById('the_date').innerHTML = "<i class='fa fa-calendar'></i>" + ": "  + n;
    var t = setTimeout(startTime, 500);
}
function checkTime(i) {
    if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
    return i;
}