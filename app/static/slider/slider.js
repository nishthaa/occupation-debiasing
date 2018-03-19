$(document).ready( function() {        

	$("#flat-slider")
    .slider({
        max: 50,
        min: 0,
        range: true,
        values: [15, 35],
        
    })
    .slider("pips", {
        first: "pip",
        last: "pip",
        rest: "label"
    });

    var $slider = $("#flat-slider"),
        $input = $("#from")
          min = 0,
          max = 50;

      $input.on("change", function(e) {
      
        var num = parseFloat( $input.val() ),
            isProblem = false;
      
        if ( num === num ) {
          
          if ( num < min ) {
            num = min;
          } else if ( num > max ) {
            num = max;
          }
      
          $slider.slider("value", num );
            $input.val( num );

        } else {
      
          alert( "should be a number" );
      
        }
      
      });
      
      $slider.on("slide", function(e,ui) {
        $input.val( ui.values[0] );
      
      });

        $input2 = $("#to")
          min = 0,
          max = 50;

      $input2.on("change", function(e) {
      
        var num = parseFloat( $input2.val() ),
            isProblem = false;
      
        if ( num === num ) {
          
          if ( num < min ) {
            num = min;
          } else if ( num > max ) {
            num = max;
          }
      
          $slider.slider("value", num );
            $input2.val( num );
      
        } else {
      
          alert( "should be a number" );
      
        }
      
      });
      
      $slider.on("slide", function(e,ui) {
        $input2.val( ui.values[1] );
      
      });







}); // document.ready