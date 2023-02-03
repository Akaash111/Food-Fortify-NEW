//variables, consts a_B, functions aB
import {Entity, DB} from "../backend-JS/entity&DB.js"
//Init DB
let MainDB = new DB()

const Title = document.querySelector("#title")
Title.style.backgroundColor = "#637e7e"
const Header = document.querySelector("#header")
Header.style.backgroundColor = "#637e7e"

//ENTITY WINDOW NAVIGATION
window.onload = function() {
  const rd_CreateNewEntity = document.querySelector("#optionA1")
  function rdCreateNewEntity(){
    window.location.href = "/HTML/create_new_entity_menu.html"
  }
  if (rd_CreateNewEntity != null)
    rd_CreateNewEntity.addEventListener("click", rdCreateNewEntity)


  const rd_ViewEntities = document.querySelector("#optionA4")
  function rdViewEntities(){
    window.location.href = "/HTML/view_existing_entities.html"
  }
  rd_ViewEntities.addEventListener("click", rdViewEntities)


  const f_flushAllRecords = document.querySelector("#optionA5")
  function fflushAllRecords(){
    MainDB.flushDistributorDB()
    MainDB.flushProducerDB()
    MainDB.flushRetailerDB()
  }2

  f_flushAllRecords.addEventListener("click", fflushAllRecords)
}



//CREATE NEW ENT and add it to DB
document.addEventListener('DOMContentLoaded', ()=>{
  const f_CreateNewEntity = document.querySelector("#submitEntityInfo")
  function fCreateNewEntity(){
    let Name = document.querySelector("#createName").value
    let ID = document.querySelector("#createID").value
    let Location = document.querySelector("#createLocation").value
    let Phone = document.querySelector("#createPhone").value
    let Email = document.querySelector("#createEmail").value

    //Contact: tuple
    let Contact = [Phone, Email]

    //Creating new entity
    let NewEntity = new Entity(Name, ID, Location, Contact)
    //ADD TO DATABASE
    MainDB.AddEntity(NewEntity)
    //UPDATE STATUS
    document.querySelector("#statusCreate").innerHTML = "Successfully Created. "
  }
  f_CreateNewEntity.addEventListener("click", fCreateNewEntity)

})

//FLUSH ALL ENTITIES

//UPDATE EXISTING ENTITY

//VIEW EXISTING ENTITIES
document.addEventListener('DOMContentLoaded', ()=>{

}
)

let test = new Entity("NameX", "P101", "SG", "-")
MainDB.AddEntity(test)
export {MainDB}

//MAIN MENU NAVIGATION
document.addEventListener('DOMContentLoaded', ()=>{
  const rd_Menu = document.querySelector("#optionM1")
  function rdMenu(){
    window.location.href = '/HTML/main.html'
  }
  rd_Menu.addEventListener("click", rdMenu)
})


//NAVIGATE TO EAGLE VIEW PAGE
document.addEventListener('DOMContentLoaded', ()=>{
  const rd_EagleView = document.querySelector("#eagleviewbtn")
  function rdEagleView(){
    window.location.href = '/HTML/eagle_view.html'
  }

  rd_EagleView.addEventListener("click", rdEagleView)

})

