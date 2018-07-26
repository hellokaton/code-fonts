package main

import (
	"fmt"
	"time"
)

func main() {

	// ------------- GOROUTINES -----------------
	for i := 0; i < 10; i++ {
		go count(i)
	}
	// wait for all go routines to finish execution
	time.Sleep(time.Millisecond * 11000)
}

func count(id int) {
	for i := 0; i < 10; i++ {
		fmt.Println(id, ":", i)
		time.Sleep(time.Millisecond * 1000)
	}
}
