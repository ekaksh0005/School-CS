import datetime
import json
import os

HISTORY_FILE = "user_history.txt"
QUIZ_SCORES_FILE = "quiz_scores.json"
STATS_FILE = "app_statistics.json"

def log_activity(activity, details=""):
    """Log user activity with timestamp"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {activity}"
    if details:
        log_entry += f" - {details}"
    log_entry += "\n"
    
    try:
        with open(HISTORY_FILE, "a", encoding="utf-8") as file:
            file.write(log_entry)
    except Exception as e:
        print(f"Error logging activity: {e}")

def save_quiz_score(score, total_questions):
    """Save quiz score to JSON file"""
    try:
       
        if os.path.exists(QUIZ_SCORES_FILE):
            with open(QUIZ_SCORES_FILE, "r", encoding="utf-8") as file:
                scores = json.load(file)
        else:
            scores = {"quiz_attempts": []}
        
      
        quiz_attempt = {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "score": score,
            "total_questions": total_questions,
            "percentage": round((score / total_questions) * 100, 2)
        }
        scores["quiz_attempts"].append(quiz_attempt)
        
       
        with open(QUIZ_SCORES_FILE, "w", encoding="utf-8") as file:
            json.dump(scores, file, indent=2)
            
    except Exception as e:
        print(f"Error saving quiz score: {e}")

def update_app_statistics(feature_used):
    """Update app usage statistics"""
    try:
        
        if os.path.exists(STATS_FILE):
            with open(STATS_FILE, "r", encoding="utf-8") as file:
                stats = json.load(file)
        else:
            stats = {
                "total_sessions": 0,
                "feature_usage": {
                    "race_results": 0,
                    "quiz": 0,
                    "driver_teams": 0,
                    "circuit_info": 0
                },
                "first_use": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        
       
        stats["total_sessions"] += 1
        if feature_used in stats["feature_usage"]:
            stats["feature_usage"][feature_used] += 1
        stats["last_use"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
       
        with open(STATS_FILE, "w", encoding="utf-8") as file:
            json.dump(stats, file, indent=2)
            
    except Exception as e:
        print(f"Error updating statistics: {e}")

def view_user_history():
    """Display user history from log file"""
    print("\n=== USER HISTORY ===")
    try:
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, "r", encoding="utf-8") as file:
                lines = file.readlines()
                if lines:
                    
                    recent_entries = lines[-20:] if len(lines) > 20 else lines
                    for line in recent_entries:
                        print(line.strip())
                else:
                    print("No history found.")
        else:
            print("No history file found.")
    except Exception as e:
        print(f"Error reading history: {e}")

def view_quiz_statistics():
    """Display quiz statistics"""
    print("\n=== QUIZ STATISTICS ===")
    try:
        if os.path.exists(QUIZ_SCORES_FILE):
            with open(QUIZ_SCORES_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
                attempts = data.get("quiz_attempts", [])
                
                if attempts:
                    print(f"Total Quiz Attempts: {len(attempts)}")
                    scores = [attempt["score"] for attempt in attempts]
                    percentages = [attempt["percentage"] for attempt in attempts]
                    
                    print(f"Average Score: {sum(scores) / len(scores):.1f}")
                    print(f"Average Percentage: {sum(percentages) / len(percentages):.1f}%")
                    print(f"Best Score: {max(scores)}")
                    print(f"Best Percentage: {max(percentages):.1f}%")
                    
                    print("\nRecent Attempts:")
                    for attempt in attempts[-5:]:  
                        print(f"  {attempt['timestamp']}: {attempt['score']}/{attempt['total_questions']} ({attempt['percentage']}%)")
                else:
                    print("No quiz attempts found.")
        else:
            print("No quiz statistics found.")
    except Exception as e:
        print(f"Error reading quiz statistics: {e}")

def view_app_statistics():
    """Display app usage statistics"""
    print("\n=== APP STATISTICS ===")
    try:
        if os.path.exists(STATS_FILE):
            with open(STATS_FILE, "r", encoding="utf-8") as file:
                stats = json.load(file)
                
                print(f"Total Sessions: {stats.get('total_sessions', 0)}")
                print(f"First Use: {stats.get('first_use', 'Unknown')}")
                print(f"Last Use: {stats.get('last_use', 'Unknown')}")
                
                print("\nFeature Usage:")
                feature_usage = stats.get("feature_usage", {})
                for feature, count in feature_usage.items():
                    print(f"  {feature.replace('_', ' ').title()}: {count} times")
        else:
            print("No app statistics found.")
    except Exception as e:
        print(f"Error reading app statistics: {e}")

def race_results():
    log_activity("Accessed Race Results")
    update_app_statistics("race_results")
    
    print("Congrats! You have chosen Formula 1 Race Results")
    print("Data for 2024 Season available. Rest season results coming soon :)")

    calendar = {
        1: "Bahrain International Circuit (Bahrain) ",
        2: "Jeddah Corniche Circuit (Jeddah) ",
        3: "Albert Park Grand Prix Circuit (Australia)",
        4: "Suzuka Circuit (Japan)",
        5: "Shangai International Circuit (China)",
        6: "Miami International Autodrome (Miami)",
        7: "Autodromo Internationale Enzo e Dino Ferrari (Emilia - Romagna)",
        8: "Circuit de Monaco (Monaco)",
        9: "Circuit Gilles-Villeneuve Montrael (Canada)",
        10: "Circuit de Barcelona-Catalunya (Spain)",
        11: "Red Bull Ring (Austria)",
        12: "Silverstone Circuit (Great Britain)",
        13: "Hungaroring, Budapest (Hungary)",
        14: "Circuit de Spa-Francochamps (Belgium)",
        15: "Circuit Zandvoort (Netherlands)",
        16: "Autodromo Nazionale Monza (Italy)",
        17: "Baku City Circuit (Azerbaijan)",
        18: "Marina Bay Street Circuit (Singapore)",
        19: "Circuit of the Americas (United States)",
        20: "Autodromo Hermanos Rodriguez (Mexico)",
        21: "Jose Carlos Pace, Sao Paulo (Brazil)",
        22: "Las Vegas Strip Circuit (Las Vegas)",
        23: "Lusial International Circuit (Qatar)",
        24: "Yas Marina Circuit (Abu Dhabi)"
    }
    
    for number, race in calendar.items():
        print(f"{number}. {race}")

    try:
        choice = int(input("Enter the number of the race you want to see results for: "))
        race_name = calendar.get(choice, "Unknown Race")
        log_activity("Viewed Race Results", f"Race {choice}: {race_name}")
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if choice == 1:
        print("Giro di Imola (Italy)")
        print("Top 10 Finishers:")
        results = [
            "1. Max Verstappen (Red Bull Racing Honda)",
            "2. Lewis Hamilton (Mercedes AMG Petronas)",
            "3. Charles Leclerc (Scuderia Ferrari)",
            "4. Daniel Ricciardo (RB Honda RBPT)",
            "5. Sebastian Vettel (Red Bull Racing Honda)",
            "6. Kimi Raikkonen (Ferrari)",
            "7. Nico Hulkenberg (Hass Ferrari)",
            "8. Fernando Alonso (Aston Martin Aramco Mercedes)",
            "9. Ricciardo Patrese (Williams Mercedes)",
            "10. Kevin Magnussen (Hass Ferrari)"
        ]
        for result in results:
            print(result)
        print("Fastest Lap of the race:")
        print("Max Verstappen - 1:07.472")
        print("Total Laps of the race: 70 Laps")
        print("STC Saudi Arabian Grand Prix (Jeddah Corniche Circuit)")
        print("Top 10 Finishers:")
        results1 = [
            "1. Max Verstappen (Red Bull Racing Honda)",
            "2. Sergio Checo Perez (Red Bull Racing Honda)",
            "3. Charles Leclerc (Scuderia Ferrari)",
            "4. Oscar Piastri (Mclaren Mercedes)",
            "5. Fernando Alonso (Aston Martin Aramco Mercedes)",
            "6. George Russell (Mercedes AMG Petronas)",
            "7. Oliver Bearman (Scuderia Ferrari Substitute)",
            "8. Lando Norris (Mclaren Mercedes)",
            "9. Lewis Hamilton (Mercedes AMG Petronas)",
            "10. Nico Hulkenberg (Hass Ferrari)"
        ]
        for result in results1:
            print(result)

        print("Fastest Lap of the race:")
        print("Charles Leclerc - 1:31.632")
        print("Total Laps of the race: 50 Laps")

    elif choice == 3:
        print("Albert Park Grand Prix Circuit (Australia)")
        print("Top 10 Finishers:")
        results2 = [
            "1. Carlos Sainz (Scuderia Ferarri)",
            "2. Charles Leclerc (Scuderia Ferrari)",
            "3. Lando Norris (Mclaren Mercedes)",
            "4. Oscar Piastri (Mclaren Mercedes)",
            "5. Sergio Checo Perez (Red Bull Racing Honda)",
            "6. Lance Stroll (Aston Martin Aramco Mercedes)",
            "7. Yuki Tsunoda (RB Honda RBPT)",
            "8. Fernando Alonso (Aston Martin Aramco Mercedes)",
            "9. Nico Hulkenberg (Hass Ferrari)",
            "10. Keven Magnussen (Hass Ferrari)"
        ]
        for result in results2:
            print(result)

        print("Fastest Lap of the race:")
        print("Charles Leclerc - 1:19.813")
        print("Total Laps of the race: 58 Laps")

    elif choice == 4:
            print("Suzuka Circuit (Japan)")
            print("Top 10 Finishers:")
            results3 = [
                "1. Max Verstappen (Red Bull Racing Honda)",
                "2. Sergio Checo Perez (Red Bull Racing Honda)",
                "3. Carlos Sainz (Scuderia Ferrari)",
                "4. Charles Leclerc (Scuderia Ferrari)",
                "5. Lando Norris (Mclaren Mercedes)",
                "6. Fernando Alonso (Aston Martin Aramco Mercedes)",
                "7. George Russell(Mercedes AMG Petronas)",
                "8. Oscar Piastri (Mclaren Mercedes)",
                "9. Lewis Hamilton (Mercedes AMG Petronas)",
                "10. Yuki Tsunoda (RB Honda RBPT)"
            ]
            for result in results3:
                print(result)

            print("Fastest Lap of the race:")
            print("Max Verstappen - 1:33.706")
            print("Total Laps of the race: 53 Laps")

    elif choice == 5:
            print("Shangai International Circuit (China)")
            print("Top 10 Finishers:")
            results4 = [
                "1. Max Verstappen (Red Bull Racing Honda)",
                "2. Lando Norris (Mclaren Mercedes)",
                "3. Sergio Checo Perez (Red Bull Racing Honda)",
                "4. Charles Leclerc (Scuderia Ferrari)",
                "5. Carlos Sainz (Scuderia Ferrari)",
                "6. George Russell (Mercedes AMG Petronas)",
                "7. Fernando Alonso (Aston Martin Aramco Mercedes)",
                "8. Oscar Piastri (Mclaren Mercedes)",
                "9. Lewis Hamilton (Mercedes AMG Petronas)",
                "10. Nico Hulkenberg (Hass Ferrari)"
            ]
            for result in results4:
                print(result)
            print("Fastest Lap of the race:")
            print("Fernando Alonso - 1:37.810")
            print("Total Laps of the race: 56 Laps")

    elif choice == 6:
            print("Miami International Autodrome (Miami)")
            print("Top 10 Finishers:")
            results5 = [
                "1. Lando Norris (Mclaren Mercedes)",
                "2. Max Verstappen (Red Bull Racing Honda)",
                "3. Charles Leclerc (Scuderia Ferrari)",
                "4. Sergio Checo Perez (Red Bull Racing Honda)",
                "5. Carlos Sainz (Scuderia Ferrari)",
                "6. Lewis Hamilton (Mercedes AMG Petronas)",
                "7. Yuki Tsunoda (RB Honda RBPT)",
                "8. George Russell (Mercedes AMG Petronas)",
                "9. Fernando Alonso (Aston Martin Aramco Mercedes)",
                "10. Esteban Ocon (Alpine Renault)"
            ]
            for result in results5:
                print(result)
            print("Fastest Lap of the race:")
            print("Lando Norris - 1:30.634")
            print("Total Laps of the race: 57 Laps")

    elif choice == 7:
            print("Autodromo Internationale Enzo e Dino Ferrari (Emilia - Romagna)")
            print("Top 10 Finishers:")
            results6 = [
                "1. Max Verstappen (Red Bull Racing Honda)",
                "2. Lando Norris (Mclaren Mercedes)",
                "3. Charles Leclerc (Scuderia Ferrari)",
                "4. Oscar Piastri (Mclaren Mercedes)",
                "5. Carlos Sainz (Scuderia Ferrari)",
                "6. Lewis Hamilton (Mercedes AMG Petronas)",
                "7. George Russell (Mercedes AMG Petronas)",
                "8. Sergio Checo Perez (Red Bull Racing Honda)",
                "9. Lance Stroll (Aston Martin Aramco Mercedes)",
                "10. Yuki Tsunoda (RB Honda RBPT)"
            ]
            for result in results6:
                print(result)
            print("Fastest Lap of the race:")
            print("Charles Leclerc - 1:32.908")
            print("Total Laps of the race: 63 Laps")


    elif choice == 8:
        print("Circuit de Monaco (Monaco)")
        print("Top 10 Finishers:")
        results7 = [
            "1. Charles Leclerc (Scuderia Ferrari)",
            "2. Oscar Piastri (Mclaren Mercedes)",
            "3. Carlos Sainz (Scuderia Ferrari)",
            "4. Lando Norris (Mclaren Mercedes)",
            "5. George Russell (Mercedes AMG Petronas)",
            "6. Max Verstappen (Red Bull Racing Honda)",
            "7. Lewis Hamilton (Mercedes AMG Petronas)",
            "8. Yuki Tsunoda (RB Honda RBPT)",
            "9. Alexander Albon (Williams Mercedes)",
            "10. Pierre Gasly (Alpine Renault)"
        ]
        for result in results7:
            print(result)
        print("Fastest Lap of the race:")
        print("Lewis Hamilton - 1:14:165")
        print("Total Laps of the race: 78")

    elif choice == 24:
        print("Yas Marina Circuit (Abu Dhabi)")
        print("Top 10 Finishers:")
        results23 = [
            "1. Lando Norris (Mclaren Mercedes)",
            "2. Carlos Sainz (Scuderia Ferrari)",
            "3. Charles Leclerc (Scuderia Ferrari)",
            "4. Lewis Hamilton (Mercedes AMG Petronas)",
            "5. George Russell (Mercedes AMG Petronas)",
            "6. Max Verstappen (Red Bull Racing Honda)",
            "7. Pierre Gasly (Alpine Renault)",
            "8. Nico Hulkenberg (Hass Ferrari)",
            "9. Fernando Alonso (Aston Martin Aramco Mercedes)",
            "10. Oscar Piastri (Mclaren Mercedes)"
        ]
        for result in results23:
            print(result)
        print("Fastest Lap of the race:")
        print("Charles Leclerc - 1:25.637")
        print("Total Laps of the race: 58 Laps")
    else:
        print("Invalid option. Please try again.")


def fun_quiz():
    log_activity("Started Formula 1 Quiz")
    update_app_statistics("quiz")
    
    print("Welcome to the Formula 1 Quiz!")
    print("You will be given 5 questions about the Formula 1 world championship.")
    print("After answering each question, you will be given feedback on your answer.")
    
    score = 0
    total_questions = 5
    questions = [
        ("Who is the 7 time world champion of Formula 1 on the grid?", "lewis hamilton"),
        ("What is the name of the Brazil Legend?", "ayrton senna"),
        ("Who won the 2021 Abu Dhabi Grand Prix?", "max verstappen"),
        ("Who is often called the 'Smooth Operator'?", "carlos sainz"),
        ("What is the famous nickname for the Mclaren Mercedes Formula 1 team?", "papaya")
    ]
    
    user_answers = []
    
    for i, (question, correct_answer) in enumerate(questions, 1):
        print(f"\nQuestion {i}: {question}")
        user_answer = input("Your answer: ").lower().strip()
        user_answers.append(user_answer)
        
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer.title()}")
    
    print(f"\nYour final score: {score}/{total_questions}")
    percentage = (score / total_questions) * 100
    print(f"Percentage: {percentage:.1f}%")
    
   
    log_activity("Completed Formula 1 Quiz", f"Score: {score}/{total_questions} ({percentage:.1f}%)")
    
    
    save_quiz_score(score, total_questions)
    
   
    try:
        quiz_details = {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "score": score,
            "total_questions": total_questions,
            "percentage": percentage,
            "answers": user_answers
        }
        
        with open("detailed_quiz_history.json", "a", encoding="utf-8") as file:
            file.write(json.dumps(quiz_details) + "\n")
    except Exception as e:
        print(f"Error saving detailed quiz history: {e}")


def driver_teams():
    log_activity("Accessed Driver Teams Information")
    update_app_statistics("driver_teams")
    
    print("Formula 1 Driver Teams:")
    teams = [
        "1. Scuderia Ferrari",
        "2. McLaren Mercedes", 
        "3. Oracle Red Bull Racing",
        "4. Mercedes AMG Petronas",
        "5. Stake Kick Sauber",
        "6. BWT Alpine Renault",
        "7. Hass Ferrari",
        "8. RB Honda RBPT",
        "9. Aston Martin Aramco Mercedes",
        "10. Williams Mercedes"
    ]
    
    for team in teams:
        print(team)
    
    try:
        choice2 = int(input("Which team details would you like (1-10): "))
        
        team_info = {
            1: ("Scuderia Ferrari", "1950", "Piero Ferrari and Exor N.V", "Maranello, Italy", "16", "Charles Leclerc and Carlos Sainz", "Frederic Vasseur"),
            2: ("McLaren Mercedes", "1966", "Bahrain Mumtalakat Holding Company and Mclaren", "Woking, United Kingdom", "9", "Lando Norris and Oscar Piastri", "Andrea Stella"),
            3: ("Oracle Red Bull Racing", "1997", "Dietrich Mateschitz", "Milton Keynes, United Kingdom", "6", "Max Verstappen and Sergio Checo Perez", "Christian Horner"),
            4: ("Mercedes AMG Petronas", "1970", "Mercedes Benz and Toto Wolff", "Brackley, United Kingdom", "8", "Lewis Hamilton and George Russell", "Toto Wolff"),
            
        }
        
        if choice2 in team_info:
            name, founded, owners, home, championships, drivers, principal = team_info[choice2]
            print(f"\n{name}:")
            print(f"Founded in {founded}")
            print(f"Current owners: {owners}")
            print(f"Home ground: {home}")
            print(f"Total World Championships: {championships}")
            print(f"Current drivers: {drivers}")
            print(f"Team Principle: {principal}")
            
            log_activity("Viewed Team Information", f"Team: {name}")
        else:
            print("Invalid team selection.")
            
    except ValueError:
        print("Invalid input. Please enter a number between 1-10.")


def Circuit_Information():
    log_activity("Accessed Circuit Information")
    update_app_statistics("circuit_info")
    
    print("Welcome to the Formula 1 Circuit Information Menu!")
    circuit = {
        1: "Bahrain International Circuit (Bahrain) ",
        2: "Jeddah Corniche Circuit (Jeddah) ",
        3: "Albert Park Grand Prix Circuit (Australia)",
        4: "Suzuka Circuit (Japan)",
        5: "Shangai International Circuit (China)",
        6: "Miami International Autodrome (Miami)",
        7: "Autodromo Internationale Enzo e Dino Ferrari (Emilia - Romagna)",
        8: "Circuit de Monaco (Monaco)",
        9: "Circuit Gilles-Villeneuve Montrael (Canada)",
        10: "Circuit de Barcelona-Catalunya (Spain)",
        11: "Red Bull Ring (Austria)",
        12: "Silverstone Circuit (Great Britain)",
        13: "Hungaroring, Budapest (Hungary)",
        14: "Circuit de Spa-Francochamps (Belgium)",
        15: "Circuit Zandvoort (Netherlands)",
        16: "Autodromo Nazionale Monza (Italy)",
        17: "Baku City Circuit (Azerbaijan)",
        18: "Marina Bay Street Circuit (Singapore)",
        19: "Circuit of the Americas (United States)",
        20: "Autodromo Hermanos Rodriguez (Mexico)",
        21: "Jose Carlos Pace, Sao Paulo (Brazil)",
        22: "Las Vegas Strip Circuit (Las Vegas)",
        23: "Lusial International Circuit (Qatar)",
        24: "Yas Marina Circuit (Abu Dhabi)"
    }
    
    for number, race in circuit.items():
        print(f"{number}. {race}")

    try:
        choice = int(input("Enter the number of the circuit you want to see information for: "))
        circuit_name = circuit.get(choice, "Unknown Circuit")
        log_activity("Viewed Circuit Information", f"Circuit {choice}: {circuit_name}")
        
        
        circuit_info = {
            1: {
                "name": "Bahrain International Circuit",
                "location": "Bahrain",
                "length": "5.412 Km",
                "first_race": "2004",
                "details": "You can usually expect great racing and decent amounts of overtaking in Bahrain...",
                "lap_record": "Pedro de la Rosa (2005) : 1:31:447"
            },
            8: {
                "name": "Circuit de Monaco",
                "location": "Monaco", 
                "length": "3.337 Km",
                "first_race": "1950",
                "details": "Circuit de Monaco is a very popular circuit in Monaco...",
                "lap_record": "Lewis Hamilton (2018): 1:12:077"
            }
        }
        
        if choice in circuit_info:
            info = circuit_info[choice]
            print(f"\nYou have chosen {info['name']}")
            print(f"Location: {info['location']}")
            print(f"Length: {info['length']}")
            print(f"Date of first race: {info['first_race']}")
            print(f"Details: {info['details']}")
            print(f"Lap Record: {info['lap_record']}")
        else:
            print("Circuit information not available for this selection.")
            
    except ValueError:
        print("Invalid input. Please enter a number.")


def export_data():
    """Export all user data to a summary file"""
    print("\nExporting user data...")
    
    try:
        with open("user_data_export.txt", "w", encoding="utf-8") as export_file:
            export_file.write("=== FORMULA 1 HUB - USER DATA EXPORT ===\n")
            export_file.write(f"Export Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            
            export_file.write("=== USER HISTORY ===\n")
            if os.path.exists(HISTORY_FILE):
                with open(HISTORY_FILE, "r", encoding="utf-8") as history_file:
                    export_file.write(history_file.read())
            else:
                export_file.write("No history found.\n")
            
            export_file.write("\n=== QUIZ STATISTICS ===\n")
            if os.path.exists(QUIZ_SCORES_FILE):
                with open(QUIZ_SCORES_FILE, "r", encoding="utf-8") as quiz_file:
                    quiz_data = json.load(quiz_file)
                    export_file.write(json.dumps(quiz_data, indent=2))
            else:
                export_file.write("No quiz data found.\n")
            
            export_file.write("\n\n=== APP STATISTICS ===\n")
            if os.path.exists(STATS_FILE):
                with open(STATS_FILE, "r", encoding="utf-8") as stats_file:
                    stats_data = json.load(stats_file)
                    export_file.write(json.dumps(stats_data, indent=2))
            else:
                export_file.write("No app statistics found.\n")
        
        print("Data exported successfully to 'user_data_export.txt'")
        log_activity("Exported User Data", "All data exported to user_data_export.txt")
        
    except Exception as e:
        print(f"Error exporting data: {e}")



def main():
    print("Welcome to the Formula 1 Hub!")
    log_activity("Started Formula 1 Hub Application")
    
    while True:
        print("\n" + "="*50)
        print("FORMULA 1 HUB - MAIN MENU")
        print("="*50)
        print("1. Race Results")
        print("2. Fun Quiz on Formula 1")
        print("3. Driver and Team Statistics")
        print("4. Circuit Information")
        print("5. View User History")
        print("6. View Quiz Statistics")
        print("7. View App Statistics")
        print("8. Export All Data")
        print("9. Exit")
        print("="*50)
        
        choice1 = input("Enter your choice (1-9): ").strip()

        if choice1 == "1":
            race_results()
        elif choice1 == "2":
            fun_quiz()
        elif choice1 == "3":
            driver_teams()
        elif choice1 == "4":
            Circuit_Information()
        elif choice1 == "5":
            view_user_history()
        elif choice1 == "6":
            view_quiz_statistics()
        elif choice1 == "7":
            view_app_statistics()
        elif choice1 == "8":
            export_data()
        elif choice1 == "9":
            log_activity("Exited Formula 1 Hub Application")
            print("Thank you for using the Formula 1 Hub!")
            print("All your activity has been logged. Come back soon!")
            break
        else:
            print("Invalid Option. Please Try Again")
            log_activity("Invalid Menu Selection", f"Selected: {choice1}")

if __name__ == "__main__":
    main()