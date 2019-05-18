export default class Marker {

	static closePopup(){
		document.getElementsByClassName('popup')[0].style.display = 'none';
	}
	static addMarker(x, y, type, name, description, datetime){
		if (document.getElementById('name').value && document.getElementById('about').value){
			var xhr = new XMLHttpRequest();
			var url = "http://90.189.168.29:13452/set_point";
			xhr.open("POST", url, true);
			xhr.setRequestHeader("Content-Type", "application/json");
			var data = JSON.stringify({
				"x": x,
				"y": y,
				"type": type,
				"name": name,
				"description": description,
				"datetime": datetime,
				"time": "",
				"rating": 100
			});
			xhr.send(data);
			if (xhr.status != 200) {
				alert( xhr.status + ': ' + xhr.statusText + "Проверьте правильность введеных данных" );
			} else {
				alert( xhr.responseText); 
				addStaticMarker(document.getElementById('location').value,document.getElementById('map').value)

			}

		}else{
			alert("Заполните все поля");
			
		}

	}
}