#15/12/22
FileName = 'AssignmentCodeWithDef.py'

#imported
import os

#System title
print('=' * 70)
print("\t\tUTAR System for Courses and Students")
print('=' * 70)
print("Available subjects: ")

#Course type and students name
course_code = ['FHBM1114', 'FHCT1024', 'FHEL1012', 'FHMM1034']
course_des = ['MANAGEMENT', 'PROGRAMMING CONCEPTS AND DESIGN' ,'ENGLISH FOR ACADEMIC STUDIES', 'MATHEMATICS III']
for (a,b) in zip(course_code, course_des):
    print(a,b)

#Authorized users
AuthorizedUsers = ['Chong Jia Hui', 'Ho Jin Xin', 'Peggy Wong Pei Chi', 'Ng Ying Ting', 'Yuon Hui Xin']
Pins = '271222'

#FHBM1114 MANAGEMENT
def management():
    print('-' * 70)
    print("FHBM1114 (MANAGEMENT) -----> ")
    file = open("FHBM1114studentlist.txt", "r")
    fileLst = file.readlines()
    
    with open("FHBM1114studentlist.txt", "r") as f:
        print(f.read())
    print('-' * 70)
    print("Choose an option.")
    option1 = input("|  <A>dd  |  <U>pdate  |  <D>elete  |  <E>xit  |: ").upper()
    if option1 == 'A':
        file = open("FHBM1114studentlist.txt", "a")
        new_studentid = input("New Student ID [YY#####] | (Press 'E' to exit >> ").upper()
        if new_studentid != 'E':
            new_studentname = input("New Student Name >> ")
            file.write('\n' + new_studentid + '\t' + '  ' + new_studentname)
            file.close()    
            continuepage = input("Successfully added! Press 'Y' to continue this page and 'N' to exit to course student maintenance: ").upper()
            if continuepage == 'Y':
                management()
            else:
                course_stu()
        else:
            course_stu()

    elif option1 == 'U':
        file = open("FHBM1114studentlist.txt", "r")
        change_infoid = input("Enter existing Student ID that want to make changes | (Press 'E' to exit >> ").upper()
        if change_infoid != 'E':
            change_infoname = input("Enter existing Student Name that want to make changes >> ")
            new_infoid = input("Updated Student ID >> ")
            new_infoname = input("Updated Student Name >> ")
            with open("FHBM1114studentlist.txt", "r+") as f:
                new_idname = f.read()
                new_idname = new_idname.replace(change_infoid, new_infoid)
                new_idname = new_idname.replace(change_infoname, new_infoname)
                f.truncate(0)
                f.seek(0)
                f.write(new_idname)
                f.close()
                continuepage = input("Successfully updated! Press 'Y' to continue this page and 'N' to exit to course student maintenance: ").upper()
                if continuepage == 'Y':
                    management()
                else:
                    course_stu()
        else:
            course_stu()

    elif option1 == 'D':
        file = open("FHBM1114studentlist.txt", "r")
        del_id = input("Enter Student ID that want to delete [Press 'E' to exit] >> ").upper()
        if del_id != 'E':
            del_name = input("Enter Student Name that want to delete >> ")
            with open("FHBM1114studentlist.txt", "r+") as f:
                file = f.readlines()
                f.seek(0)
                for line in file:
                    if del_id and del_name not in line:
                        f.write(line)
                f.truncate()
                continuepage = input("Successfully deleted! Press 'Y' to continue this page and 'N' to exit to course student maintenance: ").upper()
                if continuepage == 'Y':
                    management()
                else:
                    course_stu()
        else:
            course_stu

    elif option1 == 'E':
        confirmation = input("Press Y to confirm exit this section and N to decline >>> ").upper()
        if confirmation == 'Y':
            course_stu()
        else:
            management()

    else:
        print("Invalid option. Please make sure you choose from the given option.\n")
        management()

#FHCT1024 PROGRAMMING CONCEPTS AND DESIGN
def pcad():
    print('-' * 70)
    print("FHCT1024 (PROGRAMMING CONCEPTS AND DESIGN) -----> ")
    file = open("FHCT1024studentlist.txt", "r")
    fileLst = file.readlines()
    with open("FHCT1024studentlist.txt", "r") as f:
        print(f.read())
    print('-' * 70)
    print("Choose an option.")
    option2 = input("|  <A>dd  |  <U>pdate  |  <D>elete  |  <E>xit  |: ").upper()
    if option2 == 'A':
        file = open("FHCT1024studentlist.txt", "a")
        new_studentid2 = input("New Student ID [YY#####] | (Press 'E' to exit >> ").upper()
        if new_studentid2 != 'E':
            new_studentname2 = input("New Student Name >> ")
            file.write('\n' + new_studentid2 + '\t' + '  ' + new_studentname2)
            file.close()    
            continuepage2 = input("Successfully added! Press 'Y' to continue this page and 'N' to exit to course maintenance: ").upper()
            if continuepage2 == 'Y':
                pcad()
            else:
                course_stu()
        else:
            course_stu()

    elif option2 == 'U':
        file = open("FHCT1024studentlist.txt", "r")
        change_infoid2 = input("Enter existing Student ID that want to make changes | (Press 'E' to exit >> ").upper()
        if change_infoid2 != 'E':
            change_infoname2 = input("Enter existing Student Name that want to make changes >> ")
            new_infoid2 = input("Updated Student ID >> ")
            new_infoname2 = input("Updated Student Name >> ")
            with open("FHCT1024studentlist.txt", "r+") as f:
                new_idname2 = f.read()
                new_idname2 = new_idname2.replace(change_infoid2, new_infoid2)
                new_idname2 = new_idname2.replace(change_infoname2, new_infoname2)
                f.truncate(0)
                f.seek(0)
                f.write(new_idname2)
                f.close()
                continuepage2 = input("Successfully updated! Press 'Y' to continue this page and 'N' to exit to course student maintenance: ").upper()
                if continuepage2 == 'Y':
                    pcad()
                else:
                    course_stu()
        else:
            course_stu()

    elif option2 == 'D':
        file = open("FHCT1024studentlist.txt", "r")
        del_id2 = input("Enter Student ID that want to delete [Press 'E' to exit] >> ").upper()
        if del_id2 != 'E':
            del_name2 = input("Enter Student Name that want to delete >> ")
            with open("FHCT1024studentlist.txt", "r+") as f:
                file = f.readlines()
                f.seek(0)
                for line in file:
                    if del_id2 and del_name2 not in line:
                        f.write(line)
                f.truncate()
                continuepage2 = input("Successfully deleted! Press 'Y' to continue this page and 'N' to exit to course student maintenance: ").upper()
                if continuepage2 == 'Y':
                    pcad()
                else:
                    course_stu()
        else:
            course_stu

    elif option2 == 'E':
        confirmation2 = input("Press Y to confirm exit this section and N to decline >>> ").upper()
        if confirmation2 == 'Y':
            course_stu()
        else:
            pcad()

    else:
        print("Invalid option. Please make sure you choose from the given option.\n")
        pcad()

