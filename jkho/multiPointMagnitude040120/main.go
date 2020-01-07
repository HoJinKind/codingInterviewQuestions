package main

import (
	"fmt"
	"math"
)

//Good morning! Here's your coding interview problem for today.
//
//This problem was asked by Google.
//
//You are in an infinite 2D grid where you can move in any of the 8 directions:
//
//(x,y) to (x+1, y), (x - 1, y), (x, y+1), (x, y-1), (x-1, y-1), (x+1,y+1), (x-1,y+1), (x+1,y-1)
//
//You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.
//
//Example:
//
//Input: [(0, 0), (1, 1), (1, 2)] Output: 2
//
//It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).

func main() {
	//point1 := intitalisePoint(1,1)
	//point2 := intitalisePoint(10,10)
	//fmt.Println(calcMagnitude(point1,point2))
	test := [][]int{{0, 0}, {1, 5}, {0, -10}}
	//test = append(test, []int{1,2})
	fmt.Println(fmt.Sprint("The minimum step is : ", minimumSteps(test)))
}

func minimumSteps(arrayls [][]int) int {
	magnitude := 0
	for index := range arrayls {
		if index != len(arrayls)-1 {
			magnitude += calcMagnitude(arrayls[index], arrayls[index+1])
		}
	}
	return magnitude
}

func calcMagnitude(point1 point, point2 point) int {
	vectorPoint := intitalisePoint(point1[0]-point2[0], point1[1]-point2[1])

	return int(math.Max(math.Abs(float64(vectorPoint[0])), math.Abs(float64(vectorPoint[1]))))
}
