function getRoomsValue() {
  var uiRooms = document.getElementsByName("uiRoom");
  for(var i in uiRooms) {
    if(uiRooms[i].checked) {
      console.log(uiRooms)
      console.log(parseInt(i)+1)
        return parseInt(i)+1;
    }
  }
  return -1;  // Invalid Value
}

function getSubTypeValue() {
  var uiSubType = document.getElementsByName("uiSubType");
  for(var i in uiSubType) {
    if(uiSubType[i].checked) {
      console.log(uiSubType)
      console.log(parseInt(i)+1)
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}




function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  content = {
    house_year : parseInt(document.getElementById("uiYearBuilt").value),
    dist_to_subway : parseFloat(document.getElementById("uiDistSub").value),
    footage : parseFloat(document.getElementById("uiFootage").value),
    floor : parseInt(document.getElementById("uiFloor").value),
    max_floor : parseInt(document.getElementById("uiMaxFloor").value),
    dist_to_center : parseFloat(document.getElementById("uiDistCenter").value),
    rooms : getRoomsValue(),
    subway_type : getSubTypeValue(),
    material : document.getElementById("uiMaterials").value,
    area : document.getElementById("uiAreas").value,
  }
  console.table(content)
  var est_price = document.getElementById("uiEstimatedPrice");

  var url = "http://127.0.0.1:5000/predict_home_price"; // local server

  $.post(url, content,
    function(data, status) {
      console.log(data.estimated_price);
      est_price.innerHTML = "<h2>" + data.estimated_price.toString() + " руб.</h2>";
      console.log(status);
  });
}

function onPageLoad() {
  console.log( "document loaded" );
  var url = "http://127.0.0.1:5000/get_categories_names"; // local server
  $.get(url,function(data, status) {
      console.log("got response for get_categories_names request");
      if(data) {
          var areas = data.areas;
          var uiAreas = document.getElementById("uiAreas");
          $('#uiAreas').empty();
          for(var i in areas) {
              var opt = new Option(areas[i]);
              $('#uiAreas').append(opt);
          }
          var materials = data.materials;
          var uiMaterials = document.getElementById("uiMaterials");
          $('#uiMaterials').empty();
          for(var i in materials) {
              var opt = new Option(materials[i]);
              $('#uiMaterials').append(opt);
          }
      }
  });
}

window.onload = onPageLoad;