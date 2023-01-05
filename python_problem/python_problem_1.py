import sys
num=0
index=0 #character 배열의 인덱스

while 1:
    character=['A','B']
    try:
        select=int(input('부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능):'))
    except:#정수형으로 변환 불가일때
        print('정수를 입력하세요')
    else:
        if (select!= 1 and select !=2 and select !=3):
            print('1,2,3중 하나를 입력하세요')
        else:
            for i in range(select):
                num+=1
                print('player{}:{}'.format(character[index], num))

            if index==0: index=1#플레이어 전환을 위한 값 변경경
            else: index=0

