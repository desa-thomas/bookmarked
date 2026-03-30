import { useSearchParams } from "react-router-dom"
import exampleBooks from "../exampleBooks.json"

import BookCoverCard from "../components/BookCoverCard";

export default function BookPage({ }) {
  const [searchParams] = useSearchParams();
  const bookId = searchParams.get("id")

  const book = exampleBooks.find(book => book.id == bookId)

  return (
    <div className="flex p-5 justify-center">

      {/* BOOK COVER */}
      <div className="pr-7">

        <BookCoverCard src={book.img_path} size="L" />
      </div>

      <div className="flex flex-col max-w-150">
        {/* TITLE */}
        <p
          className="font-black text-4xl font-noto-serif tracking-tight">
          {book.title}
        </p>
        <div className="flex gap-3 pb-3">
          <p className="underline">
            {book.publicationYear}
          </p>
          <p>
            Written by <span className="underline">{book.author}</span>
          </p>
        </div>
        <p className="text-black font-medium tracking-tight">
          {book.synopsis}
        </p>

      </div>
    </div>
  )
}