#FHEL1012 ENGLISH FOR ACADEMIC STUDIES
def eas():
    print('-' * 70)
    print("FHEL1012 (ENGLISH FOR ACADEMIC STUDIES) -----> ")
    file = open("FHEL1012studentlist.txt", "r")
    fileLst = file.readlines()
    with open("FHEL1012studentlist.txt", "r") as f:
        print(f.read())
    print('-' * 70)
    print("Choose an option.")
    option3 = input("|  <A>dd  |  <U>pdate  |  <D>elete  |  <E>xit  |: ").upper()
    if option3 == 'A':
        file = open("FHEL1012studentlist.txt", "a")
        new_studentid3 = input("New Student ID [YY#####] | (Press 'E' to exit >> ").upper()
        if new_studentid3 != 'E':
            new_studentname3 = input("New Student Name >> ")
            file.write('\n' + new_studentid3 + '\t' + '  ' + new_studentname3)
            file.close()    
            continuepage3 = input("Successfully added! Press 'Y' to continue this page and 'N' to exit to course maintenance: ").upper()
            if continuepage3 == 'Y':
                eas()
            else:
                course_stu()
        else:
            course_stu()

    elif option3 == 'U':
        file = open("FHEL1012studentlist.txt", "r")
        change_infoid3 = input("Enter existing Student ID that want to make changes | (Press 'E' to exit >> ").upper()
        if change_infoid3 != 'E':
            change_infoname3 = input("Enter existing Student Name that want to make changes >> ")
            new_infoid3 = input("Updated Student ID >> ")
            new_infoname3 = input("Updated Student Name >> ")
            with open("FHEL1012studentlist.txt", "r+") as f:
                new_idname3 = f.read()
                new_idname3 = new_idname3.replace(change_infoid3, new_infoid3)
                new_idname3 = new_idname3.replace(change_infoname3, new_infoname3)
                f.truncate(0)
                f.seek(0)
                f.write(new_idname3)
                f.close()
                continuepage3 = input("Successfully updated! Press 'Y' to continue this page and 'N' to exit to course student maintenance: ").upper()
                if continuepage3 == 'Y':
                    eas()
                else:
                    course_stu()
        else:
            course_stu()

    elif option3 == 'D':
        file = open("FHEL1012studentlist.txt", "r")
        del_id3 = input("Enter Student ID that want to delete [Press 'E' to exit] >> ").upper()
        if del_id3 != 'E':
            del_name3 = input("Enter Student Name that want to delete >> ")
            with open("FHEL1012studentlist.txt", "r+") as f:
                file = f.readlines()
                f.seek(0)
                for line in file:
                    if del_id3 and del_name3 not in line:
                        f.write(line)
                f.truncate()
                continuepage3 = input("Successfully deleted! Press 'Y' to continue this page and 'N' to exit to course student maintenance: ").upper()
                if continuepage3 == 'Y':
                    eas()
                else:
                    course_stu()
        else:
            course_stu

    elif option3 == 'E':
        confirmation3 = input("Press Y to confirm exit this section and N to decline >>> ").upper()
        if confirmation3 == 'Y':
            course_stu()
        else:
            eas()

    else:
        print("Invalid option. Please make sure you choose from the given option.\n")
        eas()

#FHMM1034 MATHEMATICS III
def mathsiii():
    print('-' * 70)
    print("FHMM1034 (MATHEMATICS III) -----> ")
    file = open("FHMM1034studentlist.txt", "r")
    fileLst = file.readlines()
    with open("FHMM1034studentlist.txt", "r") as f:
        print(f.read())
    print('-' * 70)
    print("Choose an option.")
    option4 = input("|  <A>dd  |  <U>pdate  |  <D>elete  |  <E>xit  |: ").upper()
    if option4 == 'A':
        file = open("FHMM1034studentlist.txt", "a")
        new_studentid4 = input("New Student ID [YY#####] | (Press 'E' to exit >> ").upper()
        if new_studentid4 != 'E':
            new_studentname4 = input("New Student Name >> ")
            file.write('\n' + new_studentid4 + '\t' + '  ' + new_studentname4)
            file.close()    
            continuepage4 = input("Successfully added! Press 'Y' to continue this page and 'N' to exit to course maintenance: ").upper()
            if continuepage4 == 'Y':
                mathsiii()
            else:
                course_stu()
        else:
            course_stu()

    elif option4 == 'U':
        file = open("FHMM1034studentlist.txt", "r")
        change_infoid4 = input("Enter existing Student ID that want to make changes | (Press 'E' to exit >> ").upper()
        if change_infoid4 != 'E':
            change_infoname4 = input("Enter existing Student Name that want to make changes >> ")
            new_infoid4 = input("Updated Student ID >> ")
            new_infoname4 = input("Updated Student Name >> ")
            with open("FHMM1034studentlist.txt", "r+") as f:
                new_idname4 = f.read()
                new_idname4 = new_idname4.replace(change_infoid4, new_infoid4)
                new_idname4 = new_idname4.replace(change_infoname4, new_infoname4)
                f.truncate(0)
                f.seek(0)
                f.write(new_idname4)
                f.close()
                continuepage4 = input("Successfully updated! Press 'Y' to continue this page and 'N' to exit to course student maintenance: ").upper()
                if continuepage4 == 'Y':
                    mathsiii()
                else:
                    course_stu()
        else:
            course_stu()

    elif option4 == 'D':
        file = open("FHMM1034studentlist.txt", "r")
        del_id4 = input("Enter Student ID that want to delete [Press 'E' to exit] >> ").upper()
        if del_id4 != 'E':
            del_name4 = input("Enter Student Name that want to delete >> ")
            with open("FHMM1034studentlist.txt", "r+") as f:
                file = f.readlines()
                f.seek(0)
                for line in file:
                    if del_id4 and del_name4 not in line:
                        f.write(line)
                f.truncate()
                continuepage4 = input("Successfully deleted! Press 'Y' to continue this page and 'N' to exit to course student maintenance: ").upper()
                if continuepage4 == 'Y':
                    mathsiii()
                else:
                    course_stu()
        else:
            course_stu

    elif option4 == 'E':
        confirmation4 = input("Press Y to confirm exit this section and N to decline >>> ").upper()
        if confirmation4 == 'Y':
            course_stu()
        else:
            mathsiii()

    else:
        print("Invalid option. Please make sure you choose from the given option.\n")
        mathsiii()

