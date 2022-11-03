import React, {useEffect, useState} from "react";
import * as Server from './Server'


 const ListaCanciones=()=>{
     const listaCan=async ()=>{
         try {
             const res=await Server.listaSonds();
             //const datos=await res.json()
             console.log(res);
         }catch (error){
             console.log(error+" algo se murio ");
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