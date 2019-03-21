// from data.js
var tableData = data;
// var csvData = 'distinct_apps_no_null_or_duplicate_reviews_merged_df.csv';
var csvLoaded = d3.csv(
  'distinct_apps_no_null_or_duplicate_reviews_merged_df.csv',
  function(data) {
    console.log(data[0]);
    console.log(data[1]);
    console.log(data[2]);
  }
);

/*
var file = document.getElementById('file');
if (file){
    console.log("Getting file...")
    file.addEventListener('change', function() {
        var reader = new FileReader();
        console.log(file)
        var f = file.files[0];
        reader.onload = function(e) {
            var CSVARRAY = parseResult(e.target.result); //this is where the csv array will be
        };
        reader.readAsText(f);
    })
};


function parseResult(result) {
    var resultArray = [];
    result.split("\n").forEach(function(row) {
        var rowArray = [];
        row.split(",").forEach(function(cell) {
            rowArray.push(cell);
        });
        resultArray.push(rowArray);
    });
    return resultArray;
}
*/

// var csv is the CSV file with headers
// function csvJSON(csv){

// var lines=csv.split("\n");
// var result = [];
// var headers=lines[0].split(",");

// for(var i=1;i<lines.length;i++){
// var obj = {};
// var currentline=lines[i].split(",");
// for(var j=0;j<headers.length;j++){
// obj[headers[j]] = currentline[j];
// }
// result.push(obj);
// }
// return result; //JavaScript object
// console.log(JSON.stringify(result));
// return JSON.stringify(result); //JSON
// }

// get table references
var tbody = d3.select('tbody');

function buildTable(data) {
  // First, clear out any existing data
  console.log('Loading data....');
  tbody.html('');

  // Next, loop through each object in the data
  // and append a row and cells for each value in the row
  data.forEach(dataRow => {
    // Append a row to the table body
    var row = tbody.append('tr');

    // Loop through each field in the dataRow and add
    // each value as a table cell (td)
    Object.values(dataRow).forEach(val => {
      var cell = row.append('td');
      cell.text(val);
    });
  });
  console.log('Finished loading!');
}

// Keep Track of all filters
var filters = {};

function updateFilters() {
  // Save the element, value, and id of the filter that was changed
  var changedElement = d3.select(this).select('input');
  var elementValue = changedElement.property('value');
  var filterId = changedElement.attr('id');

  // If a filter value was entered then add that filterId and value
  // to the filters list. Otherwise, clear that filter from the filters object
  if (elementValue) {
    filters[filterId] = elementValue;
  } else {
    delete filters[filterId];
  }

  // Call function to apply all filters and rebuild the table
  filterTable();
}

function filterTable() {
  // Set the filteredData to the tableData
  let filteredData = tableData;

  // Loop through all of the filters and keep any data that
  // matches the filter values
  Object.entries(filters).forEach(([key, value]) => {
    filteredData = filteredData.filter(row => row[key] === value);
  });

  // Finally, rebuild the table using the filtered Data
  buildTable(filteredData);
}

// Attach an event to listen for changes to each filter
d3.selectAll('.filter').on('change', updateFilters);

// Build the table when the page loads
buildTable(tableData);

// Build the table when the page loads
// buildTable(csvJSON(csvData));

// buildTable(csvLoaded);
