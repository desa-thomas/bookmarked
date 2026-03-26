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
 
  const exampleBookList = []; 
  for (let i = 0; i < 5; i++){
    exampleBookList.push(
      <BookCoverCard key={i}/>
    )
  }

  return (
    <div className="border flex-1 flex flex-col items-center gap-5 pt-5">
      {/** SIGNUP **/}
      <div className="text-4xl font-medium font-playfair items-center flex flex-col justify-self-center">
        <p>Track books you've read.</p>
        <p>Save those you want to read.</p>
        <p>Tell your friends what's good.</p>
      </div>
      <SignupButton />

      {/** BOOK CARDS  **/}
      <div className="flex gap-5">
        {exampleBookList} 
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
