package database

import (
	"context"
	"fmt"
	"os"
	"time"

	"github.com/google/uuid"
	"github.com/jackc/pgx/v5"
	"github.com/joho/godotenv"
)

func MakeConnection(conn *pgx.Conn) *pgx.Conn {
	if conn != nil {
		return conn
	}

	err := godotenv.Load()
	if err != nil {
		fmt.Printf(".env file not found")
		os.Exit(1)
	}

	conn_string, exists := os.LookupEnv("DATABASE_CONNECTION_STRING")
	if !exists {
		fmt.Printf("The DATABASE_CONNECTION_STRING .env variable doesn't exist")
		os.Exit(1)
	}

	conn, err = pgx.Connect(context.Background(), conn_string)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Unable to connect to database: %v\n", err)
		os.Exit(1)
	}

	return conn
}

func warn(err error) {
	fmt.Fprintf(os.Stderr, "WARNING: Query execution skipped: %v\n", err)
}

func AddUser(conn *pgx.Conn, user *User) {
	id := uuid.New()
	_, err := conn.Exec(
		context.Background(),
		"INSERT INTO public.users (email, id, role) VALUES ($1, $2, $3)",
		user.Email, id, "client",
	)
	if err != nil {
		warn(err)
	}
}

func AddDish(conn *pgx.Conn, dish *Dish) {
	id := uuid.New()
	_, err := conn.Exec(
		context.Background(),
		"INSERT INTO public.dishes (name, \"bannerPath\", id, price, \"categoryId\") VALUES ($1, $2, $3, $4, $5)",
		dish.Name, dish.BannerPath, id, dish.Price, dish.CategoryUUID,
	)
	if err != nil {
		warn(err)
	}
}

func AddCategory(conn *pgx.Conn, name string, id uuid.UUID) {
	_, err := conn.Exec(
		context.Background(),
		"INSERT INTO public.categories (name, id) VALUES ($1, $2)",
		name, id,
	)
	if err != nil {
		warn(err)
	}
}

func KillThemAll(conn *pgx.Conn) {
	_, err := conn.Exec(
		context.Background(),
		"TRUNCATE TABLE users, dishes, categories, orders CASCADE",
	)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Something went wrong: %v\n", err)
		os.Exit(1)
	}
}

func ReadUserIds(conn *pgx.Conn) ([]uuid.UUID, error) {
	rows, err := conn.Query(
		context.Background(),
		"SELECT id FROM users",
	)
	if err != nil {
		return []uuid.UUID{}, err
	}

	ids, err := pgx.CollectRows(rows, pgx.RowTo[uuid.UUID])

	return ids, err
}

func ReadDishIds(conn *pgx.Conn) ([]uuid.UUID, error) {
	rows, err := conn.Query(
		context.Background(),
		"SELECT id FROM dishes",
	)
	if err != nil {
		return []uuid.UUID{}, err
	}

	ids, err := pgx.CollectRows(rows, pgx.RowTo[uuid.UUID])

	return ids, err
}

func AddOrder(conn *pgx.Conn, userId uuid.UUID, status string, takeoutTime time.Time, orderId uuid.UUID) {
	_, err := conn.Exec(
		context.Background(),
		"INSERT INTO public.orders (\"userId\", status, \"takeoutTime\", id) VALUES ($1, $2, $3, $4)",
		userId, status, takeoutTime, orderId,
	)
	if err != nil {
		warn(err)
	}
}

func AddOrderItem(conn *pgx.Conn, orderId uuid.UUID, dishId uuid.UUID, amount int) {
	id := uuid.New()
	_, err := conn.Exec(
		context.Background(),
		"INSERT INTO public.\"orderItems\" (\"orderId\", \"dishId\", amount, id) VALUES ($1, $2, $3, $4)",
		orderId, dishId, amount, id,
	)
	if err != nil {
		warn(err)
	}
}
