class Entity{
  constructor(Name, ID, Location, Contact, InventorySize = null){
    this.Name = Name
    this.ID = ID
    this.Location = Location
    this.Contact = Contact
    this.InventorySize = InventorySize

    this.CurrentInventory = [];
  }


  UpdateInfo(newName, newID, newLocation, newContact, newInventorySize){
    this.Name = newName
    this.ID = newID
    this.Location = newLocation
    this.Contact = newContact
    this.InventorySize = newInventorySize
  }

  GetInfo(){
    let Message = ""

    Message += "Name: " + this.Name
    Message += " ID: " + this.ID
    Message += " Location: " + this.Location
    Message += " Contact: " + this.Contact
    Message += " Inventory Size: " + this.InventorySize

    return Message
  }

}

class DB{
  constructor(){
    this.ProducerDB = []
    this.DistributorDB = []
    this.RetailerDB = []
  }

  AddEntity(newEntity){
    if (newEntity.ID[0] == 'P'){
      this.ProducerDB.push(newEntity)
    }
    else if (newEntity.ID[0] == "D"){
      this.DistributorDB.push(newEntity)
    }
    else if (newEntity.ID[0] == "R"){
      this.RetailerDB.push(ewEntity)
    }
  }

  ViewProducerDB(){
    let producers = []
    for (let elements of this.ProducerDB){
      producers.push(elements.GetInfo())
    }
    return producers
  }


  ViewDistributorDB(){
    for (let elements of this.DistributorDB){
      console.log(elements.GetInfo());
    }
    return "";
  }

  ViewRetailerDB(){
    for (let elements of this.RetailerDB){
      console.log(elements.GetInfo());
    }
    return "";
  }

  IsPresent(newID) {
    let found = false;
    let database = null;
    switch (newID[0]) {
        case "P":
            database = this.ProducerDB;
            break;
        case "D":
            database = this.DistributorDB;
            break;
        case "R":
            database = this.RetailerDB;
            break;
        default:
            console.log(false);
            return false;
    }
    for (let i = 0; i < database.length; i++) {
        if (database[i].ID === newID) {
            found = true;
            break;
        }
    }
    console.log(found);
    return found;
  }

  flushProducerDB(){
    this.ProducerDB = []
  }

  flushDistributorDB(){
    this.DistributorDB = []
  }

  flushRetailerDB(){
    this.RetailerDB = []
  }
}

const mainDB = new DB()
const newEnt = new Entity("FarmLand", "P10102", "SG", "-")

mainDB.AddEntity(newEnt)
console.log(mainDB.ViewProducerDB())

export {Entity, DB}
