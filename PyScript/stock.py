from datetime import *

class Stock():
    def __init__(self, Name, ID, Location, To, From, Created, Expiry = None):
        self.Name = Name
        self.ID = ID
        self.Location = Location
        self.To = To
        self.From = From
        self.Created = date.today()
        self.Expiry = Expiry