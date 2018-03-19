$(document).ready( function() {        

	$("#flat-slider")
    .slider({
        max: 2020,
        min: 1000,
        range: true,
        step: 5,
        values: [1970, 2000],
        
    })
    .slider("pips", {
        first: "pip",
        last: "pip",
        rest: "label"
    });

    var $slider = $("#flat-slider"),
        $input = $("#from")
          min = 1000,
          max = 2020;

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
          min = 1000,
          max = 2020;

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