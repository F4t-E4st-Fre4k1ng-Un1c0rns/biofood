package database

import (
	cryptoRand "crypto/rand"
	"encoding/base64"
	"fmt"
	"math/rand"
	"time"

	"github.com/google/uuid"
	"golang.org/x/crypto/argon2"
)

type User struct {
	Role     string
	Email    string
	Password string
}

type Dish struct {
	Name         string
	BannerPath   string
	Price        float32
	Description  string
	Weight       int
	CategoryUUID uuid.UUID
}

type Order struct {
	UserId      uuid.UUID
	Status      string
	TakeoutTime time.Time
	Id          uuid.UUID
}

func NewOrder(userId uuid.UUID, status string, takeoutTime time.Time, id uuid.UUID) *Order {
	return &Order{
		UserId:      userId,
		Status:      status,
		TakeoutTime: takeoutTime,
		Id:          id,
	}
}

func generateRandomBytes(n int) []byte {
	b := make([]byte, n)
	_, err := cryptoRand.Read(b)
	if err != nil {
		return nil
	}
	return b
}

func MakePassword() string {
	/*
		code shamelessly stolen from
		https://www.alexedwards.net/blog/how-to-hash-and-verify-passwords-with-argon2-in-go
	*/

	salt := generateRandomBytes(12)
	password := generateRandomBytes(rand.Intn(13) + 8)

	var iterations, memory, parallelism, keyLength = uint32(3), uint32(64 * 1024), uint8(2), uint32(8)
	hash := argon2.IDKey(password, salt, iterations, memory, parallelism, keyLength)

	b64Salt := base64.RawStdEncoding.EncodeToString(salt)
	b64Hash := base64.RawStdEncoding.EncodeToString(hash)

	encodedHash := fmt.Sprintf(
		"$argon2id$v=%d$m=%d,t=%d,p=%d$%s$%s",
		argon2.Version,
		memory,
		iterations,
		parallelism,
		b64Salt,
		b64Hash,
	)
	return encodedHash
}

func appendEmail(name string, mails []string) string {
	mailIndex := rand.Intn(len(mails))
	return fmt.Sprintf("%v@%v", name, mails[mailIndex])
}

func makeFullName(firstNames []string, secondNames []string, firstFemale int) string {
	firstIndex := rand.Intn(len(firstNames))
	secondIndex := rand.Intn(len(secondNames))
	fullName := fmt.Sprintf("%v%v", firstNames[firstIndex], secondNames[secondIndex])
	if firstIndex >= firstFemale {
		fullName += "a"
	}

	return fullName
}

func MakeEmail(firstNames []string, secondNames []string, firstFemale int, mails []string) string {
	name := makeFullName(firstNames, secondNames, firstFemale)
	return appendEmail(name, mails)
}

func GenerateDishCategoriesUUID(categories []string) []uuid.UUID {
	var output []uuid.UUID
	for range len(categories) {
		output = append(output, uuid.New())
	}
	return output
}

func NewUser(role string, email string, password string) *User {
	return &User{
		Role:     role,
		Email:    email,
		Password: password,
	}
}

func NewDish(name string, price float32, categoryId uuid.UUID, banner string) *Dish {
	// fill only NOT NULL fields
	return &Dish{
		Name:         name,
		Price:        price,
		CategoryUUID: categoryId,
		BannerPath:   banner,
	}
}
