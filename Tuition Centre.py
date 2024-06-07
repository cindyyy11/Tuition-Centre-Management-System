# Additional Feature
# Redirected to Main Menu In 3 Seconds
def redirect_to_main_menu():
    print('\nYou will be redirected to the main menu in 3 seconds.')
    for i in range(3, 0, -1):
        print(f'Redirecting in {i} seconds...')
        time.sleep(1)
    print("Redirected to the main menu!")


# Function to delete a line according to the line number
def delete_line(line_number):
    f = open("Brilliant Tuition Centre.txt", "r")
    lines = f.readlines()
    del lines[line_number]
    f = open("Brilliant Tuition Centre.txt", "w")
    f.writelines(lines)


# Admin function definition
# Function to register a tutor and assign them to levels and subjects
def register_tutor():
    f = open("Brilliant Tuition Centre.txt", "a")
    username = input("\nUsername: ")
    password = input("Password: ")
    IC_No = input("IC Number: ")
    Full_name = input("Full name: ")
    DOB = input("Date of birth: ")
    gender = input("Gender: ")
    race = input("Race: ")
    email = input("Email: ")
    contact = input("Contact number (without dash): ")
    address = input("Address (use '|' to show indent): ")
    teaching_subjects = input('Subjects currently teaching:')
    role = "Tutor"
    f.write(
        f"\n{username},{password},{IC_No},{Full_name},{DOB},{gender},{race},{email},{contact},{address},{teaching_subjects},{role}")
    f.close()
    print(f"Tutor {Full_name} registered successfully.")


# Function to delete a tutor
def delete_tutor():
    tutor_name = input("Enter tutor's name to delete: ")
    f = open("Brilliant Tuition Centre.txt", "r")
    line_to_delete = 0
    for line in f:
        if tutor_name not in line:
            line_to_delete += 1
        else:
            f = open("Brilliant Tuition Centre.txt", "r")
            lines = f.readlines()
            del lines[line_to_delete]
            f = open("Brilliant Tuition Centre.txt", "w")
            f.writelines(lines)
            print(f"Tutor {tutor_name} deleted successfully.")
            break
    else:
        print(f"Tutor does not exist.")


# Function to register a receptionist
def register_receptionist():
    username = input("\nUsername: ")
    password = input("Password: ")
    IC_No = input("IC Number: ")
    Name = input("Name: ")
    DOB = input("Date of birth: ")
    gender = input("Gender: ")
    race = input("Race: ")
    email = input("Email: ")
    contact = input("Contact number (without dash): ")
    address = input("Address (use '|' to show indent): ")
    role = "Receptionist"
    f = open("Brilliant Tuition Centre.txt", "a")
    f.write(f"\n{username},{password},{IC_No},{Name},{DOB},{gender},{race},{email},{contact},{address},{role}")
    f.close()
    print(f"Receptionist {Name} registered successfully.")


# Function to delete a receptionist
def delete_receptionist():
    receptionist_name = input("Enter receptionist's name to delete: ")
    f = open("Brilliant Tuition Centre.txt", "r")
    line_to_delete = 0
    for line in f:
        if receptionist_name not in line:
            line_to_delete += 1
        else:
            f = open("Brilliant Tuition Centre.txt", "r")
            lines = f.readlines()
            del lines[line_to_delete]
            f = open("Brilliant Tuition Centre.txt", "w")
            f.writelines(lines)
            print(f"Receptionist {receptionist_name} deleted successfully.")
            break
    else:
        print(f"Receptionist does not exist.")


# Function to retrieve the charges from class schedule stored in text file
def read_charges_from_file(level, subject):
    subjectname = level + ' ' + subject
    with open("Brilliant Tuition centre.txt", "r") as file:
        for line in file:
            if (subjectname in line) and (("Student" not in line) and ("Tutor" not in line)):
                name, charges, schedule = line.strip().split(",")
                return charges


# Function to calculate the total income for a given level and subject
def calculate_monthly_income(charges, total_students):
    monthly_income = (charges * total_students)
    return monthly_income


# Function to read the number of students enrolled in the level and subject
def read_student_from_file(level, subject):
    student = 0.0
    with open("Brilliant Tuition centre.txt", "r") as file:
        for line in file:
            if (level in line) and (subject in line) and ("Student" in line):
                student += 1.0
    return student


