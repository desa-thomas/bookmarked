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

import { IconContext } from "react-icons";

import { IoBook } from "react-icons/io5";
import { IoHeart } from "react-icons/io5";
import { IoBookmark } from "react-icons/io5";

import { IoStar } from "react-icons/io5";
import { IoStarHalfOutline } from "react-icons/io5";

import { useState } from "react";

function RatingWidget() {

  const [hovered, setHovered] = useState(false);
  const [starHoveredId, setStarHoveredId] = useState(0);
  const iconSize = 40

  const stars = []
  for (let i = 1; i <= 5; i++) {
    stars.push(

        <IoStar id={i} size={iconSize} 
        className={`${starHoveredId >= i && hovered ? "text-yellow-500" : "text-stone-600"}`}

          onMouseEnter={() => {
            setHovered(true)
            setStarHoveredId(i)
          }}
          onMouseLeave={() => {
            setHovered(false)
          }} />)
  }
  return (
    <div
      className="
    min-w-60 h-fit overflow-hide 
    flex flex-col gap-1">

      {/* FIRST ROW*/}
      <div className="flex text-sm justify-between
               border-1 border-black rounded-t-md px-6 py-4 bg-bgsecondary">

        <div className="flex flex-1 flex-col items-center">
          <IoBook size={iconSize} className="text-stone-600 hover:text-orange-300"/>
          Read
        </div>

        <div className="
          flex flex-1 flex-col items-center">
          <IoHeart size={iconSize} className="text-stone-600 hover:text-red-300"/>
          Like
        </div>
        <div className="flex flex-1 flex-col items-center">
          <IoBookmark size={iconSize} className="text-stone-600 hover:text-green-500"/>
          Bookmark
        </div>
      </div>

      {/*SECOND ROW*/}
      <div className="flex flex-col border-1 border-black rounded-b-md
                      px-6  py-3 bg-bgsecondary">
        <div className="self-center text-sm font-semibold">
          Rate
        </div>
        <div className="flex items-center justify-between">
          {stars}
        </div>
      </div>
    </div>
  )
}