#Exit program confirmation
def exitprogram():
    confirmation = input("Are you sure you want to exit the program? \nPress Y to confirm and N to go back: ").upper()
    if confirmation == 'Y':
        print('=' * 70)
        print("Thank you")
        input("Press Enter to exit.")
    else:
        startmenu()

#Course maintenance
def course():
    print('\n')
    print('-' * 70)
    print("Course Maintenance")
    print('-' * 70)
    for (a,b) in zip(course_code, course_des):
        print(a,b)
    print('-' * 70)
    print("Choose an option.")
    option = input("|  <A>dd  |  <U>pdate  |  <D>elete  |  <E>xit  |: ").upper()
    if option == 'A':
        courseCode_op2a = input('Enter Course Code >> ').upper()
        if courseCode_op2a != 'E':
            courseDes_op2a = input('Enter Course Desc >> ').upper()
            course_code.append(courseCode_op2a)
            course_des.append(courseDes_op2a)
            print(('-'*70) + '\n')
            for (a,b) in zip(course_code, course_des):
                print(a,b);
        else:
            course()
        continuepage = input("\nSuccessfully added! Press 'Y' to continue this page and 'N' to exit to course maintenance: ").upper()
        if continuepage == 'Y':
            course()
        else:
            assessment()

    elif option == 'U':
        courseCode_op2u = input('Enter exsiting Course Code >> ').upper()
        if courseCode_op2u != 'E':
            courseCode_op2uc = input('Enter updated Course Code >> ').upper()
            for i in range (0, len(course_code)):
                if course_code[i] == courseCode_op2u:
                    course_code[i] = courseCode_op2uc;
                    courseDes_op2u = input('Enter existing Course Desc >> ').upper()
                    courseDes_op2uc = input('Enter updated Course Desc  >> ').upper()
            for x in range (0, len(course_des)):
                if course_des[x] == courseDes_op2u:
                    course_des[x] = courseDes_op2uc;
                    print(('-'*70) + '\n')
            for (a,b) in zip(course_code, course_des):
                print(a,b);
        else:
            course()
        continuepage = input("\nSuccessfully updated! Press 'Y' to continue this page and 'N' to exit to course maintenance: ").upper()
        if continuepage == 'Y':
            course()
        else:
            assessment()

    elif option == 'D':
        courseCode_op2d = input('Enter existing Course Code that want to be deleted >> ').upper()
        if courseCode_op2d != 'E':
            courseDes_op2d = input('Enter existing Course Desc that want to be deleted >> ').upper()
            while(courseCode_op2d in course_code) and (courseDes_op2d in course_des):
                course_code.remove(courseCode_op2d)
                course_des.remove(courseDes_op2d)
                print(('-'*70) + '\n')
            for (a,b) in zip(course_code, course_des):
                print(a,b);
        else:
            course()
        continuepage = input("\nSuccessfully deleted! Press 'Y' to continue this page and 'N' to exit to course maintenance: ").upper()
        if continuepage == 'Y':
            course()
        else:
            assessment()
            
    elif option == 'E':
        confirmexit = input("You will exit this section. Press Y to confirm and N to decline --> ").upper()
        if confirmexit == 'Y':
            systemcon()
        else:
            course()

    else:
        print("Invalid option. Please try again.")
        course()

#Assessment type maintenance 
def assessment():
    print('\n')
    print('-' * 70)
    print('Course Assessment Type Maintenance')
    print('-' * 70)
    print(course_code)
    courseCode2 = input("Enter course code(Press 'E' to exit): ").upper()
    if courseCode2 == 'FHBM1114':
        management2()
    if courseCode2 == 'FHCT1024':
        pcad2()
    if courseCode2 == 'FHEL1012':
        eas2()
    if courseCode2 == 'FHMM1034':
        mathsiii2()
    elif courseCode2 == 'E':
        systemcon()
    else:
        print("Invalid course code. Please try again. ")
        assessmnent()

