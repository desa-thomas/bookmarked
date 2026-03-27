const SIZE = {
  LARGE: "LARGE",
  MEDIUM: "MEDIUM",
  SMALL: "SMALL"
}

export default function BookCoverCard({ src, alt, size }) {

  let widthClass = "w-20"

  if (size === SIZE.LARGE) widthClass = "w-40"
  else if (size === SIZE.MEDIUM) widthClass = "w-20"
  else widthClass = "w-20";

  return (
    <div className={`border rounded-md ${widthClass} overflow-hidden`}>
      <img src={src} alt={alt} className="w-full h-auto">
      </img>
    </div>
  )
}
