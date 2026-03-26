
export default function BookCoverCard({src, alt}){
  return(
    <div className="border rounded-md w-40 overflow-hidden">
      <img src={src} alt={alt} className="w-full h-auto">
    </img>
    </div>
  )
}
