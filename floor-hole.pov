#include "colors.inc"
#include "woods.inc"

background { color Cyan }

light_source {
  <2, 4, -3>
  color White
}

camera {
  location <0, 2, -3>
  look_at <0, 0, 2>
}

// difference {
//   box { <-3, -3, -3> <3, 0, 3> }
//   sphere {
//     <0, 1, 2> 2
//   }
//   texture {
//     pigment { color Yellow }
//   }
// }

// T_Wood1, T_Wood2, T_Wood8, T_Wood15, T_Wood19, T_Wood22, T_Wood27
// T_Wood19
  // cylinder {
  //   <0, -1, 0>, <0, 0, 0>, .25
  //   open
  //   translate n*x
  //   texture { tx rotate 90*x scale .5}
  // }

// julia_fractal {
//     <-0.083,0.0,-0.83,-0.025>
//     quaternion
//     sqr
//     max_iteration 8
//     precision 15
//   texture { T_Wood19 rotate 90*x scale .5}
// }

prism {
  quadratic_spline
  0, .25, 12,
  <-2, 1>,
  <-2, 0>, <-2, -1>, <-1, -1>, <-1, -2>, <1, -2>,
  <2, -2>, <1.5, -1>, <2, 0>, <0, 1>, <-2, 0>,
  <-1, -1>
  open
  texture { T_Wood19 rotate 90*x scale .5}
  scale .5
}
