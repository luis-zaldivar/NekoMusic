const API_URL_Sond="https://pokeapi.co/api/v2/pokemon/ditto";
 export const  listaSonds=async ()=>{
     return await fetch( API_URL_Sond);
 };