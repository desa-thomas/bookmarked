import { useSearchParams } from "react-router-dom"
import exampleBooks from "../exampleBooks.json"

import BookCoverCard from "../components/BookCoverCard";

export default function BookPage( { }){
  const [ searchParams ] = useSearchParams(); 
  const bookId = searchParams.get("id")

  const book = exampleBooks.find(book => book.id == bookId)

  return (
    <div className="flex">
   <BookCoverCard src = {book.img_path}  size = "L"/> 
    </div>
  )
}
