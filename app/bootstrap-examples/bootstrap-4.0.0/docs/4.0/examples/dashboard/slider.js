$(document).ready(function(){
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
});
