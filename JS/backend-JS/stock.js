class Stock{
    constructor(Name, ID, Location, To, From, Created, Expiry){
        this.Name = Name
        this.ID = ID
        this.Location = Location
        this.To = To
        this.From = From
        this.Created = Created
        this.Expiry = Expiry
    }

    ViewStocks(){
        string = ""
        string += `Name: ${this.Name} `
        string += `ID: ${this.ID} `
        string += `Location: ${this.Location} `
        string += `To: ${this.To} `
        string += `From: ${this.From} `
        string += `Created: ${this.Created} `
        string += `Expiry: ${this.Expiry} `
    }


}