# Question number 1 
class Star_Cinema:
    __hall_list = []

    def entry_hall(self, name):
        # Done for admin
        Star_Cinema.__hall_list.append(name)

# Question number 2
class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self._show_list=[]
        self.Seats={}
        self.entry_hall(self)
    
    # Question number 3
    def entry_show(self,id,movieName,time):
        # Done for admin
        self._show_list.append((id,movieName,time))
        list2=[]
        for i in range(self.rows):
            for j in range(self.cols):
                list2.append([0]*self.cols)
        self.Seats[id]= list2
        
        # for i in range(self.rows):
        #     for j in range(self.cols):
        #         print(self.list[i][j])
    
    
    # Question number 4
    def Book_seats(self,id,rows_cols):   
        # for user
        id_list = self.Seats.keys()
        if id not in id_list:
            print("Invalid show ID.")
            return
        if rows_cols[0]>= self.rows or rows_cols[0]< 0 or rows_cols[1]>= self.cols or rows_cols[1]< 0:
            print("Invalid input.")
            return 
        if self.Seats[id][row_col[0]][row_col[1]] == 1:
            print("Seat already booked.")
            return
        self.Seats[id][row_col[0]][row_col[1]] = 1
        print("Seat booked successfully.")

        

    # Question number 5
    def view_show_list(self):
        # Done for user
        print("All shows are:")
        for i in self._show_list:
            print (f"Movie name: {i[1]}    ID: {i[0]}     Time: {i[2]}")


    # Question number 6
    def view_available_seats(self, id):
        # for user
        if id not in self.Seats.keys():
            print("Invalid show ID.")
            return
        
        print("Available seats are:")
        list2 = self.Seats[id]
        for i in range(self.rows):
            for j in range(self.cols):
                print(list2[i][j], end=" ")
            print()



print("Please confirm your Identity.")
print("Write '1' for Admin and '2' for users.")
user_input = int(input())
hall = Hall(10,10,101)
hall.entry_show(101,"Maharaj"," 11 am - 11/07/2024")

# for admin
if user_input == 1:
    print("Please enter your password.")
    password = int(input())
    if password == 123:
        print("Welcome Admin.")
        
        while True:
            print("Please enter your choice.")
            print("1. Entry hall.")
            print("2. Entry show.")
            print("3. Exit.")
            user_input = int(input())
            # Hall entry
            if user_input == 1:
                print("Please enter hall details.")
                row = int(input("Number of Rows -> "))
                col = int(input("Number of Columns -> "))
                hall_no = int(input(" Hall number -> "))
                # name = input("Hall name -> ")
                hall = Hall(row,col,hall_no)
            

            elif user_input == 2:
                show_id = int(input("Please enter show id -> "))
                movie_name = input("Please enter movie name -> ")
                time = input("Please enter time -> ")
                hall.entry_show(show_id,movie_name,time)
                hall.view_show_list()
            elif user_input == 3:
                print("Thank you.")
                break
            else:
                print("Invalid choice.")

    else:
        print("Invalid password.\n Please try again.")



    # For users 
elif user_input == 2:
    print("Welcome User.")
    while True:
        print("Please enter your choice.")
        print ("1. View show list.")
        print ("2. Show available seats.")
        print ("3. Book seats.")
        print ("4. Exit.")
        user_input = int(input())
        if user_input == 1:
            hall.view_show_list()
        elif user_input == 2:
            id = int(input("Please enter show id -> "))
            hall.view_available_seats(id)
        elif user_input == 3:
            show_id = int(input("Please enter show id -> "))
            count = int(input("How many seats do you want to book? -> " ))
            for i in range(count):
                rows = int(input("Please enter seat row number -> "))
                cols = int(input("Please enter seat column number -> "))
                row_col = (rows, cols)
                hall.Book_seats(show_id, row_col)
        elif user_input == 4:
            print("Thank you.")
            break
        else:
            print("Invalid choice.")
   
else:
    print("Invalid input.\n Please try again")

        