// //> using scala "2.13.10"
// //> using dep "com.lihaoyi::pprint::0.8.1"

package com.rockthejvm

object basics extends App {
    // define a value
    // Int, Boolean, Char, Double, Float, String <- notice start with caps
    val meaningOfLife: Int = 42 // values are constants, immutable
    val aBoolean = false // type is optional, some exceptions
    val aString = "I love Scala!"
    val aComposedString = "I"+" "+"love"+" "+"Scala!"
    val anInterpolatedString = s"The meaning of life is $meaningOfLife" //formatted string, "$" to import var

    //expressions
    val anExpression = 2+3
    var ifExpression = if (meaningOfLife >43) 56 else 999
    var chainExpression = 
        if (meaningOfLife > 43) 56
        else if (meaningOfLife < 0) -2
        else if (meaningOfLife >999) 78
        else 0

    // code block
    val aCodeBlock = {
        val aLocalValue = 67
        // last expression is the return value
        aLocalValue + 3
    }

    //functions
    def myFunction(x: Int, y: String): String = {
        y + " "+x
    }

    def factorial(n: Int): Int =
        if (n<= 1) 1
        else n * factorial(n-1)
    
    // In Scala we don't use loops or iterations, we use RECURSION!

    // the Unit type == void

    def myUnitReturningFunction(): Unit = {
        println("I don't love returning Unit")
    }

    val theUnit = ()

    println(anInterpolatedString)
    println(aCodeBlock)
    println(factorial(5))
    println(myUnitReturningFunction())
}