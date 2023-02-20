package main

import (
	"fmt"
	"test/product"

	"github.com/gin-gonic/gin"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

type Product struct {
	gorm.Model
	Code  string `json:"Code"`
	Price uint   `json:"Price"`
}

func main() {

	dsn := "host=localhost user=youben password=123 dbname=gotest port=5432 sslmode=disable"
	db, err := gorm.Open(postgres.Open(dsn), &gorm.Config{})
	//Connection fails
	if err != nil {
		panic("failed to connect database")
	}

	app := gin.Default()

	// manually initialize imported packages
	product.Init(db, app)

	//Connection succeeds
	fmt.Print("Connection Successful !\n")

	app.Run(":8080")

}
