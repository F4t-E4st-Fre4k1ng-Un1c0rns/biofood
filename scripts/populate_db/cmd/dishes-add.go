package main

import (
	db "RandomPopulate/internal/database"
	"context"
	"fmt"

	"github.com/google/uuid"
	"github.com/jackc/pgx/v5"
)

func main() {
	var allDishesInsideCategories [][]string
	var allDishBanners []string
	var allDishes []*db.Dish
	var allCategories []string
	var categoriesIds []uuid.UUID

	allDishesInsideCategories = db.GetDishes()
	allDishBanners = db.GetBannerPaths()
	allCategories = db.GetDishCategories()
	categoriesIds = db.GenerateDishCategoriesUUID(allCategories)

	var conn *pgx.Conn
	conn = db.MakeConnection(conn)
	fmt.Println("Adding categories...")
	for i := range allCategories {
		db.AddCategory(conn, allCategories[i], categoriesIds[i])
	}

	fmt.Println("Adding every dish from the menu...")
	counter := 0
	for i, categories := range allDishesInsideCategories {
		for _, dishName := range categories {
			categoryId := categoriesIds[i]
			dish := db.NewDish(dishName, 1000.0, categoryId, allDishBanners[counter])
			allDishes = append(allDishes, dish)
			counter++
		}
	}

	for _, dish := range allDishes {
		db.AddDish(conn, dish)
	}

	conn.Close(context.Background())
	fmt.Println("Done!")
}
