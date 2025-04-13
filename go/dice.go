package main

import ("fmt"
        "math/rand"
        "strconv"
)

func main() {
    r := rand.New(rand.NewSource(99))
    var dice int
    var user_input string
    for {
        fmt.Println("Let's throw dice together...")
        fmt.Println("How many faces this imaginary dice have?")
        fmt.Scan(&user_input)
        fmt.Println("Ok, so I throw a dice of", user_input, "faces and get:")
        if user_input == "exit" {
            break
        } else {
            faces, err := strconv.Atoi(user_input)
            if err != nil {
                fmt.Println("Error converting string to int!")
            } else {
                dice = r.Int()%faces + 1
                fmt.Println(dice)
            }
        }        
    }
}
