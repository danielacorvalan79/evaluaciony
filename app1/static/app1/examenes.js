console.log("examenes js cargados") 
function formateDate(string) {
    var info = string.split('-').reverse().join('/');
    return info;
}
//MODAL HEMOGRAMA
function nuevo_hemograma() {
    var fecha = document.getElementById("fecha");
    var nueva_fecha = formateDate(fecha.value);
    console.log(fecha)
    var hematocrito_valor = document.getElementById("hematocrito");
    var hemoglobina_valor = document.getElementById("hemoglobina");

    console.log("Fecha: " + nueva_fecha);
    console.log("Hematocrito: " + hematocrito_valor.value);
    console.log("Hemoglobina: " + hemoglobina_valor.value);

    var fila_nueva = "<tr><td>" + nueva_fecha + "</td><td>" + hematocrito_valor.value + "</td><td>" + hemoglobina_valor.value + "</td></tr>";
    console.log(fila_nueva);
    var btn = document.createElement("tr");
    btn.innerHTML = fila_nueva;
    console.log("btn: ", btn);
    document.getElementById("tabla_hemograma").appendChild(btn);
}


function nuevo_perfill() {
    var fecha1 = document.getElementById("fecha1");
    var nueva_fecha1 = formateDate(fecha1.value);
    console.log(fecha1)
    var colesterol_valor = document.getElementById("colesterol");
    var trigliceridos_valor = document.getElementById("trigliceridos");

    console.log("Fecha: " + nueva_fecha1);
    console.log("Colesterol: " + colesterol_valor.value);
    console.log("Triglicéridos: " + trigliceridos_valor.value);

    var fila_nueva1 = "<tr><td>" + nueva_fecha1 + "</td><td>" + colesterol_valor.value + "</td><td>" + trigliceridos_valor.value + "</td></tr>";
    console.log(fila_nueva1);
    var btn1 = document.createElement("tr");
    btn1.innerHTML = fila_nueva1;
    console.log("btn: ", btn1);
    document.getElementById("tabla_perfill").appendChild(btn1);
}


function nuevo_perfilb() {
    var fecha = document.getElementById("fecha3");
    var nueva_fecha3 = formateDate(fecha3.value);
    console.log(fecha3)
    var glucosa_valor = document.getElementById("Glucosa");
    var bilirrubina_valor = document.getElementById("Bilirrubina");

    console.log("Fecha: " + nueva_fecha3);
    console.log("Glucosa: " + glucosa_valor.value);
    console.log("Bilirrubina: " + bilirrubina_valor.value);

    var fila_nueva3 = "<tr><td>" + nueva_fecha3 + "</td><td>" + glucosa_valor.value + "</td><td>" + bilirrubina_valor.value + "</td></tr>";
    console.log(fila_nueva3);
    var btn3 = document.createElement("tr");
    btn3.innerHTML = fila_nueva3;
    console.log("btn: ", btn3);
    document.getElementById("tabla_perfilb").appendChild(btn3);
}


var densityCanvas = document.getElementById("grafico_perfill");

Chart.defaults.global.defaultFontFamily = "Lato";
Chart.defaults.global.defaultFontSize = 13;

var densityData = {
    label: 'Valores P. lipídico 1',
    data: [1000, 1326, 687, 1271, 1638],
    backgroundColor: 'rgba(0, 99, 132, 0.6)',
    borderWidth: 0,
    yAxisID: "y-axis-density"
};

var gravityData = {
    label: 'Valores P. Lipídico 2',
    data: [3.7, 4.1, 9.0, 8.7, 11.0],
    backgroundColor: 'rgba(99, 132, 0, 0.6)',
    borderWidth: 0,
    yAxisID: "y-axis-gravity"
};



var chartOptions = {
    scales: {
        xAxes: [{
            barPercentage: 1,
            categoryPercentage: 0.6
        }],
        yAxes: [{
            id: "y-axis-density"
        }, {
            id: "y-axis-gravity"
        }]
    }
};

var barChart = new Chart(densityCanvas, {
    type: 'line',
    data: planetData,
    options: chartOptions
});



//Perfil bioquimico
var ctx = document.getElementById("grafico_perfilb");
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ["Group 1", "Group 2", "Group 3"],
        datasets: [{
            label: 'Perfil Bioquímico',
            data: [12, 5, 3]
        }]
    }
});

