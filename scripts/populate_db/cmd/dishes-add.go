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
	for i, categories := range allDishesInsideCategories {
		for j, dishName := range categories {
			categoryId := categoriesIds[i]
			dish := db.NewDish(dishName, 1000.0, categoryId, allDishBanners[j])
			allDishes = append(allDishes, dish)
		}
	}

	for _, dish := range allDishes {
		db.AddDish(conn, dish)
	}

	conn.Close(context.Background())
	fmt.Println("Done!")
}
