class Engine():
    # Name of the part, like F-1
    name: str
    # in kg
    mass: int
    # in kn (kili Nuton)
    thrust: int
    # in seconds
    isp: int

    def __init__(self, name, mass, thrust, isp):
        self.name = name
        self.mass = mass
        self.thrust = thrust
        self.isp = isp
