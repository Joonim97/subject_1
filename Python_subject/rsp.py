import random

def get_computer_choice():
    choices = ["가위", "바위", "보"]
    return random.choice(choices)

def winner(player, computer):
    if player == computer:
        return "무승부"
    elif (player == "가위" and computer == "보") or \
         (player == "바위" and computer == "가위") or \
         (player == "보" and computer == "바위"):
        return "승리"
    else:
        return "패배"

def rock_scissors_paper_game():
    win_count = 0
    lose_count = 0
    draw_count = 0

    while True:
        player_choice = input("가위, 바위, 보 중 하나를 입력하세요: ")
        if player_choice not in ["가위", "바위", "보"]:
            print("잘못된 입력입니다. 다시 입력하세요.")
            continue

        computer_choice = get_computer_choice()

        print(f"플레이어: {player_choice}, 컴퓨터: {computer_choice}")
        result = winner(player_choice, computer_choice)

        if result == "승리":
            win_count += 1
        elif result == "패배":
            lose_count += 1
        else:
            draw_count += 1

        print(f"이번 판은 {result}입니다.")

        play_again = input("다시 게임을 하시겠습니까? (y/n): ")
        if play_again == 'y':
            print ('다시 가보자고!')
            continue
        else :
            print("게임을 종료합니다. 통계를 출력합니다.")
            print(f"승리: {win_count}번, 패배: {lose_count}번, 무승부: {draw_count}번")
            break

if __name__ == "__main__":
    rock_scissors_paper_game()