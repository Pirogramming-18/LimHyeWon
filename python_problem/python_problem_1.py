num=0
character=1 #1일땐 A, -1 일땐 B 플레이어

while 1:
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
                if character==1:#A player
                    print('player{}:{}'.format('A', num))
                else:
                    print('player{}:{}'.format('B', num))
            character*=(-1) #플레이어 전환을 위한 값 변경경

