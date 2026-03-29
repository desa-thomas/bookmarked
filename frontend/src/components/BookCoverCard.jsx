const SIZE = {
  LARGE: "L",
  MEDIUM: "M",
  SMALL: "S"
}

export default function BookCoverCard({ src, alt, size, onClick, hover}) {
/*
    * src - img src
    * alt - img alt
    * size - S, M, L 
    * onClick - function 
    * hover - boolean 
*/

  let widthClass = "w-20"

  if (size === SIZE.LARGE) widthClass = "w-60"
  else if (size === SIZE.MEDIUM) widthClass = "w-40"
  else widthClass = "w-20";

  return (
    <div className={`border rounded-md ${widthClass} overflow-hidden  
                     ${hover ? "hover:outline-green-400 hover:outline-3" : ""}`}
      onClick={onClick}>
      <img src={src} alt={alt} className="w-full h-auto">
      </img>
    </div>
  )
}
