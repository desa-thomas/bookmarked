//FOR URL PARAMETERS
import { useSearchParams } from "react-router-dom"

import BookCoverCard from "../components/BookCoverCard";

//EXAMPLE BOOK INFORMATION
import exampleBooks from "../exampleBooks.json" 

export default function BookSearchResultsPage() {

  const [searchParams] = useSearchParams();
  const query = searchParams.get("query")

  //EXAMPLE SEARCH RESULTS, REPLACE WITH API RESULTS 
  const exampleBookList = [];

  for (let i = 0; i < exampleBooks.length; i++) {
    const src = `/book_covers_examples/${exampleBooks[i].img_path}`
    exampleBookList.push(
      <BookSearchResult key={i} book={exampleBooks[i]}>

        <BookCoverCard
          src={src}
          alt={exampleBooks[i].img_path}
          size={"SMALL"} />
      </BookSearchResult>);
  }
  //---------------------------------------------

  return (
    <div className="flex flex-col p-5 items-center">
      <div>
        <p className="tracking-wide font-light">

          SHOWING MATCHES FOR "{query}"
        </p>
        <hr className="mb-5" />
        <div className="flex flex-col gap-5">
          {exampleBookList}
        </div>
      </div>
    </div>
  )
}

function BookSearchResult({ book, children }) {
  /**
  
  Book search result card. Takes book object and a book cover (as the child)

  Usage:  
    <BookSearchResult book=book>

      <BookCoverCard parameters=.../>

    <BookSearchResult/>

  */
  return (
    <div>
      <div className="grid grid-cols-[min-content_auto] "  >

        <div className="justify-self-start">

          {children} {/* BOOKCOVER */}
        </div>

        {/* TITLE - YEAR  
        SYNOPSIS*/}
        <div className="pl-5">
          {/*TITLE - YEAR */}
          <div className="self-start flex items-end gap-2">
            <p 
                className="font-bold font-playfair text-2xl tracking-tight
                          hover:text-green-600 cursor-pointer">
              {book?.title}
            </p>
            <p className="font-light tracking-wide text-xl">
              {book?.publicationYear}
            </p>
          </div>

          <p className="font-light break-all">" Short synopsis of the book"   </p>
        </div>

        {/* EMPTY CELL UNDER BOOK COVER*/}
        <div></div>

        {/* Author
        GENRES */}
        <div className="pl-5">

          <div className="flex items-center gap-2"> Written by
            <div className="px-1 border-fontalt border-1 bg-bgsecondary 
               rounded-sm opacity-60 hover:opacity-100 
               transition-all duration-100 cursor-pointer">
              {`${book?.author}`}
            </div> </div>
          <p> Genres: {book?.genres.join(", ")} </p>
        </div>
      </div>

    <hr className="mt-5 opacity-30" />

    </div>
  )
}
