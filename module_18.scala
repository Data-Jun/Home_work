object StringProcessor {
  // Функция для обработки строк
  def processStrings(strings: List[String]): List[String] = {
    // В данной функции вместо цикла и условия используем filter для выбора строк длиной
    // больше 3 и map для преобразования их в верхний регистр.
    strings.filter(_.length > 3).map(_.toUpperCase)
  }

  def main(args: Array[String]): Unit = {
    val strings = List("apple", "cat", "banana", "dog", "elephant")
    val processedStrings = processStrings(strings)
    println(s"Processed strings: $processedStrings")
  }
}