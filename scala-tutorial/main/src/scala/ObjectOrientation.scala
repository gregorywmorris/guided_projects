package com.rockthejvm

//All fields and methods are public by default
// private = only the class has access
//protected = the class and descendants

object ObjectOrientation {
    
    class Animal {
        val age: Int = 0
        def eat() = println("I am eating")
    }

    val anAnimal = new Animal
    // without val, you cannot call name by Dog.name
    class Dog(val name: String) extends Animal {
        def bark() = println("Woof")
    }
    val aDog = new Dog("Lassie")

    println(aDog.bark())

    val aDeclaredAnimal: Animal = new Dog("Fido")
    aDeclaredAnimal.eat() //method called at runtime not compile

    //abstract class
    abstract class WalkingAnimal {
        protected val hasLegs = true
        def walk(): Unit
    }

    //interface = ultimate abstract type
    trait Carnivore {
        def eat (animal: Animal): Unit
    }

    trait Philosopher {
        def ?!(thought: String): Unit // ?! is a valid method name
    }

    class Crocodile extends Animal with Carnivore with Philosopher {
        override def eat(animal: Animal): Unit = println(s"I am eating you $animal!")

        def ?!(thought: String): Unit = println("I think there for I am")
    }

    val aCroc = new Crocodile
    aCroc.eat(aDog)
    aCroc eat aDog //infix notation  = object method argument, only available with ONE argument

}
