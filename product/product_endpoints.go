package product

import (
    "github.com/gin-gonic/gin"
    "gorm.io/gorm"
)

var db *gorm.DB

type Product struct {
    gorm.Model
    Code  string
    Price uint
}

func Init(gormdb *gorm.DB, r *gin.Engine) {
    db = gormdb // set package global

    db.AutoMigrate(&Product{})

    r.GET("/products", get)
}

func get(c *gin.Context) {

    var product Product
    db.First(&product, 1)

    c.JSON(200, gin.H{
        "product": product,
    })
}