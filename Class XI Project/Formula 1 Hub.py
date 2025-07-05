def race_results():
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

        choice = int(input("Enter the number of the race you want to see results for: "))

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

        elif choice == 9:
            print("Circuit Gilles Villeneuve (Canada)")
            print("Top 10 Finishers:")
            results8 = [
                "1. Max Verstappen (Red Bull Racing Honda)",
                "2. Lando Norris (Mclaren Mercedes)",
                "3. George Russell (Mercedes AMG Petronas)",
                "4. Lewis Hamilton (Mercedes AMG Petronas)",
                "5. Oscar Piastri (Mclaren Mercedes)",
                "6. Fernando Alonso (Aston Martin Aramco Mercedes)",
                "7. Lance Stroll (Aston Martin Aramco Mercedes)",
                "8. Daniel Ricciardo (RB Honda RBPT)",
                "9. Pierre Gasly (Alpine Renault)",
                "10. Esteban Ocon (Alpine Renault)"
            ]
            for result in results8:
                print(result)
            print("Fastest Lap of the race:")
            print("Lewis Hamilton - 1:14.856")
            print("Total Laps of the race: 70 Laps")

        elif choice == 10:
            print("Circuit de Barcelona-Catalunya (Spain)")
            print("Top 10 Finishers:")
            results9 = [
                "1. Max Verstappen (Red Bull Racing Honda)",
                "2. Lando Norris (Mclaren Mercedes)",
                "3. Lewis Hamilton (Mercedes AMG Petronas)",
                "4. George Russell (Mercedes AMG Petronas)",
                "5. Charles Leclerc (Scuderia Ferrari)",
                "6. Carlos Sainz (Scuderia Ferrari)",
                "7. Oscar Piastri (Mclaren Mercedes)",
                "8. Sergio Checo Perez (Red Bull Racing Honda)",
                "9. Pierre Gasly (Alpine Renault)",
                "10. Esteban Ocon (Alpine Renault)"
            ]
            for result in results9:
                print(result)
            print("Fastest Lap of the race:")
            print("Lando Norris - 1:17.115")
            print("Total Laps of the race: 66 Laps")

        elif choice == 11:
            print("Red Bull Ring (Austria)")
            print("Top 10 Finishers:")
            results10 = [
                "1. George Russell (Mercedes AMG Petronas)",
                "2. Oscar Piastri (Mclaren Mercedes)",
                "3. Carlos Sainz (Scuderia Ferrari)",
                "4. Lewis Hamilton (Mercedes AMG Petronas)",
                "5. Max Verstappen (Red Bull Racing Honda)",
                "6. Nico Hulkenberg (Hass Ferrari)",
                "7. Sergio Checo Perez (Red Bull Racing Honda)",
                "8. Kevin Magnussen (Hass Ferrari)",
                "9. Daniel Ricciardo (RB Honda RBPT)",
                "10. Pierre Gasly (Alpine Renault)"
            ]
            for result in results10:
                print(result)
            print("Fastest Lap of the race:")
            print("Fernando Alonso - 1:07.694")
            print("Total Laps of the race: 71 Laps")

        elif choice == 12:
            print("Silverstone Circuit (Great Britain)")
            print("Top 10 Finishers:")
            results11 = [
                "1. Lewis Hamilton (Mercedes AMG Petronas)",
                "2. Max Verstappen (Red Bull Racing Honda)",
                "3. Lando Norris (Mclaren Mercedes)",
                "4. Oscar Piastri (Mclaren Mercedes)",
                "5. Carlos Sainz (Scuderia Ferrari)",
                "6. Nico Hulkenberg (Hass Ferrari)",
                "7. Lance Stroll (Aston Martin Aramco Mercedes)",
                "8. Fernando Alonso (Aston Martin Aramco Mercedes)",
                "9. Alexander Albon (Williams Mercedes )",
                "10. Yuki Tsunoda (RB Honda RBPT)"
            ]
            for result in results11:
                print(result)
            print("Fastest Lap of the race:")
            print("Carlos Sainz - 1:28.293")
            print("Total Laps of the race: 52 Laps")

        elif choice == 13:
            print("Hungaroring Circuit (Hungary)")
            print("Top 10 Finishers:")
            results12 = [
                "1. Oscar Piastri (Mclaren Mercedes)",
                "2. Lando Norris (Mclaren Mercedes)",
                "3. Lewis Hamilton (Mercedes AMG Petronas)",
                "4. Charles Leclerc (Scuderia Ferrari)",
                "5. Max Verstappen (Red Bull Racing Honda)",
                "6. Carlos Sainz (Scuderia Ferrari)",
                "7. Sergio Checo Perez (Red Bull Racing Honda)",
                "8. George Russell (Mercedes AMG Petronas)",
                "9. Yuki Tsunoda (RB Honda RBPT)",
                "10. Lance Stroll (Aston Martin Aramco Mercedes)"
            ]
            for result in results12:
                print(result)
            print("Fastest Lap of the race:")
            print("George Russell - 1:20.305")
            print("Total Laps of the race: 70 Laps")

        elif choice == 14:
            print("Circuit de Spa-Francochamps (Belgium)")
            print("Top 10 Finishers:")
            results13 = [
                "1. Lewis Hamilton (Mercedes AMG Petronas)",
                "2. Oscar Piastri (Mclaren Mercedes)",
                "3. Charles Leclerc (Scuderia Ferrari)",
                "4. Max Verstappen (Red Bull Racing Honda)",
                "5. Lando Norris (Mclaren Mercedes)",
                "6. Carlos Sainz (Scuderia Ferrari)",
                "7. Sergio Checo Perez (Red Bull Racing Honda)",
                "8. Fernando Alonso (Aston Martin Aramco Mercedes)",
                "9. Esteban Ocon (Alpine Renault)",
                "10. Danial Ricciardo (RB Honda RBPT)"
            ]
            for result in results13:
                print(result)
            print("Fastest Lap of the race:")
            print("Sergio Checo Perez - 1:44.701")
            print("Total Laps of the race: 44 Laps")

        elif choice == 15:
            print("Circuit Zandvoort (Netherlands)")
            print("Top 10 Finishers:")
            results14 = [
                "1. Lando Norris (Mclaren Mercedes)",
                "2. Max Verstappen (Red Bull Racing Honda)",
                "3. Charles Leclerc (Scuderia Ferrari)",
                "4. Oscar Piastri (Mclaren Mercedes)",
                "5. Charles Leclerc (Scuderia Ferrari)",
                "6. Sergio Checo Perez (Red Bull Racing Honda)",
                "7. George Russell (Mercedes AMG Petronas)",
                "8. Lewis Hamilton (Mercedes AMG Petronas)",
                "9. Pierre Gasly (Alpine Renault)",
                "10. Fernando Alonso (Aston Martin Aramco Mercedes)"
            ]
            for result in results14:
                print(result)
            print("Fastest Lap of the race:")
            print("Lando Norris - 1:13.817")
            print("Total Laps of the race: 72 Laps")

        elif choice == 16:
            print("Autodromo Nazionale Monza (Italy)")
            print("Top 10 Finishers:")
            results15 = [
                "1. Charles Leclerc (Scuderia Ferrari)",
                "2. Oscar Piastri (Mclaren Mercedes)",
                "3. Lando Norris (Mclaren Mercedes)",
                "4. Carlos Sainz (Scuderia Ferrari)",
                "5. Lewis Hamilton (Mercedes AMG Petronas)",
                "6. Max Verstappen (Red Bull Racing Honda)Carlos Sainz (Scuderia Ferrari)",
                "7. George Russell (Mercedes AMG Petronas)",
                "8. Sergio Checo Perez (Red Bull Racing Honda)",
                "9. Alexander Albon (Williams Mercedes)",
                "10. Kevin Magnussen (Hass Ferrari)"
            ]
            for result in results15:
                print(result)
            print("Fastest Lap of the race:")
            print("Lando Norris - 1:21.432")
            print("Total Laps of the race: 53 Laps")

        elif choice == 17:
            print("Baku City Circuit (Azerbaijan)")
            print("Top 10 Finishers:")
            results16 = [
                "1. Oscar Piastri (Mclaren Mercedes)",
                "2. Charles Leclerc (Scuderia Ferrari)Lando Norris (Mclaren Mercedes)",
                "3. George Russell (Mercedes AMG Petronas)",
                "4. Lando Norris (Mclaren Mercedes)",
                "5. Max Verstappen (Red Bull Racing Honda)",
                "6. Fernando Alonso (Aston Martin Aramco Mercedes)",
                "7. Alexander Albon (Williams Mercedes)",
                "8. Franco Colapinto (Williams Mercedes)",
                "9. Lewis Hamilton (Mercedes AMG Petronas)",
                "10. Oliver Bearman (Hass Ferrari)"
            ]
            for result in results16:
                print(result)
            print("Fastest Lap of the race:")
            print("Lando Norris - 1:45.255")
            print("Total Laps of the race: 51 Laps")

        elif choice == 18:
            print("Marina Bay Street Circuit (Singapore)")
            print("Top 10 Finishers:")
            results17 = [
                "1. Lando Norris (Mclaren Mercedes)",
                "2. Max Verstappen (Red Bull Racing Honda)",
                "3. Oscar Piastri (Mclaren Mercedes)",
                "4. George Russell (Mercedes AMG Petronas)",
                "5. Charles Leclerc (Scuderia Ferrari)",
                "6. Lewis Hamilton (Mercedes AMG Petronas)",
                "7. Carlos Sainz (Scuderia Ferrari)",
                "8. Fernando Alonso (Aston Martin Aramco Mercedes)",
                "9. Nico Hulkenberg (Hass Ferrari)",
                "10. Sergio Checo Perez (Red Bull Racing Honda)"
            ]
            for result in results17:
                print(result)
            print("Fastest Lap of the race:")
            print("Daniel Ricciardo - 1:34.486")
            print("Total Laps of the race: 62 Laps")

        elif choice == 19:
            print("Circuit of the Americas (United States)")
            print("Top 10 Finishers:")
            results18 = [
                "1. Charles Leclerc (Scuderia Ferrari)",
                "2. Carlos Sainz (Scuderia Ferrari)",
                "3. Max Verstappen (Red Bull Racing Honda)",
                "4. Lando Norris (Mclaren Mercedes)",
                "5. Oscar Piastri (Mclaren Mercedes)",
                "6. George Russell (Mercedes AMG Petronas)",
                "7. Sergio Checo Perez (Red Bull Racing Honda)",
                "8. Nico Hulkenberg (Hass Ferrari)",
                "9. Liam Lawson (RB Honda RBPT)",
                "10. Franco Colapinto (Williams Mercedes)"
            ]
            for result in results18:
                print(result)
            print("Fastest Lap of the race:")
            print("Esteban Ocon - 1:37.330")
            print("Total Laps of the race: 56 Laps")

        elif choice == 20:
            print("Autodromo Hermanos Rodriguez (Mexico)")
            print("Top 10 Finishers:")
            results19 = [
                "1. Carlos Sainz (Scuderia Ferrari)",
                "2. Lando Norris (Mclaren Mercedes)",
                "3. Charles Leclerc (Scuderia Ferrari)",
                "4. Lewis Hamilton (Mercedes AMG Petronas)",
                "5. George Russell (Mercedes AMG Petronas)",
                "6. Max Verstappen (Red Bull Racing Honda)",
                "7. Kevin Magnussen (Hass Ferrari)",
                "8. Oscar Piastri (Mclaren Mercedes)",
                "9. Nico Hulkenberg (Hass Ferrari)",
                "10. Pierre Gasly (Alpine Renault)"
            ]
            for result in results19:
                print(result)
            print("Fastest Lap of the race:")
            print("Charles Leclerc - 1:18.336")
            print("Total Laps of the race: 71 Laps")

        elif choice == 21:
            print("Jose Carlos Pace, Sao Paulo (Brazil)")
            print("Top 10 Finishers:")
            results20 = [
                "1. Max Verstappen (Red Bull Racing Honda)",
                "2. Esteban Ocon (Alpine Renault)",
                "3. Pierre Gasly (Alpine Renault)",
                "4. George Russell (Mercedes AMG Petronas)",
                "5. Charles Leclerc (Scuderia Ferrari)",
                "6. Lando Norris (Mclaren Mercedes)",
                "7. Yuki Tsunoda (RB Honda RBPT)",
                "8. Oscar Piastri (Mclaren Mercedes)",
                "9. Liam Lawson (RB Honda RBPT)",
                "10. Lewis Hamilton (Mercedes AMG Petronas)"
            ]
            for result in results20:
                print(result)
            print("Fastest Lap of the race:")
            print("Max Verstappen - 1:20.472")
            print("Total Laps of the race: 69 Laps")

        elif choice == 22:
            print("Las Vegas Strip Circuit (Las Vegas)")
            print("Top 10 Finishers:")
            results21 = [
                "1. George Russell (Mercedes AMG Petronas)",
                "2. Lewis Hamilton (Mercedes AMG Petronas)",
                "3. Carlos Sainz (Scuderia Ferrari)",
                "4. Charles Leclerc (Scuderia Ferrari)",
                "5. Max Verstappen (Red Bull Racing Honda)",
                "6. Lando Norris (Mclaren Mercedes)",
                "7. Oscar Piastri (Mclaren Mercedes)",
                "8. Nico Hulkenberg (Hass Ferrari)",
                "9. Yuki Tsunoda (RB Honda RBPT)",
                "10. Sergio Checo Perez (Red Bull Racing Honda)"
            ]
            for result in results21:
                print(result)
            print("Fastest Lap of the race:")
            print("Lando Norris - 1:34.876")
            print("Total Laps of the race: 50 Laps")

        elif choice == 23:
            print("Lusial International Circuit (Qatar)")
            print("Top 10 Finishers:")
            results22 = [
                "1. Max Verstappen (Red Bull Racing Honda)",
                "2. Charles Leclerc (Scuderia Ferrari)",
                "3. Oscar Piastri (Mclaren Mercedes)",
                "4. George Russell (Mercedes AMG Petronas)",
                "5. Pierre Gasly (Alpine Renault)",
                "6. Carlos Sainz (Scuderia Ferrari)",
                "7. Fernando Alonso (Aston Martin Aramco Mercedes)",
                "8. Zhou Guanyu (Kick Sauber Ferrari)",
                "9. Kevin Magnussen (Hass Ferrari)",
                "10. Lando Norris (Mclaren Mercedes)"
            ]
            for result in results22:
                print(result)
            print("Fastest Lap of the race:")
            print("Lando Norris - 1:22.384")
            print("Total Laps of the race: 57 Laps")

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
    print("Welcome to the Formula 1 Quiz!")
    print("You will be given 5 questions about the Formula 1 world championship.")
    print("After answering each question, you will be given feedback on your answer.")
    
    score = 0
    questions = [
        ("Who is the 7 time world champion of Formula 1 on the grid?", "lewis hamilton"),
        ("What is the name of the Brazil Legend?", "ayrton senna"),
        ("Who won the 2021 Abu Dhabi Grand Prix?", "max verstappen"),
        ("Who is often called the 'Smooth Operator'?", "carlos sainz"),
        ("What is the famous nickname for the Mclaren Mercedes Formula 1 team?", "papaya")
    ]
    
    for question, answer in questions:
        print(question)
        user_answer = input("Your answer: ").lower()
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {answer.title()}")
            score -= 1
    
    print("Your score:", score)

