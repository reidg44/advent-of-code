package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	var pos_0 []int
	var pos_1 []int
	var pos_2 []int
	var pos_3 []int
	var pos_4 []int
	var pos_5 []int
	var pos_6 []int
	var pos_7 []int
	var pos_8 []int
	var pos_9 []int
	var pos_10 []int
	var pos_11 []int

	for scanner.Scan() {
		i := scanner.Text()

		fmt.Println(i)
	}
}