#FHBM1114 (MANAGEMENT)
def management2():
    print('\n')
    print('-' * 70)
    print("FHBM1114 (MANAGEMENT) -----> ")
    file = open("FHBM1114marks.txt", "r")
    fileLst = file.readlines()
    
    with open("FHBM1114marks.txt", "r") as f:
        print(f.read())
    print('-' * 70)
    print("Choose an option.")
    option1 = input("|  <A>dd  |  <U>pdate  |  <D>elete  |  <E>xit  |: ").upper()
    if option1 == 'A':
        file = open("FHBM1114marks.txt", "a")
        insertAssType = input("Enter Assessment Type [Press 'E' to exit] >>").upper() 
        if insertAssType != 'E':
            insertTotalMarks = int(input("Enter Total Marks >> "))
            insertFinalMarks = float(input("Enter Total Marks to Final >> "))
            print('-' * 70)
            file.write('\n' + insertAssType + '|' + str(insertTotalMarks) + '|' + str(insertFinalMarks))
            file.close()
            continuepage = input("Successfully added! Press 'Y' to continue this page and 'N' to exit to assessment type maintenance: ").upper()
            if continuepage == 'Y':
                management2()
            else:
                assessment()
        else:
            assessment()
                    
    elif option1 == 'U':
        file = open("FHBM1114marks.txt", "r")
        insertAssType = input("Enter existing Assessment Type that want to make changes [Press 'E' to exit] >> ").upper()
        if insertAssType != 'E':
            insertTotalMarks = int(input("Enter existing Total Marks that want to make changes >> "))
            insertFinalMarks = float(input("Enter existing Total Marks to Final Marks that want to make changes >> "))
            newAssType = input("Enter updated Assessment Type >> ").upper()
            newTotalMarks = float(input("Enter updated Total Marks >> "))
            newFinalMarks = int(input("Enter updated Total Marks to Final Marks >>"))
        elif insertAssType == 'E':
            assessment()
        #here is delete
        with open("FHBM1114marks.txt", "r") as f:
            readLine = f.readlines()
        with open("FHBM1114marks.txt", "w") as f:
            for line in readLine:
                if line.strip("\n") != (insertAssType + "|" + str(insertTotalMarks) + "|" + str(insertFinalMarks)):
                    f.write(line)
        #here you add the 'add' code
        with open("FHBM1114marks.txt", "a") as f:
            f.write('\n' + newAssType + '|' + str(newTotalMarks) + '|' + str(newFinalMarks))
        
        continuepage = input("Successfully updated! Press 'Y' to continue this page and 'N' to exit to assessment type maintenance: ").upper()
        if continuepage == 'Y':
            management2()
        else:
            assessment()
        

    elif option1 == 'D':
        insertAssType = input("Enter existing Asssessment Type that want to be deleted | (Press 'E' to exit >>").upper()
        if insertAssType != 'E':
            insertTotalMarks = int(input("Enter existing Total Marks that want to be deleted >> "))
            insertFinalMarks = float(input("Enter existing Total Marks to Final that want to be deleted >> "))
            with open("FHBM1114marks.txt", "r") as f:
                readLine = f.readlines()
            with open("FHBM1114marks.txt", "w") as f:
                for line in readLine:
                    if line.strip("\n") != (insertAssType + "|" + str(insertTotalMarks) + "|" + str(insertFinalMarks)):
                        f.write(line)
            continue3= input("\nSuccessfully deleted! Press 'Y' to continue this page and 'N' to exit assessment type maintenance: ")
            if continue3 == "Y" or continue3 == "y":
                management2()
            else:
                assessment()
        else:
            assessment()
                    
    elif option1 == 'E':
        confirmation = input("Press Y to confirm exit this section and N to decline >>> ").upper()
        if confirmation == 'Y':
            assessment()
        else:
            management2()
    else:
        print("Invalid option. Please make sure you choose from the given option.\n")
        management2()
        

#FHCT1024 (PROGRAMMING CONCEPTS AND DESIGN)
def pcad2():
    print('\n')
    print('-' * 70)
    print("FHCT1024 (PROAMMING CONCEPTS AND DESIGN) -----> ")
    file = open("FHCT1024marks.txt", "r")
    fileLst = file.readlines()
    
    with open("FHCT1024marks.txt", "r") as f:
        print(f.read())
    print('-' * 70)
    print("Choose an option.")
    option1 = input("|  <A>dd  |  <U>pdate  |  <D>elete  |  <E>xit  |: ").upper()
    if option1 == 'A':
        file = open("FHCT1024marks.txt", "a")
        insertAssType = input("Enter Assessment Type [Press 'E' to exit] >> ").upper() 
        if insertAssType != 'E':
            insertTotalMarks = int(input("Enter Total Marks >> "))
            insertFinalMarks = float(input("Enter Total Marks to Final >> "))
            print('-' * 70)
            file.write('\n' + insertAssType + '|' + str(insertTotalMarks) + '|' + str(insertFinalMarks))
            file.close()
            continuepage = input("Successfully added! Press 'Y' to continue this page and 'N' to exit to assessment type maintenance: ").upper()
            if continuepage == 'Y':
                pcad2()
            else:
                assessment()
        else:
            assessment()
                    
    elif option1 == 'U':
        file = open("FHCT1024marks.txt", "r")
        insertAssType = input("Enter existing Assessment Type that want to make changes [Press 'E' to exit] >> ").upper()
        if insertAssType != 'E':
            insertTotalMarks = int(input("Enter existing Total Marks that want to make changes >> "))
            insertFinalMarks = float(input("Enter existing Total Marks to Final Marks that want to make changes >> "))
            newAssType = input("Enter updated Assessment Type >> ").upper()
            newTotalMarks = int(input("Enter updated Total Marks >> "))
            newFinalMarks = float(input("Enter updated Total Marks to Final Marks >>"))
        elif insertAssType == 'E':
            assessment()
        #here is delete
        with open("FHCT1024marks.txt", "r") as f:
            readLine = f.readlines()
        with open("FHCT1024marks.txt", "w") as f:
            for line in readLine:
                if line.strip("\n") != (insertAssType + "|" + str(insertTotalMarks) + "|" + str(insertFinalMarks)):
                    f.write(line)
        #here you add the 'add' code
        with open("FHCT1024marks.txt", "a") as f:
            f.write('\n' + newAssType + '|' + str(newTotalMarks) + '|' + str(newFinalMarks))
        
        continuepage = input("Successfully updated! Press 'Y' to continue this page and 'N' to exit to assessment type maintenance: ").upper()
        if continuepage == 'Y':
            pcad2()
        else:
            assessment()
        

    elif option1 == 'D':
        insertAssType = input("Enter existing Asssessment Type that want to be deleted | (Press 'E' to exit >> ").upper()
        if insertAssType != 'E':
            insertTotalMarks = int(input("Enter existing Total Marks that want to be deleted >> "))
            insertFinalMarks = float(input("Enter existing Total Marks to Final that want to be deleted >> "))
            with open("FHCT1024marks.txt", "r") as f:
                readLine = f.readlines()
            with open("FHCT1024marks.txt", "w") as f:
                for line in readLine:
                    if line.strip("\n") != (insertAssType + "|" + str(insertTotalMarks) + "|" + str(insertFinalMarks)):
                        f.write(line)
            continue3= input("\nSuccessfully deleted! Press 'Y' to continue this page and 'N' to assessment type maintenance: ")
            if continue3 == "Y" or continue3 == "y":
                pcad2()
            else:
                assessment()
        else:
            assessment()
                    
    elif option1 == 'E':
        confirmation = input("Press Y to confirm exit this section and N to decline >>> ").upper()
        if confirmation == 'Y':
            assessment()
        else:
            pcad2()
    else:
        print("Invalid option. Please make sure you choose from the given option.\n")
        pcad2()

