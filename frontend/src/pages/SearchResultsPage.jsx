
import {  useSearchParams } from "react-router-dom"

export default function SearchResultsPage(){
  
  const [searchParams] = useSearchParams();
  const query = searchParams.get("query")

  return(
    <div>
    SEARCHED FOR : {query}
    </div>
  )
}
