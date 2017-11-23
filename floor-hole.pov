#include "colors.inc"
#include "woods.inc"

#include "points.inc"

background { color <1, 0, 1> }

light_source {
  <2, 4, 3>
  color White
}

camera {
  location <0, 2.3, 4.3>
  look_at <0, 0, 0>
}

// T_Wood1, T_Wood2, T_Wood8, T_Wood15, T_Wood19, T_Wood22, T_Wood27
// T_Wood19

// #declare POINTS = array[12] {<-2, 1>,
// <-2, 0>, <-2, -1>, <-1, -1>, <-1, -2>, <1, -2>,
// <2, -2>, <1.5, -1>, <2, 0>, <0, 1>, <-2, 0>,
// <-1, -1>};

difference {
  plane {
    y, 0
    pigment { color White }
    finish { emission 1 }
  }
  prism {
    linear_spline
    -25, 1, dimension_size(POINTS, 1),
#declare I = 0;
#while (I < dimension_size(POINTS, 1))
    POINTS[I]
    #declare I = I + 1;
#end
    open
    scale .01
  }
  texture { T_Wood19 rotate 90*x scale .5}
}

#declare S = 3;

// intersection {
//   plane { y, -1 }
//   box { <-S, -2, -S>, <S, 1, S> }
//   pigment {
//     image_map {
//       png "space.png"
//       map_type 0
//     }
//     translate <.5, .5, 0>
//     rotate <90, 180, 0>
//     scale <2, 1, 12>
//   }
// //  rotate 45*x
//   translate <0, -2, -5>
//   scale 5*x
// }