# Function to view the monthly income report based on student and subject name
def view_monthly_income_report():
    level = input("Enter the level: ")
    subject = input("Enter the subject: ")
    total_students = read_student_from_file(level, subject)
    charges = float(read_charges_from_file(level, subject))
    if total_students > 0:
        monthly_income = calculate_monthly_income(charges, total_students)
        print(f"Monthly Income Report for {level} {subject}: RM {monthly_income}")
    else:
        print("No students found for the given subject.")


# Function to update admin profile
def update_admin_profile(username):
    new_username = input("Enter new username: ")
    new_password = input("Enter new password: ")
    role = "Admin"
    f = open("Brilliant Tuition Centre.txt", "a")
    f.write(f"\n{new_username},{new_password},{role}")
    f.close()
    line_to_delete = 0
    f = open("Brilliant Tuition Centre.txt", "r")
    for line in f:
        if username not in line:
            line_to_delete += 1
        else:
            f = open("Brilliant Tuition Centre.txt", "r")
            lines = f.readlines()
            del lines[line_to_delete]
            f = open("Brilliant Tuition Centre.txt", "w")
            f.writelines(lines)
            print("Profile updated successfully.")
            break


# Receptionist function definition
# Function to register a student
def Students_details():
    username = input("\nUsername: ")
    password = input("Password: ")
    IC_No = input("IC Number: ")
    Student_name = input("Name: ")
    DOB = input("Date of birth: ")
    gender = input("Gender: ")
    race = input("Race: ")
    email = input("Email: ")
    contact = input("Contact number (without dash): ")
    address = input("Address (use '|' to show indent): ")
    level = input("Level: ")
    subjects = input("Subjects (use '&' sign if register more than one subject): ")
    month_enrol = input("Month of enrolment: ")
    parent_name = input("Parent's name: ")
    parent_contact = input("Parent's contact number (without dash): ")
    payable_amount = input("Payable amount: ")
    role = "Student"
    f = open("Brilliant Tuition Centre.txt", "a")
    f.write(
        f"\n{username},{password},{IC_No},{Student_name},{DOB},{gender},{race},{email},{contact},{address},{level},{subjects},{month_enrol},{parent_name},{parent_contact},{payable_amount},{role}")
    f.close()


# Function which allows receptionist to view and update students requests on subject enrolment
def Update_students_request(student_request):
    print(student_request)
    title, username, change_subject, subject_to_change, reason, status = student_request.strip().split(",")
    nstatus = input("Please update the status (either Approved or Rejected): ")
    f = open("Brilliant Tuition Centre.txt", "a")
    f.write(f"\n{title},{username},{change_subject},{subject_to_change},{reason},{nstatus}")
    f.close()
    f = open("Brilliant Tuition Centre.txt", "r")
    line_number_to_delete = 0
    for line in f:
        if (title not in line) or (username not in line) or (change_subject not in line) or (subject_to_change not in line) or (reason not in line) or (status not in line):
            line_number_to_delete += 1
        else:
            break
    delete_line(line_number_to_delete)
    print("The status is successfully updated. ")



# Function to update the subject enrolment of a student
def Update_students_subject(IC_No):
    f = open("Brilliant Tuition Centre.txt", "r+")
    for line in f:
        if (IC_No) in line:
            username, password, IC_No, Student_name, DOB, gender, race, email, contact, address, level, subjects, month_enrol, parent_name, parent_contact, payable_amount, role = line.strip().split(
                ",")
            subjects = input("Subjects (use '&' sign if register more than one subject): ")
            f.write(
                f"\n{username},{password},{IC_No},{Student_name},{DOB},{gender},{race},{email},{contact},{address},{level},{subjects},{month_enrol},{parent_name},{parent_contact},{payable_amount},{role}")
            f.close()
            f = open("Brilliant Tuition Centre.txt", "r")
            line_number_to_delete = 0
            for line in f:
                if (IC_No not in line) or (Student_name not in line):
                    line_number_to_delete += 1
                else:
                    break
            delete_line(line_number_to_delete)
            print("The record is successfully updated. ")
            import time
            redirect_to_main_menu()
            break
    else:
        print("No data found.")


