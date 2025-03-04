package main

import (
	db "RandomPopulate/internal/database"
	"context"
	"fmt"

	"github.com/jackc/pgx/v5"
)

func generateRandomUser(email string) *db.User {
	return db.NewUser("client", email, "аргоны считать долга поэтому плейсхолдер")
}

func main() {
	var firstNames, secondNames, mails []string
	var users []db.User
	fullNameSet := make(map[string]bool) // set is to prevent duplicates

	// first female name is 26th
	firstNames = db.GetFirstNames()
	secondNames = db.GetSecondNames()
	mails = db.GetMails()

	fmt.Println("How many users would you like to add to the database?")
	var userAmount int
	fmt.Scanln(&userAmount)
	for len(fullNameSet) < userAmount {
		newEmail := db.MakeEmail(firstNames, secondNames, 26, mails)
		fullNameSet[newEmail] = true
	}

	var conn *pgx.Conn
	conn = db.MakeConnection(conn)
	for email := range fullNameSet {
		user := generateRandomUser(email)
		users = append(users, *user)
		db.AddUser(conn, user)
	}

	conn.Close(context.Background())
}
