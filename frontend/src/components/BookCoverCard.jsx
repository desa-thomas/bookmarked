const SIZE = {
  LARGE: "L",
  MEDIUM: "M",
  SMALL: "S"
}

import { useNavigate } from "react-router-dom";

export default function BookCoverCard({ src, alt, size, onclick, id }) {
  /*
      * src - img src
      * alt - img alt
      * size - S, M, L 
      * onclick - boolean (clicking cover card will route to the book page)
      * id - book id for routing
  */

  const navigate = useNavigate();
  const toBookPage = (id) => { navigate(`/book?id=${id}`) }

  let widthClass = "w-20"

  if (size === SIZE.LARGE) widthClass = "w-60"
  else if (size === SIZE.MEDIUM) widthClass = "w-40"
  else widthClass = "w-20";

  return (
    <div className={`border rounded-md ${widthClass} overflow-hidden  
                     ${onclick ? "hover:outline-green-400 hover:outline-3" : ""}`}
      onClick={onclick ? () => { toBookPage(id) } : () => { }}>
      <img src={src} alt={alt} className="w-full h-auto">
      </img>
    </div>
  )
}