# Function to update receptionist profile
def Update_my_profile(username):
    f = open("Brilliant Tuition Centre.txt", "r+")
    for line in f:
        data = line.strip().split(",")
        if (username == data[0]):
            username = input("\nUsername: ")
            password = input("Password: ")
            IC_No = input("IC Number: ")
            Name = input("Name: ")
            DOB = input("Date of birth: ")
            gender = input("Gender: ")
            race = input("Race: ")
            email = input("Email: ")
            contact = input("Contact number (without dash): ")
            address = input("Address (use '|' to show indent): ")
            role = "Receptionist"
            f.write(f"\n{username},{password},{IC_No},{Name},{DOB},{gender},{race},{email},{contact},{address},{role}")
            f.close()
            break


# Function which helps to determine whether user needs to insert more than 1 record
def Add_record():
    print("The record is successfully stored. Do you wish to add another record? ")
    option = int(input("1: Yes \n2: No"))
    if (option == 1):
        record = 1
    else:
        record = 0
    return record


# Function to store visitors records as visitors logbook
def Store_visitor(name, date, time, purpose):
    f = open("Brilliant Tuition Centre.txt", "a")
    f.write(f"\n{name},{date},{time},{purpose}")
    f.close()


# Function to display receipt as output
def Generate_receipt(username, name, amount_paid, outstanding_amount, subjects, level):
    import datetime
    date_time = datetime.datetime.now()
    print("\nReceipt")
    print(
        f"\n[Name: {name}]\n[Subjects: {subjects}]\n[Level: {level}]\n[Amount paid: {amount_paid}]\n[Outstanding amount: {outstanding_amount}]\n[Time: {date_time}]\n")


# Tutor function definition
# Function to add class information
def add_class():
    subject_name = input('Please enter subject name:')
    charges = input('Please enter charges:')
    class_schedule = input('Please enter the class schedule (Day|Time):')

    f = open("Brilliant Tuition Centre.txt", "a")
    f.write(f'\n{subject_name},{charges},{class_schedule}')
    f.close()
    print('Record added successfully.')


# Function to update class information
def update_class():
    f = open('Brilliant Tuition Centre.txt', 'r+')
    class_to_update = input('Please enter the subject name to update (eg. Form 1 Maths) :')
    for line in f:
        if class_to_update in line:
            new_subject_name = input('Please enter new subject name:')
            new_charges = input('Please enter new charges:')
            new_class_schedule = input('Please enter new class schedule (eg. Monday|1300):')
            f.write(f'\n{new_subject_name},{new_charges},{new_class_schedule}')
            f.close()
            f = open('Brilliant Tuition Centre.txt', 'r')
            line_number_to_delete = 0
            for line in f:
                if (class_to_update not in line) or ("Tutor" in line):
                    line_number_to_delete += 1
                else:
                    break
            delete_line(line_number_to_delete)
            print('The data is successfully updated.')
            break
    else:
        print("No data found.")


# Function to view the students enrolled in the subject and level taught by the tutor
def view_students_enrolled(username):
    f = open('Brilliant Tuition Centre.txt', 'r')
    for line in f:
        if (username in line):
            data = line.strip().split(",")
            subject_name = data[10].strip().split(" ")
            level = subject_name[0] + ' ' + subject_name[1]
            subject_to_view = subject_name[2]
            print('\nStudents enrolled:')
            f = open("Brilliant Tuition Centre.txt","r")
            for line in f:
                if (level in line) and (subject_to_view in line) and ("Student" in line):
                    data = line.strip().split(",")
                    print(data[3])
            f.close()


# Function to update tutor profile
def update_tutor_profile(username):
    f = open("Brilliant Tuition Centre.txt", "r+")
    for line in f:
        data = line.strip().split(",")
        if (username == data[0]):
            username = input("\nUsername: ")
            password = input("Password: ")
            IC_No = input("IC Number: ")
            Full_name = input("Full name: ")
            DOB = input("Date of birth: ")
            gender = input("Gender: ")
            race = input("Race: ")
            email = input("Email: ")
            contact = input("Contact number (without dash): ")
            address = input("Address (use '|' to show indent): ")
            teaching_subjects = input('Subjects currently teaching: ')
            role = "Tutor"
            f.write(
                f"\n{username},{password},{IC_No},{Full_name},{DOB},{gender},{race},{email},{contact},{address},{teaching_subjects},{role}")
            f.close()
            break


