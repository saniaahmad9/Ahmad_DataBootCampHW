// // YOUR CODE HERE!


var tableData = data;

tbody = d3.select("tbody")


function displayData(data){ 
    tbody.text("")
    data.forEach(function(sighting){
    new_tr = tbody.append("tr")
    Object.entries(sighting).forEach(function([key, value]){
        new_td = new_tr.append("td").text(value)	
    })
})}

displayData(tableData)

var inputText = d3.select("#datetime")
var button = d3.select("filter-btn")

function changeHandler(){
    d3.event.preventDefault();
    console.log(inputText.property("value"));
    var new_table = tableData.filter(sighting => sighting.datetime===inputText.property("value"))
    displayData(new_table)
}

inputText.on("change", changeHandler)
button.on("click", changeHandler)
