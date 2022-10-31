import React, {useEffect, useState} from "react";
import * as Server from './Server'


 const ListaCanciones=()=>{
     const listaCan=async ()=>{
         try {
             const res=await Server.listaSonds();
             const datos=await res.json()
             console.log(datos);
         }catch (error){
             console.log(error);
         }
     }
     useEffect(()=>{
         listaCan();
     },[]);
     return(
         <div>

         </div>
     );
 };

 export default ListaCanciones