def driver_teams():
    print("Formula 1 Driver Teams:")
    print("1. Scuderia Ferrari")
    print("2. McLaren Mercedes")
    print("3. Oracle Red Bull Racing")
    print("4. Mercedes AMG Petronas")
    print("5. Stake Kick Sauber")
    print("6. BWT Alpine Renault")
    print("7. Hass Ferrari")
    print("8. RB Honda RBPT")
    print("9. Aston Martin Aramco Mercedes")
    print("10. Williams Mercedes")
    choice2 = ("Which team details would you like:")
    if choice2 == 1:
        print("Scuderia Ferrari:")
        print("Founded in 1950")
        print("Current owners: Piero Ferrari and Exor N.V")
        print("Home ground: Maranello, Italy")
        print("Total World Championships: 16 ")
        print("Current drivers: Charles Leclerc and Carlos Sainz")
        print("Team Principle: Frederic Vasseur")
    elif choice2 == 2:
        print("McLaren Mercedes:")
        print("Founded in 1966")
        print("Current owners: Bahrain Mumtalakat Holding Company and Mclaren")
        print("Home ground: Woking, United Kingdom")
        print("Total World Championships: 9")
        print("Current drivers: Lando Norris and Oscar Piastri")
        print("Team Principle: Andrea Stella")
    elif choice2 == 3:
        print("Oracle Red Bull Racing:")
        print("Founded in 1997")
        print("Current owners: Dietrich Mateschitz")
        print("Home ground: Milton Keynes, United Kingdom")
        print("Total World Championships: 6")
        print("Current drivers: Max Verstappen and Sergio Checo Perez")
        print("Team Principle: Christian Horner")
    elif choice2 == 4:
        print("Mercedes AMG Petronas:")
        print("Founded in 1970")
        print("Current owners: Mercedes Benz and Toto Wolff")
        print("Home ground: Brackley, United Kingdom")
        print("Total World Championships: 8")
        print("Current drivers: Lewis Hamilton and George Russell")
        print("Team Principle: Toto Wolff")
    elif choice2 == 5:
        print("Stake Kick Sauber:")
        print("Founded in 1993")
        print("Current owners: Audi and Qatar")
        print("Home ground: Hinwil, Switzerland")
        print("Total World Championships: 0")
        print("Current drivers: Vallteri Bottas and Guanyu Zhou")
        print("Team Principle: Alessandro Alunni Bravi")
    elif choice2 == 6:
        print("BWT Alpine Renault:")
        print("Founded in 1986")
        print("Current owners: Renault and Renault-Nissan")
        print("Home ground: Enstone, United Kingdom")
        print("Total World Championships: 2")
        print("Current drivers: Pierre Gasly and Jack Doohan")
        print("Team Principle: Oliver Oakes")
    elif choice2 == 7:
        print("Hass Ferrari:")
        print("Founded in 2016")
        print("Current owners: Gene Hass")
        print("Home ground: Kannapolis, United States")
        print("Total World Championships: 0")
        print("Current drivers: Nico Hulkenberg and Kevin Magnussen")
        print("Team Principle: Ayao Komatsu")
    elif choice2 == 8:
        print("Visa Cash App RB:")
        print("Founded in 1985")
        print("Current owners: Red Bull Gmbh")
        print("Home ground: Faenza, Italy")
        print("Total World Championships: 0")
        print("Current drivers: Yuki Tsunoda and Liam Lawson")
        print("Team Principle: Laurent Mekies")
    elif choice2 == 9:
        print("Aston Martin Aramco Mercedes:")
        print("Founded in 2018")
        print("Current owners: Lawrence Stroll")
        print("Home ground: Silverston, United Kingdom")
        print("Total World Championships: 0")
        print("Current drivers: Fernando Alonso and Lance Stroll")
        print("Team Principle: Mike Krack")
    elif choice2 == 10:
        print("Williams Racing:")
        print("Founded in 1978")
        print("Current owners: Dorliton Capital")
        print("Home ground: Grove, United Kingdom")
        print("Total World Championships: 9")
        print("Current drivers: Alexander Alon and  Franco Colapinto")
        print("Team Principle: James Vowles")

