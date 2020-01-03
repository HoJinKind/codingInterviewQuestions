package main

import "fmt"

func main()  {
	sm:= specialMapInitialise()
	sm.set(1,10,1)
	fmt.Println(sm.get(2,1))
	fmt.Println(sm.get(1,1))
}


