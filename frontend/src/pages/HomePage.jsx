import { useState } from "react";

import BookCoverCard from "../components/BookCoverCard"
import RegisterPopup from "./RegisterPopup";

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
  // State for registration pop up dialog/form 
  const [registerPopup, setRegisterPopup] = useState(false);
  const openRegisterPopup = () => setRegisterPopup(true); 
  const closeRegisterPopup = () => setRegisterPopup(false); 

  return (
    <div className="border flex-1 flex flex-col items-center gap-10 justify-center">
      {/** SIGNUP **/}
      <div className="text-4xl font-medium font-playfair items-center flex flex-col justify-self-center pt-5">
        <p>Track books you've read.</p>
        <p>Save those you want to read.</p>
        <p>Tell your friends what's good.</p>
      </div>
      <SignupButton onclick={openRegisterPopup}/>

      <div className="pt-5">
        {/**<h1 className="text-3xl font-semibold tracking-tighter"> POPULAR BOOKS </h1> **/}
        <PopularBooks />
      </div>

       {registerPopup && (<RegisterPopup closeFunction={closeRegisterPopup}/>)}
    </div>
  )
}

function SignupButton( {onclick} ) {
  return (
    <button onClick={onclick} 
    className="p-3 border-green-800 border-1 rounded-md
    font-medium text-white
    bg-green-600 hover:bg-green-700">
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