def Circuit_Information():
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

    choice = int(input("Enter the number of the circuit you want to see information for: "))
    if choice == 1:
        print("You have chosen Bahrain International circuit")
        print("Location: Bahrain")
        print("Length: 5.412 Km")
        print("Date of first race: 2004")
        print("Details: You can usually expect great racing and decent amounts of overtaking in Bahrain, while the drivers have to contend with wind, racing under floodlights and the difficulty of finding a decent set-up with the wide temperature fluctuations between sessions. The track’s most challenging point is the tight, downhill, off-camber Turn 10 left-hander, while the fast run through Turn 12 is another highlight, allowing the racers to really feel their cars coming alive.")
        print("Lap Record: Pedro de la Rosa (2005) : 1:31:447")
    elif choice == 2:
        print("You have chosen Jeddah Corniche Circuit")
        print("Location: Jeddah")
        print("Length: 6.174 Km")
        print("Date of first race: 2021")
        print("Details: Fast. Very fast. Average speeds around the Jeddah Corniche Circuit are around 250km/h – quicker than those at Silverstone, and second on the 2021 calendar only to Monza – aka ‘The Temple of Speed’. It is, quite simply, the fastest street circuit ever seen in Formula 1 – while the track also features the most corners on the calendar with 27, many of them quick, sinuous bends as the drivers wend their way along the Jeddah waterfront.")
        print("Lap Record: Lewis Hamilton (2021) : 1:30:734")
    elif choice == 3:
        print("You have chosen Albert Park Grand Prix Circuit")
        print("Location: Australia")
        print("Length: 5.278 Km")
        print("Date of first race: 1996")
        print("Details: The Albert Park Grand Prix Circuit is the world's longest Formula 1 circuit, with a length of 21.04 kilometers. It's a classic, narrow, and windy track, with a steep incline and a small, narrow turn-around at the end. The circuit is particularly popular among drivers who enjoy the extreme conditions and the challenging racing at the start of the season.")
        print("Lap Record: Charels Leclerc (2024) : 1:19:813")
    elif choice == 4:
        print("You have chosen Suzuka Circuit")
        print("Location: Japan")
        print("Length: 5.807 Km")
        print("Date of first race: 1987")
        print("Details: Suzuka Circuit is a very popular circuit in Japan, with a length of 5.807 kilometers. It is a narrow, windy track, with a steep incline and a small, narrow turn-around at the end. The circuit is famous for its iconic, winding, and narrow turns, and is a popular choice for drivers who enjoy the extreme conditions and the challenging racing at the start of the season.")
        print("Lap Record: Lewis Hamilton (2019) : 1:30:983")
    elif choice == 5:
        print("You have chosen Shanghai International Circuit")
        print("Location: China")
        print("Length: 5.451 Km")
        print("Date of first race: 2004")
        print("Details: Shanghai International Circuit is a very popular circuit in China, with a length of 5.451 kilometers. It is a narrow, windy track, with a steep incline and a small, narrow turn-around at the end. The circuit is famous for its iconic, winding, and narrow turns, and is a popular choice for drivers who enjoy the extreme conditions and the challenging racing at the start of the season.")
        print("Lap Record: Micheal Schumachar (2004) : 1:32:238")
    elif choice == 6:
        print("You have chosen Miami International Autodrome")
        print("Location: Miami")
        print("Length: 5.412 Km")
        print("Date of first race: 2022")
        print("Details: Miami International Autodrome is a very popular circuit in the United States, with a length of 5.412 kilometers. It is a narrow, windy track, with a steep incline and a small, narrow turn-around at the end. The circuit is famous for its iconic, winding, and narrow turns, and is a popular choice for drivers who enjoy the extreme conditions and the challenging racing at the start of the season.")
        print("Lap Record: Lewis Hamilton : 1:29:708")
    elif choice == 7:
        print("You have chosen Autodromo Internationale Enzo e Dino Ferrari")
        print("Location: Emilia - Romagna")
        print("Length: 4.909 Km")
        print("Date of first race: 1980")
        print("Details: Autodromo Internationale Enzo e Dino Ferrari is a very popular circuit in Italy, with a length of 6.016 kilometers. It is a narrow, windy track, with a steep incline and a small, narrow turn-around at the end. The circuit is famous for its iconic, winding, and narrow turns, and is a popular choice for drivers who enjoy the extreme conditions and the challenging racing at the start of the season.")
        print("Lap Record: Lewis Hamilton (2020) : 1:15:484")
    elif choice == 8:
        print("You have chosen Circuit de Monaco")
        print("Location: Monaco")
        print("Length: 3.337 Km")
        print("Date of first race: 1950")
        print("Details: Circuit de Monaco is a very popular circuit in Monaco, with a length of 5.280 kilometers. It is a narrow, windy track, with a steep incline and a small, narrow turn-around at the end. The circuit is famous for its iconic, winding, and narrow turns, and is a popular choice for drivers who enjoy the extreme conditions and the challenging racing at the start of the season.")
        print("Lap Record: Lewis Hamilton (2018): 1:12:077")
    elif choice == 9:
        print("You have chosen Circuit Gilles-Villeneuve Montrael")
        print("Location: Canada")
        print("Length: 4.361 Km")
        print("Date of first race: 1978")
        print("Details: Circuit Gilles-Villeneuve Montrael is a very popular circuit in Canada, with a length of 4.361 kilometers. It is a narrow, windy track, with a steep incline and a small, narrow turn-around at the end. The circuit is famous for its iconic, winding, and narrow turns, and is a popular choice for drivers who enjoy the extreme conditions and the challenging racing at the start of the season.")
        print("Lap Record: Vallteri Bottas (2018) : 1:13:078")
    elif choice == 10:
        print("You have chosen Circuit de Barcelona-Catalunya")
        print("Location: Spain")
        print("Length: 4.657 Km")
        print("Date of first race: 1991")
        print("Details: Circuit de Barcelona-Catalunya is a very popular circuit in Spain, with a length of 5.147 kilometers. It is a narrow, windy track, with a steep incline and a small, narrow turn-around at the end. The circuit is famous for its iconic, winding, and narrow turns, and is a popular choice for drivers who enjoy the extreme conditions and the challenging racing at the start of the season.")
        print("Lap Record: Max Verstappen (2023) : 1:16:330")
    elif choice == 11:
        print("You have chosen Red Bull Ring")
        print("Location: Austria")
        print("Length: 4.318 Km")
        print("Date of first race: 1970")
        print("Details: It’s only wee, bless it, but the Red Bull Ring packs a lot into a short lap. The first half rewards power, as the cars blast along three straights separated by a pair of uphill right-handers. But then as the drivers work their way downhill, the circuit becomes a regular toboggan ride, as the cars canyon through a series of quick corners, including the exhilarating Rindt right-hander, named for Austria’s first F1 champion.")
        print("Lap Record: Carlos Sainz (2020) : 1:05:619")
    elif choice == 12:
        print("You have chosen Silverstone")
        print("Location: United Kingdom")
        print("Length: 5.891 Km")
        print("Date of first race: 1950")
        print("Details: At the 2018 British Grand Prix, Lewis Hamilton compared a flat-out lap around Silverstone to flying a fighter jet, which should tell you all you need to know about the Northamptonshire circuit. Despite numerous layout changes over the years, Silverstone has always maintained its essential character as one of the fastest tracks on the F1 calendar, while historic corners like Maggotts, Becketts and Abbey provide some of the biggest challenges for racing drivers anywhere in the world.")
        print("Lap Record: Max Verstappen (2020) : 1:27:097")
    elif choice == 13:
        print("You have chosen Hungaroring")
        print("Location: Hungary")
        print("Length: 4.381 Km")
        print("Date of first race: 1986")
        print("Details: Hungaroring is a very popular circuit in Hungary, with a length of 4.615 kilometers. It is a narrow, windy track, with a steep incline and a small, narrow turn-around at the end. The circuit is famous for its iconic, winding, and narrow turns, and is a popular choice for drivers who enjoy the extreme conditions and the challenging racing at the start of the season.")
        print("Lap Record: Lewis Hamilton (2020) : 1:16:627")
    elif choice == 14:
        print("You have chosen Circuit de Spa-Francorchamps")
        print("Location: Belgium")
        print("Length: 7.004 Km")
        print("Date of first race: 1950")
        print("Details: Circuit de Spa is a very popular circuit in France, with a length of 4.656 kilometers. It is a narrow, windy track, with a steep incline and a small, narrow turn-around at the end. The circuit is famous for its iconic, winding, and narrow turns, and is a popular choice for drivers who enjoy the extreme conditions and the challenging racing at the start of the season.")
        print("Lap Record: Sergio Checo Perez (2024) : 1:44:701")
    elif choice == 15:
        print("You have chosen Circuit Zandvoort")
        print("Location: Netherlands")
        print("Length: 4.259 Km")
        print("Date of first race: 1952")
        print("Details: ‘Really quick’, ‘pretty insane’, ‘crazy’ and ‘old-school’ were words used by the current crop of F1 drivers when asked to describe the Zandvoort track that many of them tackled in their junior category days. We’d also add ‘undulating’ to that list. The Zandvoort track swoops and flows through the sand dunes, creating a rollercoaster-like feel to the lap. And while the circuit was modernised in time for F1’s most recent return – including increasing the banking angle at the famous Tarzan corner to an Indianapolis Motor Speedway-trumping 18 degrees – Zandvoort remains a proper, challenging drivers’ track.")
        print("Lap Record: Lewis Hamilton (2021) : 1:11:097")
    elif choice == 16:
        print("You have chosen Autodromo Nazionale Monza")
        print("Location: Italy")
        print("Length: 5.793 Km")
        print("Date of first race: 1950")
        print("Details: Rapido! Formula 1’s fastest ever lap was set at Monza – Williams driver Juan Pablo Montoya’s 260.6km/h effort during practice for the 2004 Grand Prix – which should give you some idea of the nature of the track the locals call ‘La Pista Magica’. Cars are on full throttle for 80% of the lap, and hit their Vmax on the circuit’s 1.1km start/finish straight. From there, they roar off into the historic park section, where a series of big stops into tight chicanes give the brakes a good workout.")
        print("Lap Record: Rubens Barichello (2004) : 1:21:046")
    elif choice == 17:
        print("You have chosen Baku city Circuit")
        print("Location: Azerbaijan")
        print("Length: 6.003 Km")
        print("Date of first race: 2016")
        print("Details: A mixture of wide and open and tight and twisty. The lonnnnng main straight along the Baku shoreline is a slipstreaming mecca, and with cars able to run three abreast into Turn 1, the action often looks more IndyCar than F1. However from there, the track loops around into the city’s narrow, winding Icheri Sheher old town, dramatically wending past Baku’s medieval city walls. As in Monaco, slightest mistakes are punished quickly and severely, while set-up wise, the teams are forced to choose between downforce for the twisty bits and less drag for the straight.")
        print("Lap Record: Charles Leclerc (2019) : 1:43:009")
    elif choice == 18:
        print("You have chosen Marina Bay Street Circuit")
        print("Location: Singapore")
        print("Length: 4.94 Km")
        print("Date of first race: 2008")
        print("Details: The Marina Bay Circuit is one of the most physically demanding on the calendar, its bumpy street surface coupled with humid conditions giving the drivers plenty to think about. Even after a 2023 layout change reducing the number of corners from 23 to 19, they are working the wheel a lot, too, around the high-speed lap – the physical stress causing them to lose as much as 3kg in body weight over the course of a race.")
        print("Lap Record: Daniel Ricciardo (2024) : 1:34:486")
    elif choice == 19:
        print("You have chosen Circuit of the Americas")
        print("Location: Texas")
        print("Length: 5.513 Km")
        print("Date of first race: 1912")
        print("Details:If the corners at COTA seem familiar, they should be. Turns 3 through 6 look not dissimilar to Silverstone's high-speed run through Maggotts/Becketts or the S Curves at Suzuka, while Turns 12 through 15 mimic Hockenheim's stadium section. Meanwhile, the uphill run into wide, wide Turn 1 – hey, everything’s bigger in Texas, right? – has provided some fine overtaking action in the track’s short life.")
        print("Lap Record: Charles Leclerc (2019) : 1:36:169")
    elif choice == 20:
        print("You have chosen Autodromo Hermanos Rodriguez")
        print("Location: Mexico")
        print("Length: 4.304 Km")
        print("Date of first race: 1963")
        print("Details: Hungaroring is a very popular circuit in Hungary, with a length of 4.615 kilometers. It is a narrow, windy track, with a steep incline and a small, narrow turn-around at the end. The circuit is famous for its iconic, winding, and narrow turns, and is a popular choice for drivers who enjoy the extreme conditions and the challenging racing at the start of the season.")
        print("Lap Record: Valtteri Bottas (2021) : 1:17:774")
    elif choice == 21:
        print("You have chosen Autodromo Jose Carlos Pace")
        print("Location: Brazil")
        print("Length: 4.309 Km")
        print("Date of first race: 1973")
        print("Details:Like many pre-World War II tracks, Interlagos features banked corners, with the drivers beginning their lap on a sort of half oval – in fact, between 1957 and the track’s return to the F1 calendar in 1990, Interlagos could be run as a giant oval. After wiggling through the Senna S and down to Turn 4, the drivers then go through a snaking in-field section with some challenging camber changes, before slinging back up the hill and through the banked final turn. ")
        print("Lap Record: Valtteri Bottas (2018) : 1:10:540")
    elif choice == 22:
        print("You have chosen Las Vegas Strip Circuit")
        print("Location: Las Vegas")
        print("Length: 6.201 Km")
        print("Date of first race: 2023")
        print("Details:Located in the heart of Las Vegas, the new 6.2km, 17-turn street circuit winds its way past iconic locations like Caesars Palace, the Bellagio and the Venetian. With average speeds similar to Monza, otherwise known as F1’s ‘Temple of Speed’, fans are guaranteed plenty of action and overtaking.")
        print("Lap Record: Lando Norris (2024) : 1:34:876")
    elif choice == 23:
        print("You have chosen Lusail International Circuit")
        print("Location: Qatar")
        print("Length: 5.419 Km")
        print("Date of first race: 2021")
        print("Details: Silverstone is a classic Formula 1 circuit, with a length of 5.494 kilometers. It has a simple layout, with the main straight and narrow turns, and a high-speed lap with a slight downforce. Silverstone has been a popular choice for drivers since its inception in 1958, and has won 16 of the 21 Formula 1 Grand Prixes since then.")
        print("Lap Record: Lando Norris (2024) : 1:22:384")
    elif choice == 24:
        print("You have chosen Yas Marina Circuit")
        print("Location: Abu Dhabi")
        print("Length: 5.281 Km")
        print("Date of first race: 2009")
        print("Details: The Hermann Tilke-designed track is dominated by its 1.2km straight between Turns 5 and 6 – which, with slow-speed corners marking its beginning and end, makes it a honeypot for overtaking moves. Other highlights include the tricky run through Turns 10 and 11 into 12, which forces the drivers to brake hard with bags of lateral load still on the car. Track modifications ahead of the 2021 race, shortening the lap slightly to 5.28km, have only added to its excitement.")
        print("Lap Record: Kevin Magnussen (2024) : 1:25:637")


while True:
    print("Welcome to the Formula 1 Hub!")
    print("1. Race results")
    print("2. Fun Quiz on Formula 1")
    print("3. Driver and Team Statistics")
    print("4. Circuit Information")
    print("5. Exit")
    choice1 = input("Enter your choice: ")

    if choice1 == "1":
        race_results()

    elif choice1 == "2":
        fun_quiz()
        
    elif choice1 == "3":
        driver_teams()
            
    elif choice1 == "4":
        Circuit_Information()
        
    elif choice1 == "5":
        print("Thank you for using the Formula 1 Circuit Information App!")
        break
    else:
        print("Invaild Option. Please Try Again")



