"""Определяет операцию для расчёта вероятности событий."""

QUESTION_SIMULTANEOUS: str = (
    "События могут произойти одновременно? (да/нет)\n"
    "Пример: выпадение орла И четного числа на кубике\n"
    "Ваш ответ: "
)

EXAMPLE_MULTIPLICATION: str = (
    "Пример: P(орел и четное) = P(орел) × P(четное) = 1/2 × 1/2 = 1/4"
)

EXAMPLE_ADDITION: str = "Пример:P(орел или решка)=P(о) + P(р) = 1/2+1/2 = 1"

while True:
    print("\nОпределитель операции для расчёта вероятности\n")

    if input(QUESTION_SIMULTANEOUS).lower().strip() == "да":
        print("\nИспользуйте умножение вероятностей: P(A и B) = P(A) × P(B)")
        print(EXAMPLE_MULTIPLICATION)

    else:
        print("\nИспользуйте сложение вероятностей: P(A или B) = P(A) + P(B)")
        print(EXAMPLE_ADDITION)

    if input("\nХотите продолжить? (да/нет): ").lower().strip() != "да":
        print("\nСпасибо за использование программы!")
        break
