package main

import (
	db "RandomPopulate/internal/database"
	"errors"
	"fmt"
	"math/rand"
	"os"
	"time"

	"github.com/google/uuid"
	"github.com/jackc/pgx/v5"
)

func randomAmount() int {
	roll := rand.Intn(100) + 1
	switch {
	case 1 <= roll && roll <= 80:
		return 1
	case 81 <= roll && roll <= 95:
		return 2
	case 96 <= roll && roll <= 100:
		return 3
	default:
		return 0
	}
}

func chooseRandomMeals(allDishes []uuid.UUID, amount int) []uuid.UUID {
	var output []uuid.UUID
	for range amount {
		dish := allDishes[rand.Intn(len(allDishes))]
		output = append(output, dish)
	}
	return output
}

func createTimeScope() (start time.Time) {
	halfYear, _ := time.ParseDuration("4380h")
	day, _ := time.ParseDuration("24h")
	end := time.Now().Truncate(day)
	start = end.Add(-halfYear)

	return
}

func randomDate(start time.Time) time.Time {
	// 183 is year divided by 2
	day, _ := time.ParseDuration("24h")
	randomDay := time.Duration(day * time.Duration(rand.Intn(183)))

	// working from 07:00 to 18:00
	randomHour := time.Hour * time.Duration((rand.Intn(12) + 7))
	randomSeconds := time.Second * time.Duration(rand.Intn(3600))
	output := start.Add(randomDay).Add(randomHour).Add(randomSeconds)

	return output
}

func randomDeviation(number int) int {
	output := -number + rand.Intn(2*number+1)
	return output
}

func main() {
	var ORDERS_PER_USER = 50
	var ORDER_DEVIATION = 3
	var FAVOURITE_FOODS = 3
	var FAVOURITE_DEVIATION = 1

	var allUsers, allDishes []uuid.UUID

	var conn *pgx.Conn
	conn = db.MakeConnection(conn)

	allUsers, err := db.ReadUserIds(conn)
	if errors.Is(err, pgx.ErrNoRows) {
		fmt.Println("Error: Database has no users")
		os.Exit(1)
	} else if err != nil {
		fmt.Printf("Database read failed with error: %v\n", err)
		os.Exit(1)
	}

	allDishes, err = db.ReadDishIds(conn)
	if errors.Is(err, pgx.ErrNoRows) {
		fmt.Println("Error: Database has no dishes")
		os.Exit(1)
	} else if err != nil {
		fmt.Printf("Database read failed with error: %v\n", err)
		os.Exit(1)
	}

	fmt.Println("Populating db with orders...")
	start := createTimeScope()
	for _, userId := range allUsers {
		orderAmount := ORDERS_PER_USER + randomDeviation(ORDER_DEVIATION)
		favouritesAmount := FAVOURITE_FOODS + randomDeviation(FAVOURITE_DEVIATION)

		favouriteDishes := chooseRandomMeals(allDishes, favouritesAmount)

		for range orderAmount {
			time := randomDate(start)
			amount := randomAmount()
			dishId := favouriteDishes[rand.Intn(len(favouriteDishes))]
			orderId := uuid.New()
			db.AddOrder(conn, userId, "taken", time, orderId)
			db.AddOrderItem(conn, orderId, dishId, amount)
		}
	}

	fmt.Println("Done!")
}
