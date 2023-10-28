// Get references to the dropdowns and data display div
const dropdown1 = document.getElementById("dropdown1");
const dropdown2 = document.getElementById("dropdown2");
const dropdown3 = document.getElementById("dropdown3");
const dataDisplay = document.getElementById("dataDisplay");

// Define the data associated with the dropdown selections
const data = {
    "residential": {
      "lessthan":{
        "maharashtra":"residential lessthan maharashtra",
        "tamilnadu":"residential lessthan tamilnadu"
      },
      "greaterthan":{
        "maharashtra":"Data for residential more than maharashtra",
      }
    },
    "industrial": {
        "lessthan": "Data for industrial less than",
        "greaterthan": "Data for industrial-greater than"
    },
    "commercial": {
        "lessthan": "Data for commercial less than",
        "greaterthan": "Data for commercial greater than"
    }
    // Add more options as needed
  };

// Function to display the data based on the selections
function displayData() {
    const selectedOption1 = dropdown1.value;
    const selectedOption2 = dropdown2.value;
    const selectedOption3 = dropdown3.value;
  
    const dataKey = data[selectedOption1]?.[selectedOption2]?.[selectedOption3];
  
    dataDisplay.textContent = dataKey || "No data available";
  }
  
  // Event listeners for the dropdowns
  dropdown1.addEventListener("change", displayData);
  dropdown2.addEventListener("change", displayData);
  dropdown3.addEventListener("change", displayData);