#FHEL1012 (ENGLISH FOR ACADEMIC STUDIES)
def eas2():
    print('\n')
    print('-' * 70)
    print("FHEL1012 (ENGLISH FOR ACADEMIC STUDIES) -----> ")
    file = open("FHEL1012marks.txt", "r")
    fileLst = file.readlines()
    
    with open("FHEL1012marks.txt", "r") as f:
        print(f.read())
    print('-' * 70)
    print("Choose an option.")
    option1 = input("|  <A>dd  |  <U>pdate  |  <D>elete  |  <E>xit  |: ").upper()
    if option1 == 'A':
        file = open("FHEL1012marks.txt", "a")
        insertAssType = input("Enter Assessment Type [Press 'E' to exit] >> ").upper() 
        if insertAssType != 'E':
            insertTotalMarks = int(input("Enter Total Marks >> "))
            insertFinalMarks = float(input("Enter Total Marks to Final >> "))
            print('-' * 70)
            file.write('\n' + insertAssType + '|' + str(insertTotalMarks) + '|' + str(insertFinalMarks))
            file.close()
            continuepage = input("Successfully added! Press 'Y' to continue this page and 'N' to exit to assessment type maintenance: ").upper()
            if continuepage == 'Y':
                eas2()
            else:
                assessment()
        else:
            assessment()
                    
    elif option1 == 'U':
        file = open("FHEL1012marks.txt", "r")
        insertAssType = input("Enter existing Assessment Type that want to make changes [Press 'E' to exit] >> ").upper()
        if insertAssType != 'E':
            insertTotalMarks = int(input("Enter existing Total Marks that want to make changes >> "))
            insertFinalMarks = float(input("Enter existing Total Marks to Final Marks that want to make changes >> "))
            newAssType = input("Enter updated Assessment Type >> ").upper()
            newTotalMarks = int(input("Enter updated Total Marks >> "))
            newFinalMarks = float(input("Enter updated Total Marks to Final Marks >>"))
        elif insertAssType == 'E':
            assessment()
        #here is delete
        with open("FHEL1012marks.txt", "r") as f:
            readLine = f.readlines()
        with open("FHEL1012marks.txt", "w") as f:
            for line in readLine:
                if line.strip("\n") != (insertAssType + "|" + str(insertTotalMarks) + "|" + str(insertFinalMarks)):
                    f.write(line)
        #here you add the 'add' code
        with open("FHEL1012marks.txt", "a") as f:
            f.write('\n' + newAssType + '|' + str(newTotalMarks) + '|' + str(newFinalMarks))
        
        continuepage = input("Successfully updated! Press 'Y' to continue this page and 'N' to exit to assessment type maintenance: ").upper()
        if continuepage == 'Y':
            eas2()
        else:
            assessment()
        

    elif option1 == 'D':
        insertAssType = input("Enter existing Asssessment Type that want to be deleted | (Press 'E' to exit >>").upper()
        if insertAssType != 'E':
            insertTotalMarks = int(input("Enter existing Total Marks that want to be deleted >> "))
            insertFinalMarks = float(input("Enter existing Total Marks to Final that want to be deleted >> "))
            with open("FHEL1012marks.txt", "r") as f:
                readLine = f.readlines()
            with open("FHEL1012marks.txt", "w") as f:
                for line in readLine:
                    if line.strip("\n") != (insertAssType + "|" + str(insertTotalMarks) + "|" + str(insertFinalMarks)):
                        f.write(line)
            continue3= input("\nSuccessfully deleted! Press 'Y' to continue this page and 'N' to exit assessment type maintenance: ")
            if continue3 == "Y" or continue3 == "y":
                eas2()
            else:
                assessment()
        else:
            assessment()
                    
    elif option1 == 'E':
        confirmation = input("Press Y to confirm exit this section and N to decline >>> ").upper()
        if confirmation == 'Y':
            assessment()
        else:
            eas2()
    else:
        print("Invalid option. Please make sure you choose from the given option.\n")
        eas2()

#FHMM1034 (MATHEMATICS III)
def mathsiii2():
    print('\n')
    print('-' * 70)
    print("FHMM1034 (MATHEMATICS III) -----> ")
    file = open("FHMM1034marks.txt", "r")
    fileLst = file.readlines()
    
    with open("FHMM1034marks.txt", "r") as f:
        print(f.read())
    print('-' * 70)
    print("Choose an option.")
    option1 = input("|  <A>dd  |  <U>pdate  |  <D>elete  |  <E>xit  |: ").upper()
    if option1 == 'A':
        file = open("FHMM1034marks.txt", "a")
        insertAssType = input("Enter Assessment Type [Press 'E' to exit] >> ").upper() 
        if insertAssType != 'E':
            insertTotalMarks = int(input("Enter Total Marks >> "))
            insertFinalMarks = float(input("Enter Total Marks to Final >> "))
            print('-' * 70)
            file.write('\n' + insertAssType + '|' + str(insertTotalMarks) + '|' + str(insertFinalMarks))
            file.close()
            continuepage = input("Successfully added! Press 'Y' to continue this page and 'N' to exit to assessment type maintenance: ").upper()
            if continuepage == 'Y':
                mathsiii2()
            else:
                assessment()
        else:
            assessment()
                    
    elif option1 == 'U':
        file = open("FHMM1034marks.txt", "r")
        insertAssType = input("Enter existing Assessment Type that want to make changes [Press 'E' to exit] >> ").upper()
        if insertAssType != 'E':
            insertTotalMarks = int(input("Enter existing Total Marks that want to make changes >> "))
            insertFinalMarks = float(input("Enter existing Total Marks to Final Marks that want to make changes >> "))
            newAssType = input("Enter updated Assessment Type >> ").upper()
            newTotalMarks = int(input("Enter updated Total Marks >> "))
            newFinalMarks = float(input("Enter updated Total Marks to Final Marks >>"))
        elif insertAssType == 'E':
            assessment()
        #here is delete
        with open("FHMM1034marks.txt", "r") as f:
            readLine = f.readlines()
        with open("FHMM1034marks.txt", "w") as f:
            for line in readLine:
                if line.strip("\n") != (insertAssType + "|" + str(insertTotalMarks) + "|" + str(insertFinalMarks)):
                    f.write(line)
        #here you add the 'add' code
        with open("FHMM1034marks.txt", "a") as f:
            f.write('\n' + newAssType + '|' + str(newTotalMarks) + '|' + str(newFinalMarks))
        
        continuepage = input("Successfully updated! Press 'Y' to continue this page and 'N' to exit to assessment type maintenance: ").upper()
        if continuepage == 'Y':
            mathsiii2()
        else:
            assessment()
        

    elif option1 == 'D':
        insertAssType = input("Enter existing Asssessment Type that want to be deleted | (Press 'E' to exit >>").upper()
        if insertAssType != 'E':
            insertTotalMarks = int(input("Enter existing Total Marks that want to be deleted >> "))
            insertFinalMarks = float(input("Enter existing Total Marks to Final that want to be deleted >> "))
            with open("FHMM1034marks.txt", "r") as f:
                readLine = f.readlines()
            with open("FHMM1034marks.txt", "w") as f:
                for line in readLine:
                    if line.strip("\n") != (insertAssType + "|" + str(insertTotalMarks) + "|" + str(insertFinalMarks)):
                        f.write(line)
            continue3= input("\nSuccessfully deleted! Press 'Y' to continue this page and 'N' to exit assessment type maintenance: ")
            if continue3 == "Y" or continue3 == "y":
                mathsiii2()
            else:
                assessment()
        else:
            assessment()
                    
    elif option1 == 'E':
        confirmation = input("Press Y to confirm exit this section and N to decline >>> ").upper()
        if confirmation == 'Y':
            assessment()
        else:
            mathsiii2()
    else:
        print("Invalid option. Please make sure you choose from the given option.\n")
        mathsiii2()
        
