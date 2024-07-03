import random


def up_down_game():

    best_score = 99

    while True:
        random_number = random.randint(1, 100)
        attempts = 0
        print("1부터 100 사이의 숫자를 맞춰보세요!")

        while True:
            try:
                Input = int(input("숫자를 입력하세요: "))
                if Input < 1 or Input > 100:
                    print("유효한 범위 내의 숫자를 입력하세요.")
                    continue
            except ValueError:
                print("숫자를 입력해주세요.")
                continue

            attempts += 1

            if Input < random_number:
                print("업")
            elif Input > random_number:
                print("다운")
            else:
                print(f"정답입니다! {attempts}번 만에 맞췄어요.")
                if best_score is None or attempts < best_score:
                    best_score = attempts
                    print("최고 기록을 갱신했습니다!")
                else:
                    print(f"현재 최고 기록은 {best_score}번 입니다.")
                break

        Again = input("다시 하시겠습니까? (y/n): ")
        if Again == 'y':
            print("최고 기록 가보자고!")
            continue
        else:
            print("고생했습니다, 빠이!")
            break

if __name__ == "__main__":
    up_down_game()
