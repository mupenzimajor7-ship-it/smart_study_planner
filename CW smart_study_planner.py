# ****************************************************************
# Smart Study Planner
# programming fundamentals coursework
#
# student: Mupenzi Major biryeija
# Registration Number: VU-BIT-2603-1098-DAY
# Programme: Bachelor of Science cybersecurity and digital forensics
# Year: 1.2
# Block: 2
# Module: Programming Fundamentals
# Lecturer: kinyinyo David Hope
# ****************************************************************


# ****************************************************************
# Session Classification
# First Fuction: classic_session()
# classifies a study session  according to its duration.
# ****************************************************************



def classify_session(duration):

    if duration < 30:
        return "Short"
    
    elif duration <= 90:
        return "Medium"
    
    else:
        return "Long"





# ****************************************************************
# Second Function: add_session()
# Adds a new study sessions to the session list.
# ****************************************************************    


def add_session(sessions):
    

    print("\n--- Add Study Session ---")

    subject = input("Enter subject name: ").strip()
    topic = input("Enter topic covered: ").strip()
    date = input("Enter date/day label: ").strip()

    # Keep asking until the user enters a positive number.
    while True:
        try:
            duration = float(input("Enter duration in minutes: "))

            if duration <= 0:
                print("Duration must be a positive number.")
            else:
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

    session = {
        "subject": subject,
        "topic": topic,
        "date": date,
        "duration": duration
    }

    sessions.append(session)

    print("Study session added successfully!")


def display_session(session):
    """Display one study session in a formatted table row."""
    classification = classify_session(session["duration"])

    print(
        f"{session['subject']:<20}"
        f"{session['topic']:<30}"
        f"{session['date']:<15}"
        f"{session['duration']:<12.1F}"
        f"{classification:<10}"
        
    )


def print_table_header():
    """Display the heading for the study-session table."""
    print("-" * 87)
    print(
        f"{'Subject':<20}"
        f"{'Topic':<30}"
        f"{'Date/Day':<15}"
        f"{'Minutes':<12}"
        f"{'Class':<10}"
    )
    print("-" * 87)




# ****************************************************************
# Third Function: view_session()
# view all recorded study sessions
# ****************************************************************





def view_sessions(sessions):
    

    print("\n--- All Study Sessions ---")

    if not sessions:
        print("No study sessions have been recorded yet.")
        return

    print_table_header()

    for session in sessions:
        display_session(session)

    print("-" * 87)



# ****************************************************************
# Fourth Function: search_by_subject()
# searches for study sessions by subject.
# search is not case-sensetive.
# ****************************************************************



def search_by_subject(sessions):
    
    """Search for study sessions by subject without case sensitivity."""

    print("\n--- Search Sessions by Subject ---")

    subject = input("Enter subject to search: ").strip()




    # Convert both values to lowercase for case-insensitive matching.
    matching_sessions = [
        session for session in sessions
        if session["subject"].lower() == subject.lower()
    ]

    if not matching_sessions:
        print(f"No study sessions found for '{subject}'.")
        return

    print(f"\nSessions for: {subject}")
    print_table_header()

    total_minutes = 0

    for session in matching_sessions:
        display_session(session)
        total_minutes += session["duration"]

    print("-" * 87)
    print(f"Total time spent on {subject}: {total_minutes:.1f} minutes")
    print(f"Equivalent hours: {total_minutes / 60:.2f} hours")





# ****************************************************************
# fifth function: study_statistics()
# calculates overall  subject statistics.
# ****************************************************************




def study_statistics(sessions):
    """Calculate and display overall study statistics."""

    print("\n--- Study Statistics ---")

    if not sessions:
        print("No study sessions available for analysis.")
        return

    # Total study time in minutes.
    total_minutes = sum(session["duration"] for session in sessions)

    print(f"\nTotal hours studied overall: {total_minutes / 60:.2f} hours")

    # Calculate total study time for each subject.
    subject_totals = {}

    for session in sessions:
        subject = session["subject"]
        subject_totals[subject] = (
            subject_totals.get(subject, 0) + session["duration"]
        )

    print("\nTotal hours studied per subject:")

    for subject, minutes in subject_totals.items():
        print(f"  {subject:<25} {minutes / 60:.2f} hours")

    # Find the subject with the least amount of study time.
    weakest_subject = min(subject_totals, key=subject_totals.get)
    weakest_time = subject_totals[weakest_subject]

    print(
        f"\nSubject with least study time: "
        f"{weakest_subject} ({weakest_time / 60:.2f} hours)"
    )

    # Find the single longest study session.
    longest_session = max(sessions, key=lambda session: session["duration"])

    print("\nSingle longest study session:")
    print(f"  Subject: {longest_session['subject']}")
    print(f"  Topic: {longest_session['topic']}")
    print(f"  Date/Day: {longest_session['date']}")
    print(f"  Duration: {longest_session['duration']:.1f} minutes")
    print(f"  Classification: "
          f"{classify_session(longest_session['duration'])}")



# ****************************************************************
# sixth Function: save_ session()
# save all session to study_log.txt.
# ****************************************************************

def save_sessions(sessions):
    

    try:
        with open("study_log.txt", "w") as file:

            for session in sessions:
                
                file.write(
                    f"{session['subject']}|"
                    f"{session['topic']}|"
                    f"{session['date']}|"
                    f"{session['duration']}\n"
                )

        print(f"\nSessions saved successfully .")

    except OSError as error:
        print(f"Error saving sessions: {error}")





# ****************************************************************
# seventh Functions: load_sessions()
# Loads previously saved sessions  from study_log.txt.
# ****************************************************************





def load_sessions():
    """Load previously saved sessions from study_log.txt."""

    sessions = []

    try:
        with open("study_log.txt", "r") as file:

            for line in file:
                line = line.strip()

                if not line:
                    continue

                parts = line.split("|")

                # Make sure the saved record has all four fields.
                if len(parts) != 4:
                    continue

                subject, topic, date, duration = parts

                try:
                    duration = float(duration)

                    sessions.append({
                        "subject": subject,
                        "topic": topic,
                        "date": date,
                        "duration": duration
                    })

                except ValueError:
                    # Ignore corrupted records instead of crashing.
                    continue

        print(f"{len(sessions)} saved session(s) loaded.")

    except FileNotFoundError:
        # This is normal during the first run.
        print("No previous study log found. Starting with an empty planner.")

    except OSError as error:
        print(f"Could not load study log: {error}")

    return sessions


def display_menu():
    """Display the main program menu."""

    print("\n" + "&" * 50)
    print("          SMART STUDY PLANNER")
    print("&" * 50)
    print("1. Add a study session")
    print("2. View all sessions")
    print("3. Search sessions by subject")
    print("4. View statistics")
    print("5. Save and exit")
    print("&" * 50)




# ****************************************************************
# Eigth Functions: main()
# contols the entire program
# *************************************************************




def main():
    
    

    # load existing sessions when the program starts.
    sessions = load_sessions()

    print("             *******************************************************")
    print("             **           SMART STUDY PLANNER                     **")
    print("             **          Your personal study companion            **")
    print("             *******************************************************")

    


    # continue displaying the menu until the user exits
    while True:
        display_menu()

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_session(sessions)

        elif choice == "2":
            view_sessions(sessions)

        elif choice == "3":
            search_by_subject(sessions)

        elif choice == "4":
            study_statistics(sessions)

        elif choice == "5":
            save_sessions(sessions)
            print("Thank you for using Smart Study Planner!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 5.")


# Program entry point
if __name__ == "__main__":
    main()