#Preview student marks
def preview_marks():
    print('\n')
    print(course_code)
    results = input("Enter course code to preview student results (Press 'E' to exit): ").upper()
    if results == 'FHBM1114':
        management_stu_results()
    elif results == 'FHCT1024':
        pcad_stu_results()
    elif results == 'FHEL1012':
        eas_stu_results()
    elif results == 'FHMM1034':
        maths_stu_results()
    elif results == 'E':
        systemcon()
    else:
        print("Invalid course code. Please try again. ")
        preview_marks()

    
#Management student results
student_id = []
name= []
marks = []
grade = []
total = {'A':0,'B':0,'C':0,'F':0}

def management_stu_results():
    with open('FHBM1114_total_marks.txt', 'r') as f:
        print(f.read())
    with open('FHBM1114_total_marks.txt','a') as s:
        id = input('\nStudent ID (Press E to exit): ').upper()
        while id != 'E':
            name_1 = input('Name: ').upper()
            mark_1 = int(input('Total Marks: '))
            s.write('%s|%s|%d\n'%(id,name_1,mark_1))
            id = input('\nStudent ID: ').upper()

    with open('FHBM1114_total_marks.txt','r') as s:
        lines = s.readlines()
    
        for i in lines:
            data = i.strip('\n').split('|')
            student_id.append(data[0])
            name.append(data[1])
            marks.append(int(data[-1]))

        for x in marks:
            if x <= 49:
                grade.append('F')
                total['F'] +=1
            elif x > 49 and x <= 59:
                grade.append('C')
                total['C'] +=1
            elif x > 59 and x <= 79:
                grade.append('B')
                total['B'] +=1
            elif x > 79 and x <= 100:
                grade.append('A')
                total['A'] +=1

    new = "\n".join("{}\t\t{}\t\t{}\t{}".format(x,y,z,k)for x,y,z,k in zip(student_id,name,marks,grade))
    print("-"*80)
    print("Studend ID\tName\t\t\tMarks   Grade")
    print(new)
    print("\nNumber of times each of the grades is %s"%total)
    confirmation = input("Press Y to confirm exit this section and N to decline >>> ").upper()
    if confirmation == 'Y':
        course_stu()
    else:
        preview_marks()

#PCAD student results
student_id = []
name= []
marks = []
grade = []
total = {'A':0,'B':0,'C':0,'F':0}

def pcad_stu_results():
    with open('FHCT1024_total_marks.txt', 'r') as f:
        print(f.read())
    with open('FHCT1024_total_marks.txt','a') as s:
        id = input('\nStudent ID (Press E to exit): ').upper()
        while id != 'E':
            name_1 = input('Name: ').upper()
            mark_1 = int(input('Total Marks: '))
            s.write('%s|%s|%d\n'%(id,name_1,mark_1))
            id = input('\nStudent ID: ').upper()

    with open('FHCT1024_total_marks.txt','r') as s:
        lines = s.readlines()
    
        for i in lines:
            data = i.strip('\n').split('|')
            student_id.append(data[0])
            name.append(data[1])
            marks.append(int(data[-1]))
            
        for x in marks:
            if x <= 49:
                grade.append('F')
                total['F'] +=1
            elif x > 49 and x <= 59:
                grade.append('C')
                total['C'] +=1
            elif x > 59 and x <= 79:
                grade.append('B')
                total['B'] +=1
            elif x > 79 and x <= 100:
                grade.append('A')
                total['A'] +=1

    new = "\n".join("{}\t\t{}\t\t{}\t{}".format(x,y,z,k)for x,y,z,k in zip(student_id,name,marks,grade))
    print("-"*80)
    print("Studend ID\tName\t\t\tMarks   Grade")
    print(new)
    print("\nNumber of times each of the grades is %s"%total)
    confirmation = input("Press Y to confirm exit this section and N to decline >>> ").upper()
    if confirmation == 'Y':
        course_stu()
    else:
        preview_marks()

#eas student results
student_id = []
name= []
marks = []
grade = []
total = {'A':0,'B':0,'C':0,'F':0}

def eas_stu_results():
    with open('FHEL1012_total_marks.txt', 'r') as f:
        print(f.read())
    with open('FHEL1012_total_marks.txt','a') as s:
        id = input('\nStudent ID (Press E to exit): ').upper()
        while id != 'E':
            name_1 = input('Name: ').upper()
            mark_1 = int(input('Total Marks: '))
            s.write('%s|%s|%d\n'%(id,name_1,mark_1))
            id = input('\nStudent ID: ').upper()

    with open('FHEL1012_total_marks.txt','r') as s:
        lines = s.readlines()
    
        for i in lines:
            data = i.strip('\n').split('|')
            student_id.append(data[0])
            name.append(data[1])
            marks.append(int(data[-1]))
            
        for x in marks:
            if x <= 49:
                grade.append('F')
                total['F'] +=1
            elif x > 49 and x <= 59:
                grade.append('C')
                total['C'] +=1
            elif x > 59 and x <= 79:
                grade.append('B')
                total['B'] +=1
            elif x > 79 and x <= 100:
                grade.append('A')
                total['A'] +=1

    new = "\n".join("{}\t\t{}\t\t{}\t{}".format(x,y,z,k)for x,y,z,k in zip(student_id,name,marks,grade))
    print("-"*80)
    print("Studend ID\tName\t\t\tMarks   Grade")
    print(new)
    print("\nNumber of times each of the grades is %s"%total)
    confirmation = input("Press Y to confirm exit this section and N to decline >>> ").upper()
    if confirmation == 'Y':
        course_stu()
    else:
        preview_marks()

