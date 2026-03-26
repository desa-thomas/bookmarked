import BookCoverCard from "../components/BookCoverCard"

export default function HomePage({ loggedIn }) {
  /**
  *    HomePage Boundary Class
  *    Takes login state
  */
  return (loggedIn ? <LoggedInHomepage /> : <DefaultHomepage />)
}

function LoggedInHomepage() {

  return (
    <div>
      LOGGED IN
    </div>)
}

function DefaultHomepage() {

  return (
    <div className="border flex-1 flex flex-col items-center gap-5 pt-5">
      {/** SIGNUP **/}
      <div className="text-4xl font-medium font-playfair items-center flex flex-col justify-self-center">
        <p>Track books you've read.</p>
        <p>Save those you want to read.</p>
        <p>Tell your friends what's good.</p>
      </div>
      <SignupButton />

      <div>
        <h1 className="text-3xl font-semibold tracking-tighter"> POPULAR BOOKS </h1>
        <PopularBooks />
      </div>
    </div>
  )
}

function SignupButton() {
  return (
    <button className=" p-3 border-green-700 border-1 font-medium rounded-md bg-green-500 hover:opacity-80 hover:bg-green-600">
      Begin Your Reading Journey </button>
  )
}

function PopularBooks() {

  // EXAMPLE BOOKS REPLACE WITH BOOKS FROM DB
  const publicPath = "/book_covers_examples"
  const exampleBookPaths = ["1984.jpg", "blood_meridian.jpg", "clockwork.jpg", "LOTR.jpg", "metamorphosis.jpg"]
  const exampleBookList = [];
  for (let i = 0; i < exampleBookPaths.length; i++) {
    const src = `${publicPath}/${exampleBookPaths[i]}`
    exampleBookList.push(
      <BookCoverCard key={i} src={src} alt={exampleBookPaths[i]} />
    )
  }
  return (
    <div className="flex gap-5">
      {exampleBookList}
    </div>)
}
