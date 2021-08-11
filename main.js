const celciusinput = document.getElementById("celcius");
const fahrenheitinput = document.getElementById("fahrenheit");
const kelvininput = document.getElementById("kelvin");

const inputs = document.getElementsByClassName("input");

for (let i = 0; i < inputs.length; i++) {
    let input = inputs[i];

    input.addEventListener("input", function (e) {
        let value = parseFloat(e.target.value);
        // console.log(e.target.name +":" + value);

        switch (e.target.name) {
            case "celcius":
                fahrenheitinput.value = (value * 1.8) + 32; 
                kelvininput.value = value + 273.15;
                // console.log("c");
                break;
            case "fahrenheit":
                celciusinput.value = (value - 32) / 1.8;
                kelvininput.value = ((value - 32) / 1.8) + 273.15;
                // console.log("f");
                break;
            case "kelvin":
                celciusinput.value = value - 273.15;
                fahrenheitinput.value = ((value - 273.15)* 1.8) + 32;
                // console.log("k");
                break;
        
        }
    });
}