import { Entity, DB} from "../backend-JS/entity&DB.js";
import { MainDB } from "./main.js";

const ProducerDBSize = MainDB.ProducerDB.length
const RetailerDBSize = MainDB.RetailerDB.length
const DistributorDBSize = MainDB.DistributorDB.length

window.onload = function dataToTable(data) {
    let tableHTML = "";

    for (let i = 0; i <= ProducerDBSize; i++){
      const holder = MainDB.ViewProducerDB()
      const row = holder[i]

      tableHTML += `<td>  ${row}  </td>`;
      tableHTML += "</tr>";
  
      const tableSelector = document.querySelector("#tableData");
      tableSelector.innerHTML = tableHTML;


    }

  }


console.log(MainDB.ViewProducerDB())
  

