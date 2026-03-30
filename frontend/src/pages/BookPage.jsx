import { useSearchParams } from "react-router-dom"
import exampleBooks from "../exampleBooks.json"

import BookCoverCard from "../components/BookCoverCard";

export default function BookPage({ }) {
  const [searchParams] = useSearchParams();
  const bookId = searchParams.get("id")

  const book = exampleBooks.find(book => book.id == bookId)

  return (
    <div className="flex p-5 gap-5 justify-center">

      {/* BOOK COVER */}
      <div className="">

        <BookCoverCard src={book.img_path} size="L" />
      </div>

      {/* COL 2 : Title , year, author , synopsis , rating widget*/}
      <div className="flex flex-col max-w-160">
        {/* TITLE */}
        <p
          className="font-black text-4xl font-noto-serif tracking-tight">
          {book.title}
        </p>
        {/* YEAR - AUTHOR */}
        <div className="flex gap-3 pb-3">
          <p className="underline">
            {book.publicationYear}
          </p>
          <p>
            Written by <span className="underline">{book.author}</span>
          </p>
        </div>
        {/* SYNOPSIS - RATING*/}
        <div className="flex gap-5">
          <p className="text-black font-medium tracking-tight">
            {book.synopsis}
          </p>
          <RatingWidget />
        </div>
      </div>
    </div>
  )
}


//WIDGET ICONS
import { IoBookOutline } from "react-icons/io5";
import { CiHeart } from "react-icons/ci";
import { CiBookmark } from "react-icons/ci";
function RatingWidget() {
  const iconSize = 40
  return (
    <div
      className="
    border-1 border-black rounded-md min-w-50 h-fit overflow-hide p-4
    flex flex-col">

      {/* FIRST ROW*/}
      <div className="flex gap-2 justify-between">
        <IoBookOutline size={iconSize}/>
        <CiHeart size={iconSize} />
        <CiBookmark size={iconSize}/>
      </div>

      {/*SECOND ROW*/}
      <div>
        RATE (STARS)
      </div>
    </div>
  )
}
