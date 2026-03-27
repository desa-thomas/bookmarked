//FOR URL PARAMETERS
import { useSearchParams } from "react-router-dom"

//EXAMPLE 
import BookCoverCard from "../components/BookCoverCard";

//EXAMPLE BOOK INFORMATION
const exampleBookInfo = [
  {
    "title": "Nineteen Eighty-Four",
    "author": "George Orwell",
    "publicationYear": "1949",
    "genres": ["Dystopian", "Political Fiction"]
  },
  {
    "title": "Blood Meridian",
    "author": "Cormac McCarthy",
    "publicationYear": "1985",
    "genres": ["Anti-Western", "Gothic Western", "Historical Fiction"]
  },
  {
    "title": "A Clockwork Orange",
    "author": "Anthony Burgess",
    "publicationYear": "1962",
    "genres": ["Science Fiction", "Dystopian Fiction", "Satire", "Black Comedy"]
  },
  {
    "title": "The Lord of the Rings",
    "author": "J.R.R. Tolkien",
    "publicationYear": "1954",
    "genres": ["High Fantasy", "Adventure", "Epic"]
  },
  {
    "title": "The Metamorphosis",
    "author": "Franz Kafka",
    "publicationYear": "1915",
    "genres": ["Existentialist Fiction", "Absurdist Fiction", "Short Story"]
  }
]

export default function SearchResultsPage() {

  const [searchParams] = useSearchParams();
  const query = searchParams.get("query")

  //EXAMPLE SEARCH RESULTS, REPLACE WITH API RESULTS 
  const path = "/book_covers_examples"
  const exampleBookPaths = ["1984.jpg", "blood_meridian.jpg", "clockwork.jpg", "LOTR.jpg", "metamorphosis.jpg"]
  const exampleBookList = [];
  for (let i = 0; i < exampleBookPaths.length; i++) {
    const src = `${path}/${exampleBookPaths[i]}`
    exampleBookList.push(
      <SearchResult key={i}
        title={exampleBookInfo[i].title}
        author={exampleBookInfo[i].author}
        publicationYear={exampleBookInfo[i].publicationYear}
        genres={exampleBookInfo[i].genres}>

        <BookCoverCard
          src={src}
          alt={exampleBookPaths[i]}
          size={"SMALL"} />
      </SearchResult>);
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

function SearchResult({ title, author, publicationYear, genres, children }) {
  /**
  Pass a book cover as the children 
  
    <SearchResult title= ... author= ... publicaitonDate=... genres =...>
      <BookCoverCard parameters=.../>
    <SearchResult/>
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
              {title}
            </p>
            <p className="font-light tracking-wide text-xl">
              {publicationYear}
            </p>
          </div>

          <p className="font-light">" Short synopsis of the book"   </p>
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
              {`${author}`}
            </div> </div>
          <p> Genres: {genres.join(", ")} </p>
        </div>
      </div>

    <hr className="mt-5 opacity-30" />

    </div>
  )
}
