export default class Marker {

	static closePopup(){
		document.getElementsByClassName('popup')[0].style.display = 'none';
	}

	static addMarker(x, y, type, name, description, datetime, timelenght, nolimit){
		if(nolimit){
			datetime = "infinity"
			timelenght = ""
		}else{
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
					"time": timelenght,
					"rating": 100
				});
				xhr.send(data);
			}else{
				alert("Заполните все поля");
				
			}
		}
	}
}