#mathsiii student results
student_id = []
name= []
marks = []
grade = []
total = {'A':0,'B':0,'C':0,'F':0}

def maths_stu_results():
    with open('FHMM1034_total_marks.txt', 'r') as f:
        print(f.read())
    with open('FHMM1034_total_marks.txt','a') as s:
        id = input('\nStudent ID (Press E to exit): ').upper()
        while id != 'E':
            name_1 = input('Name: ').upper()
            mark_1 = int(input('Total Marks: '))
            s.write('%s|%s|%d\n'%(id,name_1,mark_1))
            id = input('\nStudent ID: ').upper()

    with open('FHMM1034_total_marks.txt','r') as s:
        lines = s.readlines()
    
        for i in lines:
            data = i.strip('\n').split('|')
            student_id.append(data[0])
            name.append(data[1])
            marks.append(int(data[-1]))
            
        for x in marks:
            if x <= 49:
                grade.append('F')
                total['F'] +=1
            elif x > 49 and x <= 59:
                grade.append('C')
                total['C'] +=1
            elif x > 59 and x <= 79:
                grade.append('B')
                total['B'] +=1
            elif x > 79 and x <= 100:
                grade.append('A')
                total['A'] +=1

    new = "\n".join("{}\t\t{}\t\t{}\t{}".format(x,y,z,k)for x,y,z,k in zip(student_id,name,marks,grade))
    print("-"*80)
    print("Studend ID\tName\t\t\tMarks   Grade")
    print(new)
    print("\nNumber of times each of the grades is %s"%total)
    confirmation = input("Press Y to confirm exit this section and N to decline >>> ").upper()
    if confirmation == 'Y':
        course_stu()
    else:
        preview_marks()

        
#Course student maintenance
def make_change():
    print('\n')
    print(course_code)
    courseCode3 = input("Enter course code (Press 'E' to exit): ").upper()
    if courseCode3 == 'FHBM1114':
        management()
    elif courseCode3 == 'FHCT1024':
        pcad()
    elif courseCode3 == 'FHEL1012':
        eas()
    elif courseCode3 == 'FHMM1034':
        mathsiii()
    elif courseCode3 == 'E':
        systemcon()
    else:
        print("Invalid course code. Please try again. ")
        course_stu()

        
#KEY IN STUDENT MARKS
def insert_marks():
    print('\n')
    print('-'*70)
    print(course_code)
    insert_marks1 = input("Enter course code to insert student results (Press 'E' to exit): ").upper()
    if insert_marks1 == 'FHBM1114':
        management_ass_marks()
    elif insert_marks1 == 'FHCT1024': 
        pcd_ass_marks()
    elif insert_marks1 == 'FHEL1012':
        eas_ass_marks()
    elif insert_marks1 == 'FHMM1034':
        maths_ass_marks()
    elif insert_marks1 == 'E':
        systemcon()
    else:
        print("Invalid course code. Please try again. ")
        insert_marks()

#FHBM1114 MANAGEMENT (KEY IN ASSESSMENT MARKS)
student_id = []
assignmentlist = []
presentationlist= []
cal = []
midtermlist = []
finallist = []
averagelist =[]