# Student function definition
# Function to view the schedule of the student's classes
def view_schedule(username):
    # Initialize variables
    student_level = None
    student_subjects = []
    data =[] #Initizalize data as an empty list to avoid the warning "Local Variable 'data' might be referenced before assignment"

    # Read the file content once and store it in a list
    with open("Brilliant Tuition Centre.txt", "r") as f:
      file_content=f.readlines()

    # Extract relevant student data based on the provided username
    for line in file_content:
        data = line.strip().split(",")
        if len(data) == 17 and username == data[0]:
            student_level = data[10]
            student_subjects = data[11].split("&")
            break # Exit the loop once the student data is found

    # If student_level or student_subjects is not found, return
    if not student_level or not student_subjects:
        print(f"No schedule found for {username}.")
        return

    # Print table header
    print(f"\nSchedule for {data[3]} (Level: {student_level}):\n")
    print('-' * 50)
    print(f"{'Subject':<30} |   {'Schedule':<15}")
    print('-' * 50)

    # Generate and print the table content
    for subject in student_subjects:
        student_class_combination = f"{student_level} {subject}".strip()
        for line in file_content:
            data = line.strip().split(",")
            if len(data) ==3 and student_class_combination == data[0]:
                subject_from_file, _ ,schedule = data[0], data[1], data[2]
                print(f"{subject_from_file:<30} | {schedule:<15}")


# Function to send a request to change subject enrollment of the user
def send_request(username):
    # Define constants for validation
    valid_subjects = ['Mathematics', 'Science', 'Mandarin', 'Bahasa Melayu', 'English']

    # Read the file content internally
    with open('Brilliant Tuition Centre.txt', 'r') as file:
        file_content = file.readlines()

    # Fetch the student's details
    student_data = None
    for line in file_content:
        data = line.strip().split(",")
        if username == data[0] and "Student" in line:
            student_data = data
            break

    if not student_data:
        print("Error: Student data not found!")
        return

    student_level = student_data[10]
    student_subjects = student_data[11].split("&")

    # Display the student's details
    print(f"\nStudent Level: {student_level}")
    print(f"Current Subjects: {', '.join(student_subjects)}")

    # Prompt the user to input the original subject they want to change
    original_subject = input("Enter the original subject you want to change: ")
    while original_subject not in student_subjects:
        print("Invalid choice. Please enter one of your current subjects.")
        original_subject = input("Enter the original subject you want to change: ")

    # Display the Available Subjects
    print(f"Available Subjects: {', '.join(valid_subjects)}")

    # Prompt the user to input the new subject they want to change to
    new_subject = input("Enter the new subject you want to switch to: ").strip()
    while new_subject not in valid_subjects or new_subject in student_subjects:
        print("Invalid choice, or you're already enrolled in the chosen subject. Please choose a valid subject.")
        new_subject = input("Enter the new subject you want to switch to: ").strip()

    # Check for duplicate requests in the provided file content
    duplicate_request = False
    for line in file_content:
        line_data = line.strip().split(",")
        if len(line_data) == 6 and line_data[0] == "Request" and line_data[1] == username and line_data[2] == original_subject and line_data[3] == new_subject:
            duplicate_request = True
            break

    if duplicate_request:
        print(f"\nDuplicate request detected. You've already requested to change from {original_subject} to {new_subject}.")
        return

    # Ask the student for the reason to change the subject
    reason = input(f"Why do you want to change from {original_subject} to {new_subject}? ")

    # Append the request with "Pending" status to the file
    with open('Brilliant Tuition Centre.txt', 'a') as file:
        file.write(f"\nRequest,{username},{original_subject},{new_subject},{reason},Pending")

    # Display the request details
    print("\nRequest has been sent successfully")
    print(f"\nRequest to change from {original_subject} to {new_subject} has been sent for the following reason: {reason}. Status: Pending")


