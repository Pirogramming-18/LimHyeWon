import sys
student_list=[]

##############  menu 1
def Menu1(name,mid_score,final_score) :
    student={}
    student['name']=name
    student['mid_score']=mid_score
    student['final_score']=final_score
    student['grade']='0' #grade는 우선 '0'으로 초기화

    student_list.append(student)
    print(student_list)
    #student (dictionary)에 학생 정보 저장후 student_list (list)에 학생들의 정보 추가

##############  menu 2
def Menu2(student_list) :
    for student in student_list:
        if student['grade']=='0':

            average=(student['mid_score']+student['final_score'])/2

            if average>=90:
                student['grade']='A'
            elif average>= 80:
                student['grade']='B'
            elif average>= 70:
                student['grade']='C'
            else: student['grade']='D'
        else:continue

    print('Grading to all students')

    #학점 부여 하는 코딩

##############  menu 3
def Menu3(student_list) :
    print('----------------------------')
    print('{:<6} {:<4} {:<4} {:<4}'.format('name','mid','final','grade'))
    print('----------------------------')
    for student in student_list:
        # print('{}      {}      {}      {}'.format(student['name'],student['mid_score'],student['final_score'],student['grade']))
        print("{:<6} {:<4} {:<4} {:<4}".format(student['name'],student['mid_score'],student['final_score'],student['grade']))

##############  menu 4
def Menu4(del_student):
    student_list.remove(del_student)


#학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        #학생 정보 입력받기
        try:
            name,mid_score,final_score=input('Enter name mid-score final-score: ').split(' ')

            #이름 겹칠때
            for student in student_list:
                if student['name']==name:
                    raise Exception('Already exist name!')

            #score에 정수 이외의 것을 입력했을때
            if not (mid_score.isdigit() and final_score.isdigit()):
                raise Exception('Score is not positive integer!')


        #data입력을 3개보다 덜 했을때
        except ValueError:
            print('Num of data is not 3!')

        except Exception as e:
            print(e)

        else:
            mid_score = int(mid_score)
            final_score = int(final_score)
            Menu1(name,mid_score,final_score)

    elif choice == "2" :
        try:
            if not student_list: raise Exception
            
        except:print('No student data')
        else:Menu2(student_list)

    elif choice == "3" :
        try:
            if not student_list: raise Exception('No student data')
            for student in student_list:
                if student['grade']=='0':
                    raise Exception("There is a student who didn't get grade")
                
        except Exception as e:
            print(e)

        else:Menu3(student_list)

    elif choice == "4" :
        try:
            if not student_list: raise Exception('No student data')

            del_student_name=input('Enter the name to delete: ')
            del_student={} #삭제학생을 담아놓을 리스트
            for student in student_list:
                if student['name']==del_student_name:
                    del_student=student
                    Menu4(del_student)
                    print('{} student information is deleted'.format(del_student_name))
            if not del_student:#삭제 학생에 아무것도 안담겼다면
                print("Not exist name!")

        except Exception as e: print(e)

    elif choice == "5" :
        print('exit program!')
        sys.exit()
        #프로그램 종료 메세지 출력

    else :
        print("wrong number. choose again")