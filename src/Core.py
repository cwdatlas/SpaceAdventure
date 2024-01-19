
from Models.Capsules.Apollo import Apollo
from Models.Capsules.Dragon import Dragon
from Models.Capsules.Orion import Orion
from Models.Engines.Raptor import Raptor
from Models.Engines.F_1 import F1
from Models.Engines.RD_170 import RD170
from Models.FuelTanks.Large import Large
from Models.FuelTanks.Medium import Medium
from Models.FuelTanks.Small import Small
class core:
    def __init__(self):
        print("inisializing application")
        # inisialize dictionary that holds commands
        self.commands = {"capsule": self.Capsule, "engine": self.Engine, "help": self.Help, "launch": self.Launch, "reset": self.Reset,
                    "status": self.Status, "tank": self.Tank}
        # inisialize dictionary that holds rocket parts (rocket should be a class in a long term projecct)
        self.rocket = {"name": "First Rocket", "capsule": "Default", "tank": "Default", "engine": "Default"}
        # set game status
        self.game_running = False

    def start_game(self):
        #start the game
        game_running = True
        #title screen
        print("______  ______  ______  __  __   ______  ______     ______  __  __  __  __      _____   ______  ______     ")
        print("/\  == \/\  __ \/\  ___\/\ \/ /  /\  ___\/\__  _\   /\  == \/\ \/\ \/\ \/\ \    /\  __-./\  ___\/\  == \   ")
        print("\ \  __<\ \ \/\ \ \ \___\ \  \_-.\ \  __\\/_/\ \/    \ \  __<\ \ \_\ \ \ \ \ \___\ \ \/\ \ \  __\\ \  __<   ")
        print(" \ \_\ \_\ \_____\ \_____\ \_\ \_\\ \_____\ \ \_\     \ \_____\ \_____\ \_\ \_____\ \____-\ \_____\ \_\ \_\ ")
        print("  \/_/ /_/\/_____/\/_____/\/_/\/_/ \/_____/  \/_/     \/_____/\/_____/\/_/\/_____/\/____/ \/_____/\/_/ /_/ ")

        print("Welcome to rocket builder, Here you can build your very own rocket and fly it!")
        print("Your goal is to build a rocket that can get to orbit, or even as far as Jupiter! Type help for more information")
        print("Build your rocket by typing in capsule, tank, and engine to choose your parts, then type launch to launch!")
        print("You can always use exit to exit the game. If you dont know the commands or need mroe help, then type help.")
        print("Take note that you wont be able to use commands in the capsule, tank and engine builder bays")

        #main game loop
        while game_running:
            command = input("-> ")
            # if the user wants to exit the game, then that command has priority.
            if command == "exit":
                self.game_running = False
                break
            # check if their command was in the list of commands
            if command in self.commands:
                self.commands[command]()

    def Capsule(self):
        # Create a list of capsules to choose from
        capsules = {"Apollo": Apollo, "Dragon": Dragon, "Orion":Orion}
        print("Welcome to the Capule Build Bay, choose a capsule from below")
        for i in capsules:
            print("---", i ,"Crew Capsule ---")
            print("-Mass ", capsules[i].mass, "kg")
            print("-Crew ", capsules[i].crew)

        # loop so the user can have more than one chance at making a decision
        choosing = True
        while choosing:
            capsule = input("Apollo, Dragon, Orion ->")
            if capsule in capsules:
                self.rocket["capsule"] = capsules[capsule]
                print("Capsule set to", self.rocket["capsule"].name)
                choosing = False
            else:
                print("Please type in one of the three capsule names")

    def Tank(self):
        # Create a list of tanks to choose from
        tanks = {"small": Small, "medium": Medium, "large": Large}
        print("Welcome to the Tank Build Bay, choose a tank from below")
        for i in tanks:
            print("---", i, "tank ---")
            print("-Mass ",        tanks[i].mass, "kg")
            print("-liquid Fuel ", tanks[i].liquid_fuel, "kg")

        # loop so the user can have more than one chance at making a decision
        choosing = True
        while choosing:
            tank = input("small, medium, large ->")
            if tank in tanks:
                self.rocket["tank"] = tanks[tank]
                print("Tank set to", self.rocket["tank"].name)
                choosing = False
            else:
                print("Please type in one of the three tank names")

    def Engine(self):
        # Create a list of engines to choose from
        engines = {"F-1": F1, "Raptor": Raptor, "RD-170": RD170}
        print("Welcome to the Engine Build Bay, choose an Engine from below")
        for i in engines:
            print("---", i, "engine ---")
            print("-Mass ",   engines[i].mass, "kg")
            print("-Thrust ", engines[i].thrust, "kn")
            print("-ISP ",    engines[i].isp, "seconds")

        # loop so the user can have more than one chance at making a decision
        choosing = True
        while choosing:
            engine = input("F-1, Raptor, RD-170 ->")
            if engine in engines:
                self.rocket["engine"] = engines[engine]
                print("Engine set to", self.rocket["engine"].name)
                choosing = False
            else:
                print("Please type in one of the three engine names")

    def Status(self):
        # Stating statistics for the rocket that the user created
        print("-- Capsule --")
        print("Name:", self.rocket["capsule"].name)
        print("mass:", self.rocket["capsule"].mass)
        print("Total Crew:", self.rocket["capsule"].crew)

        print("-- Fuel Tank --")
        print("Name:", self.rocket["tank"].name)
        print("Dry Mass:", self.rocket["tank"].mass)
        print("Fuel Mass:", self.rocket["tank"].liquid_fuel)

        print("-- Engine --")
        print("Name", self.rocket["engine"].name)
        print("Mass", self.rocket["engine"].mass)
        print("Thrust", self.rocket["engine"].thrust)
        print("ISP", self.rocket["engine"].isp)

    def Launch(self):
        print("launch")

    def Reset(self):
        print("Resetting gmae")
        self.__init__()
        self.start_game()

    def Help(rocket):
        print("Rocket builder, otherwise known as SpaceAdventure is a game where you can build your own rocket")
        print("You will need to balance mass, thrust and fuel to build a rocket with the highest Delta V.")
        print("Delta V is the measurment of how much change in velocity a rocket can achieve. This game does not take "
              "into account drag or more complicated factors. ")
        print(
            "1. Once Launched Rocket Builder checks thrust to mass ratio (TWR). If your TWR is less than 1.5, you fail to get to orbit")
        print(
            "2. Your Delta V will then be calculated. Depending on it's value, you are able to achieve orbit around one of the "
            "plannets. Avaliable plannets are Earth, (basic orbit), Mars, and Jupiter")
        print(
            "This game is supposeded to be a learning experience, so the values for the capsules and engines are accurate. Sadly, Delta V"
            " Calculations are not.")
        print("<----> Here are all of the commands and the descriptions for what they do <---->")
        print(
            "____________________________________________________________________________________________________________________________________")
        print("capsule -> Lists capsules and their stats. Any choice will override a previous choice")
        print("tank    -> Lists tanks and their stats. Any choice will override a previous choice")
        print("engine  -> Lists engines and their stats. Any choice will override a previous choice")
        print(
            "status  -> Lists the mass and thrust of your rocket. you will just have to wait for Delta V to be calculated")
        print("launch  -> Launches your rocket! See how far you get!")
        print("reset   -> resets Rocket Builder")
        print("help    -> looks like you already know what this does")
        print(
            "____________________________________________________________________________________________________________________________________")