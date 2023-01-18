import random

pre_userList = ['혜원', '성일', '민지', '창진']

user_info = {}
final_userList = []
limit_list = [2, 4, 6, 8, 10]
friend_num = 0

userName = input('이름이 뭐에요? : ')

print(userName)
print("===========소주기준 당신의 주량은?=============")
print("1. 소주 0.5병(2잔)")
print('2. 소주 0.5~1병(4잔)')
print('3. 소주 1~1.5병(6잔)')
print('4. 소주 1.5~2병(8잔)')
print('5. 소주 2병 이상(10잔)')
print("==============================================")

while 1:
    try:
        limit = int(input('당신의 치사량(주량은) 어느정도인가요?(1~5 사이 선택!):'))
        if not 1 <= limit <= 5: raise Exception

    except:
        print('1~5사이 정수를 입력해주세여..')
    else:
        print("{}님 당신의 치사량은 {}잔으로 입력하셨습니다!".format(userName, limit_list[limit - 1]))
        user_info['name'] = userName
        user_info['limit'] = limit_list[limit - 1]
        final_userList.append(user_info)
        print(final_userList)
        break

while True:
    try:
        friend_num = int(input('함께 취할 친구들은 얼마나 필요하나요? 최대 3명 입니다: '))
        if not 1 <= limit <= 3: raise Exception

    except:
        print('1~3사이 정수를 입력해주세여..')
    else:

        user_select_list = []
        for i in range(friend_num):
            x = random.randint(1, friend_num)
            # user는 여러명 중복해서 선택하면 안되니까 중복이면 다시 뽑기
            while x in user_select_list:
                x = random.randint(1, friend_num)
            user_select_list.append(x)
            l = limit_list[random.randint(1, 5)]
            print('오늘 함께 취할 친구는 {}입니다! (치사량: {})'.format(pre_userList[x - 1], l))

            user_info['name'] = pre_userList[x - 1]
            user_info['limit'] = l
            print(user_info)
            final_userList.append(user_info)

        # print(user_info)
        print(final_userList)
        break

# def showLimit():



