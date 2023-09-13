// let variable1 = document.getElementById("demo1");
//     function getlocation() {
//     navigator.geolocation.getCurrentPosition(showLoc);
// }
// function showLoc(pos) {
//     // variable1.innerHTML =
//     // "Latitude: " +
//     // pos.coords.latitude +
//     // "<br>Longitude: " +
//     // pos.coords.longitude;
//     document.getElementById("Location").value = pos.coords.latitude
// }
fetch("https://api.ipify.org?format=json")
.then(response => response.json())
.then(data => {
document.getElementById("ip").value = data.ip;
});