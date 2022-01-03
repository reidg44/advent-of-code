package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	defer file.Close()

	vert_pos := 0
	hor_pos := 0

	vert_pos_2 := 0
	aim := 0

	// Iterate over each line
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {

		i := scanner.Text()

		if strings.HasPrefix(i, "forward") {
			num := get_num(i, "forward ")
			hor_pos += num
			vert_pos_2 += num * aim
		} else if strings.HasPrefix(i, "down") {
			num := get_num(i, "down ")
			vert_pos += num
			aim += num
		} else if strings.HasPrefix(i, "up") {
			num := get_num(i, "up ")
			vert_pos -= num
			aim -= num
		}
	}
	fmt.Println(vert_pos * hor_pos)
	fmt.Println(vert_pos_2 * hor_pos)
}

func get_num(s string, p string) int {
	num, err := strconv.Atoi(strings.TrimPrefix(s, p))
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	return num
}
