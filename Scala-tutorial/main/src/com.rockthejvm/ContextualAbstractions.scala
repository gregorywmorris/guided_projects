package com.rockthejvm

object ContextualAbstractions {

    val aList = List(2,1,3,4)
    val anOrderedList = aList.sorted // contextual argument: (descendingOrdering)

    // Ordering
    given descendingOrdering: Ordering[Int] = Ordering.fromLessThan(_ > _) // (a,b) => a > b, given will reverse all sorted

    // analogous to an implicit val

    trait Combinator[A] {
    def combine(x: A, y: A): A
    }

    // using makes it a contextual argument
    def combineAll[A](list: List[A])(using combinator: Combinator[A]): A =
        list.reduce((a,b) => combinator.combine(a,b))

    given intCombinator: Combinator[Int] = new Combinator[Int] {
        override def combine(x: Int, y: Int) = x + y
    }

    val theSum = combineAll(aList) // (intCombinator)

    def main(args: Array[String]): Unit = {
        println(anOrderedList)
        println(theSum)
    }

}
