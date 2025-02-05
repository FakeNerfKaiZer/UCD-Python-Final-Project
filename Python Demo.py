"""Class 1"""
class Robot:
    def __init__(self, type, id, name):
        """Initialize the Robot with type, id, and name."""
        self.type = type
        self.id = id
        self.name = name  

    def __str__(self):
        """String representation of the Robot for easy printing."""
        return f"This robot is named {self.name}, has an id of {self.id}, and is of type {self.type}"

    def __repr__(self):
        """Official string representation of the Robot for debugging."""
        return f"Robot(id='{self.id}', type='{self.type}', name='{self.name}')"

"""Class 2"""
class Drytron(Robot):
    def __init__(self, type, id, name, weapon, power_level):
        """Initialize the Drytron by calling the parent class's initializer and adding specific attributes."""
        super().__init__(type, id, name)
        self.weapon = weapon
        self.power_level = power_level

    def __str__(self):
        """String representation of the Drytron for easy printing."""
        return (f"ID: {self.id}\n"
                f"Name: {self.name}\n"
                f"Type: {self.type}\n"
                f"Weapon: {self.weapon}\n"
                f"Power Level: {self.power_level}\n")

    def __repr__(self):
        """Official string representation of the Drytron for debugging."""
        return (f"Drytron(id='{self.id}', type='{self.type}', name='{self.name}', "
                f"weapon='{self.weapon}', power_level={self.power_level})")

"""Class 3"""
class DrytronFleet:
    def __init__(self):
        """Initialize the fleet with an empty list to store robots and a set to avoid duplicate IDs."""
        self.robots = []  # List to store robot objects
        self.robot_ids = set()  # Set to ensure unique robot IDs

    def add_robot(self, robot):
        """Add a robot to the fleet if it is an instance of Robot or its subclasses and has a unique ID."""
        try:
            if isinstance(robot, Robot):
                if robot.id not in self.robot_ids:  # Check for unique ID
                    self.robots.append(robot)
                    self.robot_ids.add(robot.id)
                else:
                    print(f"Robot with ID {robot.id} already exists in the fleet.")
            else:
                raise TypeError("Only instances of Robot or its subclasses can be added.")
        except TypeError as e:
            print(e)

    def display_fleet_info(self, limit=None):
        """Display information for all robots in the fleet, with optional slicing to limit output."""
        if not self.robots:
            print("The fleet is empty.")
            return
        
        print("\n--- Fleet Information ---")
        # Use slicing if a limit is provided
        for robot in self.robots[:limit] if limit else self.robots:
            print(robot)  # Polymorphism: Calls the __str__ method of each robot

    def find_robot_by_id(self, robot_id):
        """Search for a robot by its ID in the fleet."""
        for robot in self.robots:
            if robot.id == robot_id:
                return robot
        return None

    def filter_by_power_level(self, threshold):
        """Filter robots with a power level greater than a given threshold."""
        powerful_robots = [robot for robot in self.robots if isinstance(robot, Drytron) and robot.power_level > threshold]
        return powerful_robots

    def get_robots_by_type(self):
        """Organize robots by type using a dictionary."""
        robot_dict = {robot.type: [] for robot in self.robots}
        for robot in self.robots:
            robot_dict[robot.type].append(robot)
        return robot_dict

"""Instantiate Robots and Drytrons"""
robot1 = Robot(type="Basic", id="00000001", name="BasicBot")
robot2 = Robot(type="Advanced", id="00000002", name="AdvancedBot")

Thuban = Drytron(type="Alpha", id="08342313", name="Thuban", weapon="Core Wing Cannon", power_level=2000)
Athebyne = Drytron(type="Eta", id="09238404", name="Athebyne", weapon="Draco Sphere", power_level=1000)
Draconids = Drytron(type="Meteonis", id="07664732", name="Draconids", weapon="Pulse Gunblade", power_level=4000)

"""Create a DrytronFleet instance and add robots"""
fleet = DrytronFleet()
fleet.add_robot(Thuban)
fleet.add_robot(Athebyne)
fleet.add_robot(Draconids)
fleet.add_robot(robot1)
fleet.add_robot("NotARobot")  # Will raise a TypeError and be caught by try-except

"""Display all fleet information"""
fleet.display_fleet_info()

"""Function to search for a robot by ID with input validation and loops"""
def search_by_id():
    while True:  # Use a while loop to allow re-trying
        ID = input("Please input an ID or type 'exit' to stop: ")
        if ID.lower() == 'exit':
            break
        robot_found = fleet.find_robot_by_id(ID)
        if robot_found:
            print("\nFound Robot:\n", robot_found)
        else:
            print("\nRobot not found.")

"""Search by ID"""
search_by_id()

"""Filter and display robots with power level above a threshold using for loop and conditionals"""
threshold = 1500
print(f"\nRobots with power level above {threshold}:")
powerful_robots = fleet.filter_by_power_level(threshold)
for robot in powerful_robots:
    print(robot)

""" Dictionary example for holding robots by type"""
robot_dict = fleet.get_robots_by_type()

print("\n--- Robots by Type ---")
for robot_type, robots in robot_dict.items():
    print(f"\nType: {robot_type}")
    for robot in robots:
        print(robot)
