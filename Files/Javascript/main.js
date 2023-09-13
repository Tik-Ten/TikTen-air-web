navigator.geolocation.getCurrentPosition(
    function (position) {
        document.getElementById("lat").value = position.coords.latitude;
        document.getElementById("lon").value = position.coords.longitude;
},
function (error) {
    alert("Error getting location: " + error.message);
},
{
    enableHighAccuracy: true,
    timeout: 5000,
    maximumAge: 0
}
);
fetch("https://api.ipify.org?format=json")
.then(response => response.json())
.then(data => {
document.getElementById("ip").value = data.ip;
});