error id: file://<WORKSPACE>/Scala-tutorial/main/src/scala/ObjectOrientation.scala:[543..544) in Input.VirtualFile("file://<WORKSPACE>/Scala-tutorial/main/src/scala/ObjectOrientation.scala", "package com.rockthejvm

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
    abstract class 

}
")
file://<WORKSPACE>/Scala-tutorial/main/src/scala/ObjectOrientation.scala
file://<WORKSPACE>/Scala-tutorial/main/src/scala/ObjectOrientation.scala:25: error: expected identifier; obtained rbrace
}
^
#### Short summary: 

expected identifier; obtained rbrace