class Player:
    def __init__(self, first_name, last_name, apt, set, position, national_association):
        self.first_name = first_name
        self.last_name = last_name
        self.apt = apt
        self.set = set
        self.position = position
        self.national_association = national_association
        self.avg = (apt + set) / 2

    def __repr__(self):
        return f"{self.first_name} {self.last_name}, APT: {self.apt}, SET: {self.set}, AVG: {self.avg}, Position: {self.position}, National Association: {self.national_association}"
