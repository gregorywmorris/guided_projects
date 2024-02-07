error id: file://<WORKSPACE>/Scala-tutorial/main/src/scala/ObjectOrientation.scala:[805..806) in Input.VirtualFile("file://<WORKSPACE>/Scala-tutorial/main/src/scala/ObjectOrientation.scala", "package com.rockthejvm

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
    trait

}
")
file://<WORKSPACE>/Scala-tutorial/main/src/scala/ObjectOrientation.scala
file://<WORKSPACE>/Scala-tutorial/main/src/scala/ObjectOrientation.scala:35: error: expected identifier; obtained rbrace
}
^
#### Short summary: 

expected identifier; obtained rbrace