# Function to delete the request (which is still pending) sent to the receptionist to change the subject
def delete_request(username):
    # Try block to handle potential runtime errors
    try:
        # Open and read the content of the file
        with open('Brilliant Tuition Centre.txt', 'r') as file:
            file_content = file.readlines()

        # Initialize an empty list to hold the new content of the file (without the deleted request)
        new_content = []

        # Flag to track if a request has been deleted
        request_deleted = False

        # Iterate over each line in the file content
        for line in file_content:
            data = line.strip().split(",")

            # Check if the line is a "Request" for the given username and is in "Pending" status
            if "Request" in line and data[1].strip() == username and data[5].strip() == "Pending":
                # Set the request_deleted flag to True
                request_deleted = True
                # Print detailed info about the request being deleted
                print(f"\nDeleting request to change from {data[2]} to {data[3]} for user {username}.")
                # Skip adding this line to the new_content list (effectively deleting it)
                continue
            # Add lines that don't meet the deletion criteria to the new_content list
            new_content.append(line)

        # Write the new content (without the deleted request) back to the file
        with open('Brilliant Tuition Centre.txt', 'w') as file:
            file.writelines(new_content)

        # Provide feedback to the user about whether the request was deleted or not
        if request_deleted:
            print(f"\nRequest for {username} has been deleted successfully!")
        else:
            print(f"\nNo pending request found for {username}.")

    # Handle any exceptions that might occur during the process
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to view payment status with the total balance that needs to be paid
def view_payment_status(username):
    # Initialize variables to default values
    student_name = None
    monthly_fee = None
    payment_month= None
    student_found = False
    total_balance = 0
    payment_history = []

    with open('Brilliant Tuition Centre.txt', 'r') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(",")

        # Extract student details
        if username in line and "Student" in line:
            student_name = data[3]
            monthly_fee = float(data[15])  # Convert the fee to float for calculations
            payment_month = data[12]
            student_found = True
            total_balance += monthly_fee  # Add the monthly fee to the total balance

        # Check for payment record and add to payment history
        if student_found and username in line and "payment" in line.lower():
            payment_date = data[1]
            payment_amount = float(data[2])
            payment_history.append((payment_date, payment_amount))
            total_balance -= payment_amount  # Subtract the payment amount from the total balance

    if not student_found:
        print(f"\nError: No details found for {username}!")
        return

    if student_name is None or monthly_fee is None or payment_month is None:
        print(f"\nError: Incomplete details found for {username}!")

    print(f"\nStudent Name: {student_name}")
    print(f"Monthly Fee: RM {monthly_fee}")
    print(f"Last enrollment/payment month: {payment_month}")

    # Displaying payment history
    if payment_history:
        print("\nPayment History:")
        for date, amount in payment_history:
            print(f"Paid RM {amount:.2f} on {date}")
    else:
        print("\nNo payments have been made yet.")

    if total_balance > 0:
        print(f"\nTotal balance to be paid: RM {total_balance:.2f}")
    else:
        print("\nNo balance due. All payments are up to date.")

# Function to update student profile
def update_student_profile(username):
    with open("Brilliant Tuition Centre.txt", 'r') as file:
        lines = file.readlines()

    # Display current details to the user
    for index, line in enumerate(lines):
        data = line.strip().split(",")
        if data[0] == username and len(data)==17:
            print("Your current details are:")
            print(f"Username: {data[0]}")
            print(f"Password: {'*' * len(data[1])}")  # Display password length as asterisks for privacy
            print(f"IC Number: {data[2]}")
            print(f"Name: {data[3]}")
            print(f"DOB: {data[4]}")
            print(f"Gender: {data[5]}")
            print(f"Race: {data[6]}")
            print(f"Email: {data[7]}")
            print(f"Contact Number: {data[8]}")
            print(f"Address: {data[9]}")
            print(f"Parent's Name: {data[13]}")
            print(f"Parent's Contact Number:{data[14]}")

            fields = ["username", "password", "IC Number", "Name", "DOB", "Gender", "Race", "Email",
                            "Contact Number","Address", "Parent's Name", "Parent's Contact Number"]

            while True:
                #Asking user which field to update
                print("\nWhich field would you like to update?")
                for indexx,field in enumerate(fields, 1):
                    print(f"{indexx}. {field}")

                print(f"{len(fields) + 1}. Exit")
                try:
                    choice= int(input("\nPlease enter your choice (1-13): "))
                    if choice>=1 and choice<= len(fields):
                        old_value = data[choice -1]
                        # Adjusting the indices for Parent's Name and Parent's Contact Number
                        if choice == 11:
                            old_value = data[13]
                        elif choice == 12:
                            old_value = data[14]

                        if choice ==2:
                            old_password = input("Enter your old password for confirmation:  ")
                            if old_password == old_value:  # Confirm old password
                                new_password = input("Enter your new password: ")
                                confirm_new_password = input("Confirm your new password: ")
                                if new_password == confirm_new_password:
                                    data[choice -1] = new_password
                                    print(f"\n{fields[choice - 1]} updated successfully from '{old_value}' to '{new_password}'!")
                                else:
                                    print("Password does not match. Please try again.")
                                    continue
                            else:
                                print("Incorrect old password. Please try again.")
                                continue
                        else:
                            new_value = input(f"Enter your new {fields[choice - 1]}: ")

                            # Adjusting the data update for Parent's Name and Parent's Contact Number
                            if choice == 11:
                                data[13] = new_value
                            elif choice == 12:
                                data[14] = new_value
                            else:
                                data[choice - 1] = new_value

                            print(f"\n{fields[choice - 1]} updated successfully from '{old_value}' to '{new_value}'!")
                    elif choice == len(fields) + 1:
                        print("Exiting update process.")
                        break
                    else:
                        print("Invalid choice. Please select a valid option.")
                except ValueError:
                    print("Please enter a valid number.")

                # This ensures we update the file once after all changes are made
                lines[index] = ",".join(data) +"\n"

            # Exit the outer loop after updating the details for the matched username
            break

    # Write the updated content to the file
    try:
        with open("Brilliant Tuition Centre.txt", 'w') as file:
            file.writelines(lines)
    except IOError:
        print("Error: An issue occured while writing to the file.")

