//FOR URL PARAMETERS
import { useSearchParams } from "react-router-dom"

//EXAMPLE 
import BookCoverCard from "../components/BookCoverCard";

//EXAMPLE BOOK INFORMATION


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
      <BookCoverCard
        key={i}
        src={src}
        alt={exampleBookPaths[i]}
        size={"SMALL"} />);
  }
  //---------------------------------------------

  return (
    <div className="p-5">
      <p className="tracking-wide font-light">

        SHOWING MATCHES FOR "{query}"
      </p>
      <hr className="mb-5"/>
      <div className="flex flex-col gap-5">
        {exampleBookList}
      </div>
    </div>
  )
}