def management_ass_marks():
    with open('FHBM1114_ass_marks.txt','a') as s:
        id = input('\nStudent ID (Press E to exit): ').upper()
        while id != 'E':
            assignment = int(input('Assignment marks: '))
            presentation = int(input('Presentation marks: '))
            midterm = int(input('Midterm marks: '))
            final = int(input('Final: '))
            cal = (assignment+presentation+midterm+final) * 0.7143
            print("Total Marks: ",cal)
            s.write('%s,\t%d,\t%d,\t%d,\t%d,\t%d\n'%(id,assignment,presentation,midterm,final,cal))
            id = input('\nStudent ID: ').upper()
            
    with open('FHBM1114_ass_marks.txt','r') as s:
        lines = s.readlines()
    
        for i in lines:
            data = i.strip("\n").split(",")
            student_id.append(data[0])
            assignmentlist.append(int(data[1]))
            presentationlist.append(int(data[2]))
            midtermlist.append(int(data[3]))
            finallist.append(int(data[4]))
            averagelist.append(int(data[-1]))
      
    print("FHBM1114 (MANAGEMENT)")
    print("-" * 90)
    print("Student ID  | A(15/0.15) | P(10|0.10) |  M(15/0.15)  |  F(100/0.60)  | Total Marks")
    print("-" * 90)       
    new = "\n".join("{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(x,y,z,k,m,n)for x,y,z,k,m,n in zip(student_id,assignmentlist,presentationlist,midtermlist,finallist,averagelist))
    print(new)
    confirmation = input("Press Y to confirm exit this section and N to decline >>> ").upper()
    if confirmation == 'Y':
        course_stu()
    else:
        insert_marks()

#FHCT1024 PCAD (KEY IN ASSESSMENT MARKS)
sstudent_id = []
test1 = []
test2 = []
cal = []
assignmentlist = []
finallist = []
averagelist =[]

def pcd_ass_marks():
    with open('FHCT1024_ass_marks.txt','a') as s:
        id = input('\nStudent ID (Press E to exit): ').upper()
        while id != 'E':
            t1 = int(input('T1 marks: '))
            t2 = int(input('T2 marks: '))
            assignment = int(input('Assignment marks: '))
            final = int(input('Final marks: '))
            cal = (t1+t2+assignment+final) * 0.4
            print("Total Marks: ",cal)
            s.write('%s,\t%d,\t%d,\t%d,\t%d,\t%d\n'%(id,t1,t2,assignment,final,cal))
            id = input('\nStudent ID: ').upper()
            
    with open('FHCT1024_ass_marks.txt','r') as s:
        lines = s.readlines()
    
        for i in lines:
            data = i.strip("\n").split(",")
            student_id.append(data[0])
            test1.append(int(data[1]))
            test2.append(int(data[2]))
            assignmentlist.append(int(data[3]))
            finallist.append(int(data[4]))
            averagelist.append(int(data[-1]))
      
    print("FHCT1024 (PROGRAMMING CONCPETS AND DESIGN)")
    print("-" * 90)
    print("Student ID  | T1(50/0.15) | T2(50|0.15) |  A(50/0.20)  |  F(100/0.50)  | Total Marks")
    print("-" * 90)       
    new = "\n".join("{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(x,y,z,k,m,n)for x,y,z,k,m,n in zip(student_id,test1,test2,assignmentlist,finallist,averagelist))
    print(new)
    confirmation = input("Press Y to confirm exit this section and N to decline >>> ").upper()
    if confirmation == 'Y':
        course_stu()
    else:
        insert_marks()

#FHEL1012 EAS (KEY IN ASSESSMENT MARKS)
student_id = []
presentationlist = []
midtermlist = []
assignmentlist = []
cal = []
averagelist = []
finallist = []
def eas_ass_marks():
    with open('FHEL1012_ass_marks.txt','a') as s:
        id = input('\nStudent ID (Press E to exit): ').upper()
        while id != 'E':
            assignment = int(input('Assignment marks: '))
            presentation = int(input('Presentation marks: '))
            midterm = int(input('Midterm marks: '))
            final = int(input('Final marks: '))
            cal = (assignment+presentation+midterm+final)
            print("Total Marks: ",cal)
            s.write('%s,\t%d,\t%d,\t%d,\t%d,\t%d\n'%(id,assignment,presentation,midterm,final,cal))
            id = input('\nStudent ID: ').upper()
            
    with open('FHEL1012_ass_marks.txt','r') as s:
        lines = s.readlines()
    
        for i in lines:
            data = i.strip("\n").split(",")
            student_id.append(data[0])
            assignmentlist.append(int(data[1]))
            presentationlist.append(int(data[2]))
            midtermlist.append(int(data[3]))
            finallist.append(int(data[4]))
            averagelist.append(int(data[-1]))
      
    print("FHEL1012 (ENGLISH FOR ACADEMIC STUDIES)")
    print("-" * 90)
    print("Student ID  | A(20/0.20) | P(15/0.15) | M(15/0.15) | F(50/0.50) | Total Marks")
    print("-" * 90)
    new = "\n".join("{}\t\t{}\t\t{}\t\t{}\t{}\t\t{}".format(x,y,z,k,m,n)for x,y,z,k,m,n in zip(student_id,assignmentlist,presentationlist,midtermlist,finallist,averagelist))
    print(new)
    confirmation = input("Press Y to confirm exit this section and N to decline >>> ").upper()
    if confirmation == 'Y':
        course_stu()
    else:
        insert_marks()

#FHMM1034 MATHS III (KEY IN ASSESSMENT MARKS)
student_id = []
test1 = []
test2 = []
finallist = []
cal = []
averagelist = [] 
def maths_ass_marks():
    with open('FHMM1034_ass_marks.txt','a') as s:
        id = input('\nStudent ID (Press E to exit): ').upper()
        while id != 'E':
            t1 = int(input('T1 marks: '))
            t2 = int(input('T2 marks: '))
            final = int(input('Final marks: '))
            cal = (t1+t2+final) / 2
            print("Total Marks: ",cal)
            s.write('%s,\t%d,\t%d,\t%d,\t%d\n'%(id,t1,t2,final,cal))
            id = input('\nStudent ID: ').upper()
            
    with open('FHMM1034_ass_marks.txt','r') as s:
        lines = s.readlines()
    
        for i in lines:
            data = i.strip("\n").split(",")
            student_id.append(data[0])
            test1.append(int(data[1]))
            test2.append(int(data[2]))
            finallist.append(int(data[3]))
            averagelist.append(int(data[-1]))
      
    print("FHMM1034 (MATHEMATICS III)")
    print("-" * 90)
    print("Student ID  | T1(50/0.15) | T2(50|0.15) ||  F(100/0.50)  | Total Marks")
    print("-" * 90)       
    new = "\n".join("{}\t\t{}\t\t{}\t\t{}\t\t{}".format(x,y,z,k,m)for x,y,z,k,m in zip(student_id,test1,test2,finallist,averagelist))
    print(new)
    confirmation = input("Press Y to confirm exit this section and N to decline >>> ").upper()
    if confirmation == 'Y':
        course_stu()
    else:
        insert_marks()

#Course Student Maintenance 
def course_stu():
    print('\n')
    print('-' * 70)
    print("Course Student Maintenance")
    print('-' * 70)
    print("Choose an option.")
    option1 = input("|  <M>ake change  |  <I>nsert student marks  |  <P>review student marks  |  <E>xit  |: ").upper()
    if option1 == 'M':
        make_change()
    elif option1 == 'I':
        insert_marks()
    elif option1 == 'P':
        preview_marks()
    elif option1 == 'E':
        systemcon()
    else:
        print("Invalid course code. Please try again. ")
        course_stu()
        
#System configuration (main menu)
def systemcon():
    print('\n')
    print('-' * 70)
    print("System configuration. Please choose an option. ")
    print('-' * 70)
    option = int(input("|  [1]Courses Maintenance  |  [2]Assessment Type Maintenance  |  [3]Courses Student Maintenance  |  [4]Exit  |: "))
    if option == 1:
        course()
    elif option == 2:
        assessment()
    elif option == 3:
        course_stu()
    elif option == 4:
        exitprogram()
    else:
        print("Invalid option. Please try again. \n")
        systemcon()

#Login process
def startmenu():
    loginid = input("\nInsert name: ")
    password = input("Insert password: ")
    
    def verifyaccess(name, pwd):
        if name in AuthorizedUsers and pwd in Pins:
            return True
        else:
            return False

    verified = verifyaccess(loginid, password)
    if verified == True:
        print("Access granted. \n")
        print("Welcome back!")
        systemcon()
    else:
        print("Access denied.")
        reenter = input("Press Y to reenter and N to exit: ").upper()
        if reenter == 'Y':
            startmenu()
        else:
            exitprogram()
startmenu()