# Additional feature for student part
# View Student's Request Status
def view_request_status(username):
    # Open the file to search for the student's requests
    with open("Brilliant Tuition Centre.txt","r") as file:
        file_content = file.readlines()

        # Initialize an empty list for storing requests
        requests =[]

        # Loop through each line in the file content
        for line in file_content:
            if line.startswith("Request") and username in line:
                _, _, current_subject, desired_subject, _, status = line.strip().split(",")
                requests.append((current_subject, desired_subject, status))

        # Display the results
        if not requests:
            print(f"\nNo requests found for username {username}.")
            return

        print(f"\nRequests for {username}: ")
        for current_subject, desired_subject, status in requests:
            print(f"Current Subject: {current_subject} -Desired Subject: {desired_subject} - Status: {status}")


# Login page (main menu)
print("--------Welcome to Brilliant Tuition Centre (BTC)!--------")
Attempt = 3
while (Attempt > 0):
    print("Please enter your username and password")
    username = input("Username: ")
    password = input("Password: ")
    f = open("Brilliant Tuition Centre.txt","r")
    for line in f:
        data = line.strip().split(",")
        # Determine the role of the user and go into the main page of the role
        if (username == data[0  ]) and (password == data[1]) and ("Admin" in line):

            # Main menu of admin
            print("\nWelcome admin! Please select an option to proceed.")
            while True:
                print("\nOptions:")
                print("1. Register a tutor and assign levels/subjects")
                print("2. Delete a tutor")
                print("3. Register a receptionist")
                print("4. Delete a receptionist")
                print("5. View monthly income report")
                print("6. Update own profile")
                print("7. Exit")
                choice = int(input("\nEnter your choice: "))
                if choice == 1:
                    register_tutor()
                    import time
                    redirect_to_main_menu()

                elif choice == 2:
                    delete_tutor()
                    import time
                    redirect_to_main_menu()

                elif choice == 3:
                    register_receptionist()
                    import time
                    redirect_to_main_menu()

                elif choice == 4:
                    delete_receptionist()
                    import time
                    redirect_to_main_menu()

                elif choice == 5:
                    view_monthly_income_report()
                    import time
                    redirect_to_main_menu()

                elif choice == 6:
                    update_admin_profile(username)
                    import time
                    redirect_to_main_menu()

                elif choice == 7:
                    print("Logging out. Bye!")
                    Attempt = -1
                    break
                else:
                    print("Invalid entry. Try again.")
            break
        elif (username == data[0]) and (password == data[1]) and ("Receptionist" in line):

            # Main menu of receptionist
            back = 0
            while (back == 0):
                print("\n==========Receptionist Menu=========="
                    "\n1: Register student's enrolment\n2: Read requests from students who want to change subject enrolment\n3: Update subject enrolment of a student\n4: Update student's payment"
                    "\n5: Delete students\n6: Update my profile\n7: Update visitors' logbook\n8: Log out")
                feature = int(input("Select one of the features: "))

                # Register student
                if (feature == 1):
                    record = 1
                    while (record > 0):
                        Students_details()
                        record = Add_record()
                    import time
                    redirect_to_main_menu()

                # View and update students request on subject enrolment
                elif (feature == 2):
                    f = open("Brilliant Tuition Centre.txt", "r")
                    for line in f:
                        if ("Request" in line) and ("Pending" in line):
                            Update_students_request(line)
                            import time
                            redirect_to_main_menu()
                            break
                    else:
                        print("No request.")
                        import time
                        redirect_to_main_menu()

                # Update student's subject enrolment
                elif (feature == 3):
                    IC_No = input("Enter student's IC number: ")
                    Student_name = input("Enter student's name: ")
                    print(f"Do you want to update the subject enrolment of {Student_name}?")
                    option = int(input("1: Yes\n2: No"))
                    if (option == 1):
                        Update_students_subject(IC_No)
                    else:
                        import time
                        redirect_to_main_menu()

                # Accept payment from student & generate receipt
                elif (feature == 4):
                    record = 1
                    while (record > 0):
                        Student_name = input("Enter student's name: ")
                        f = open("Brilliant Tuition Centre.txt", "r+")
                        for line in f:
                            if (Student_name) in line:
                                username, password, IC_No, Student_name, DOB, gender, race, email, contact, address, level, subjects, month_enrol, parent_name, parent_contact, payable_amount, role = line.strip().split(
                                    ",")
                                amount = float(payable_amount)
                                amount_paid = float(input(f"Enter the amount paid by {Student_name}: "))
                                outstanding_amount = amount - amount_paid
                                payable_amount = str(outstanding_amount)
                                f.write(f"\n{username},{password},{IC_No},{Student_name},{DOB},{gender},{race},{email},{contact},{address},{level},{subjects},{month_enrol},{parent_name},{parent_contact},{payable_amount},{role}")
                                Generate_receipt(username,Student_name, amount_paid, outstanding_amount, subjects, level)
                                f.close()
                                f = open("Brilliant Tuition Centre.txt", "r")
                                line_number_to_delete = 0
                                for line in f:
                                    if (Student_name not in line):
                                        line_number_to_delete += 1
                                    else:
                                        break
                                delete_line(line_number_to_delete)
                                f.close()
                                import datetime
                                date_time = datetime.date.today()
                                f = open("Brilliant Tuition Centre.txt", "a")
                                f.write(f"\n{username},{date_time},{amount_paid},payment")
                                f.close()
                                break
                        else:
                            print("No data found.")
                        record = Add_record()
                    import time
                    redirect_to_main_menu()

                # Delete student's record
                elif (feature == 5):
                    IC_No = input("Enter student's IC Number: ")
                    Student_name = input("Enter student's name: ")
                    print(f"Do you want to delete the details of {Student_name}?")
                    option = int(input("1: Yes\n2: No"))
                    if (option == 1):
                        f = open("Brilliant Tuition Centre.txt", "r")
                        line_number_to_delete = 0
                        for line in f:
                            if (IC_No not in line) or (Student_name not in line):
                                line_number_to_delete += 1
                            else:
                                break
                        delete_line(line_number_to_delete)
                        print("The record is deleted.")
                        import time
                        redirect_to_main_menu()
                    else:
                        import time
                        redirect_to_main_menu()

                # Update receptionist's profile
                elif (feature == 6):
                    Update_my_profile(username)
                    f = open("Brilliant Tuition Centre.txt", "r")
                    line_number_to_delete = 0
                    for line in f:
                        if (username not in line):
                            line_number_to_delete += 1
                        else:
                            break
                    delete_line(line_number_to_delete)
                    import time
                    redirect_to_main_menu()

                # Store visitor's logbook
                elif (feature == 7):
                    record = 1
                    while (record > 0):
                        visitor_name = input("Visitor name: ")
                        visitor_date = input("Date: ")
                        visitor_time = input("Time: ")
                        purpose = input("Purpose: ")
                        Store_visitor(visitor_name, visitor_date, visitor_time, purpose)
                        record = Add_record()
                    import time
                    redirect_to_main_menu()

                # Log out
                elif (feature == 8):
                    print("Do you wish to log out?")
                    option = int(input("1: Yes \n2: No"))
                    if (option == 1):
                        print("You have successfully logged out. Thank you. ")
                        back = 1
                        Attempt = -1
                else:
                    print("This feature does not exist. Please enter again. ")
            break
        elif (username == data[0]) and (password == data[1]) and ("Tutor" in line):

            # Main Menu of tutor
            back = 0
            while back == 0:
                print(
                    '\n======Tutor Main Menu====== \n1. Add Class Information \n2. Update Class Information \n3. View Students Enrolled \n4. Update Tutor Profile \n5. Log Out')
                option = int(input('Please enter option:'))
                if option == 1:
                    record = 1
                    while record > 0:
                        add_class()
                        record = Add_record()
                    import time
                    redirect_to_main_menu()

                elif option == 2:
                    record = 1
                    while record > 0:
                        update_class()
                        record = Add_record()
                    import time
                    redirect_to_main_menu()

                elif option == 3:
                    view_students_enrolled(username)
                    import time
                    redirect_to_main_menu()

                elif option == 4:
                    update_tutor_profile(username)
                    f = open("Brilliant Tuition Centre.txt", "r")
                    line_number_to_delete = 0
                    for line in f:
                        if (username not in line):
                            line_number_to_delete += 1
                        else:
                            break
                    delete_line(line_number_to_delete)
                    print('Do you wish to update again?')
                    option = int(input('1.Yes \n2.No'))
                    if option == 1:
                        update_tutor_profile(username)
                        f = open("Brilliant Tuition Centre.txt", "r")
                        line_number_to_delete = 0
                        for line in f:
                            if (username not in line):
                                line_number_to_delete += 1
                            else:
                                break
                        delete_line(line_number_to_delete)
                    else:
                        print('Successfully updated.')
                        import time
                        redirect_to_main_menu()

                elif option == 5:
                    print('Do you wish to log out?')
                    option = int(input('1.Yes \n2.No'))
                    if option == 1:
                        print('You have successfully logged out. Thank You!')
                        back = 1
                        Attempt = -1
                else:
                    print('This feature does not exist. Please enter again. ')
            break
        elif (username == data[0]) and (password == data[1]) and ("Student" in line):

            # Main menu for the student part
            import time
            back = 0
            while back == 0:
                print("===" * 80)
                print("\t\t\t\tStudent Menu")
                print("===" * 80)
                print("1. View Class Schedule")
                print("2. Send Request to Change Subject Enrollment")
                print("3. Delete Request")
                print("4. View Payment Status")
                print("5. Update Student Profile")
                print("6. View Request Status")
                print("7. Logout")

                try:
                    choice = int(input("Please enter your choice (1-7): "))
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 7.")
                    continue

                print("===" * 80)

                # View Class Schedule
                if (choice == 1):
                    print("===" * 80)
                    print("\t\t\t\tView Class Schedule")
                    print("===" * 80)
                    print(time.strftime("\nDate: %Y/%m/%d Time: %I:%M:%S %p"))
                    view_schedule(username)
                    redirect_to_main_menu()

                # Send Request To Change The Subject Enrollment
                elif (choice == 2):
                    print("===" * 80)
                    print("\t\t\t\tSend Request To Change The Subject Enrollment")
                    print("===" * 80)
                    send_request(username)
                    redirect_to_main_menu()

                # Delete Request
                elif (choice == 3):
                    print("===" * 80)
                    print("\t\t\t\tDelete Request")
                    print("===" * 80)
                    delete_request(username)
                    redirect_to_main_menu()

                # View Payment Status
                elif (choice == 4):
                    print("===" * 80)
                    print("\t\t\t\tView Payment Status With The Total Balance That Needs To Be Paid, If Any")
                    print("===" * 80)
                    print(time.strftime("\nDate: %Y/%m/%d Time: %I:%M:%S %p"))
                    view_payment_status(username)
                    redirect_to_main_menu()

                # Update Student Profile
                elif (choice == 5):
                    print("===" * 80)
                    print("\t\t\t\tUpdate Student Profile")
                    print("===" * 80)
                    update_student_profile(username)
                    redirect_to_main_menu()

                # View Request Status
                elif (choice == 6):
                    print("===" * 80)
                    print("\t\t\t\tView Request Status ")
                    print("===" * 80)
                    print(time.strftime("\nDate: %Y/%m/%d Time: %I:%M:%S %p"))
                    view_request_status(username)
                    redirect_to_main_menu()

                # Log Out
                elif (choice == 7):
                    print('Do you wish to log out?')
                    option = int(input('1.Yes \n2.No'))
                    if option == 1:
                        print('You have successfully logged out. Thank You!')
                        back = 1
                        Attempt = -1
                else:
                    print('This feature does not exist. Please enter again. ')
            break
    else:
        Attempt -= 1
        # User is unable to log in if exceed the attempt
        if (Attempt == 0):
            print("You have exceeded the attempt left. Please try again 3 minutes later. ")
        else:
            print("Your username or password does not match with the role. Please enter again. ")
