// Import input.txt file and iterate over each line
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	defer file.Close()

	prev_val := 0
	curr_count := 0
	count_more_than_prev := 0

	prev_2_val := 0
	triple_prev_val := 0
	triple_count_more_than_prev := 0

	// Iterate over each line
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {

		i, err := strconv.Atoi(scanner.Text())
		if err != nil {
			fmt.Println(err)
			os.Exit(1)
		}
		// If curr_count is not 0
		if curr_count != 0 {
			if i > prev_val {
				count_more_than_prev += 1
			}
		}
		if curr_count == 2 {
			triple_prev_val = prev_2_val + prev_val + i
		} else if curr_count > 2 {
			triple_sum := prev_2_val + prev_val + i
			if triple_sum > triple_prev_val {
				triple_count_more_than_prev += 1
			}
			triple_prev_val = triple_sum
		}
		curr_count += 1
		prev_2_val = prev_val
		prev_val = i

	}

	// Print sum
	fmt.Println("Answer 1 is: " + strconv.Itoa(count_more_than_prev))
	fmt.Println("Answer 2 is: " + strconv.Itoa(triple_count_more_than_prev))
}
