$(document).ready(function () {



  $.ajax({
    dataType: "json",
    url: "http://www.youknownothing.fyi/api/houses",
    success: function(data){
      var map = {};
      var houses = data.houses;
      var patt =/^the /i;
        for (var i = 0; i < houses.length; i++){
          var s = houses[i].region.toLowerCase();
          console.log(s);
          console.log(patt.test(s));
          s = s.replace(patt,"");
          if(s.valueOf() == "-" || s.valueOf() == "none" || s.valueOf() == "unknown"){
            continue;
          }
          if(s.valueOf() =="vale of arryn"){
            s = "vale";
          }
          if(map[s] == null)
          {
            map[s] = 1;
          }
          else
          {
            map[s]++;
          }
        }


        console.log(map);
        var arr = [];
        Object.keys(map).forEach(function(key,index) {
        //console.log("Key = " + key + " Value= " + data[key]);
        var val = map[key];
        arr.push({
          text: key,
          count: val
        });
      })
        var arrSmall = [];

        function compare(a,b) {
          if (a.count > b.count){
            return -1;
          }
          if (a.count <= b.count){
            return 1;
          }
          return 0
        }

        arr.sort(compare);

        for(var i = 0; i < 10; i++)
        {
          arrSmall[i] = arr[i];
        }
        //console.log(arrSmall);
        createChart(arrSmall);
      }
    });


  function createChart(smallArray){

    //console.log(smallArray.length);
    var bubbleChart = new d3.svg.BubbleChart({
      supportResponsive: true,
    //container: => use @default
    size: 600,
    //viewBoxSize: => use @default
    innerRadius: 600 / 3.5,
    //outerRadius: => use @default
    radiusMin: 50,
    //radiusMax: use @default
    //intersectDelta: use @default
    //intersectInc: use @default
    //circleColor: use @default
    data: {
      items: smallArray,
      eval: function (item) {return item.count;},
      classed: function (item) {return item.text.split(" ").join("");}
    },
    plugins: [
    {
      name: "central-click",
      options: {
        style: {
          "font-size": "12px",
          "font-style": "italic",
          "font-family": "Source Sans Pro, sans-serif",
            //"font-weight": "700",
            "text-anchor": "middle",
            "fill": "white"
          },
          attr: {dy: "65px"},
          centralClick: function() {
          }
        }
      },
      {
        name: "lines",
        options: {
          format: [
            {// Line #0
              textField: "count",
              classed: {count: true},
              style: {
                "font-size": "28px",
                "font-family": "Source Sans Pro, sans-serif",
                "text-anchor": "middle",
                fill: "white"
              },
              attr: {
                dy: "0px",
                x: function (d) {return d.cx;},
                y: function (d) {return d.cy;}
              }
            },
            {// Line #1
              textField: "text",
              classed: {text: true},
              style: {
                "font-size": "14px",
                "font-family": "Source Sans Pro, sans-serif",
                "text-anchor": "middle",
                fill: "white"
              },
              attr: {
                dy: "20px",
                x: function (d) {return d.cx;},
                y: function (d) {return d.cy;}
              }
            }
            ],
            centralFormat: [
            {// Line #0
              style: {"font-size": "50px"},
              attr: {}
            },
            {// Line #1
              style: {"font-size": "30px"},
              attr: {dy: "40px"}
            }
            ]
          }
        }]
      });
}
});
