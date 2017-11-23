#include "colors.inc"
#include "woods.inc"

background { color Cyan }

light_source {
  <2, 4, -3>
  color White
}

camera {
  location <0, 2.3, -4.3>
  look_at <0, 0, 0>
}

// T_Wood1, T_Wood2, T_Wood8, T_Wood15, T_Wood19, T_Wood22, T_Wood27
// T_Wood19

difference {
  plane {
    y, 0
    pigment { color White }
    finish { emission 1 }
  }
  prism {
    quadratic_spline
    -.25, .25, 12,
    <-2, 1>,
    <-2, 0>, <-2, -1>, <-1, -1>, <-1, -2>, <1, -2>,
    <2, -2>, <1.5, -1>, <2, 0>, <0, 1>, <-2, 0>,
    <-1, -1>
    open
  }
//  box { <-2.1, -1, .1>, <-1.9, -.1, -1.1> }
  // mesh {
  //   triangle { <0, 0, 0>, <-2, -.1, 0>, <-2, -.1, -1> }
  // }
  texture { T_Wood19 rotate 90*x scale .5}
}

// mesh {
//   triangle { <0, 0, 0>, <1, 1, 1>, <1, 1, 0> }
//   triangle { <0, 0, 0>, <0, 1, 0>, <1, 0, 1> }
//   texture { T_Wood19 rotate 90*x scale .5}
// }
