$(document).ready(function(){

    $.ajax({
      dataType: "json",
      url: "http://www.youknownothing.fyi/api/houses",
      success: function(data){
        var map = {};
        var houses = data.houses;
        var count = 0;
        for (var i = 0; i < houses.length; i++){
          if(map[houses[i].region] == null)
          {
            map[houses[i].region] = 1;
          }
          else
          {
            map[houses[i].region]++;
          }
        }
        console.log(map);
        createChart(map);
      }
    });


      function createChart(dataset){

      var width = 360;
      var height = 360;
      var radius = Math.min(width, height) / 2;
      var color = d3.scaleOrdinal(d3.schemeCategory20b);

      var svg = d3.select('#chart')
        .append('svg')
        .attr('width', width)
        .attr('height', height)
        .append('g')
        .attr('transform', 'translate(' + (width / 2) +  ',' + (height / 2) + ')');

        var arc = d3.arc()
        .innerRadius(0)
        .outerRadius(radius);

        var pie = d3.pie()
        .value(function(d){ return d.count; })
        .sort(null);

        var path = svg.selectAll('path')
          .data(pie(dataset))
          .enter()
          .append('path')
          .attr('d', arc)
          .attr('fill', function(d, i) {
            return color(d.data.label);
          });

          window.d3;
       }   

        
    });