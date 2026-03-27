// Import icons
import { IoBookmark } from "react-icons/io5";

export default function NavBar() {

  return (
    <div
      className="flex flex-row w-screen items-center justify-between border-2 border-black border-md p-4">

      <div className="justify-self-start text-3xl font-bold tracking-tighter flex flex-row items-center gap-1">
        <a className="" href = '#/'>Bookmarked</a>
        <IoBookmark/>
      </div>

      <div className="justify-self-end flex flex-row gap-5 items-center font-semibold">
        <a href="#/bookshelf" className="hover:underline">Bookshelf</a>
        <a href="#/community" className="hover:underline">Community</a> 
        <a href="#/lists" className="hover:underline">Lists</a>
        <SearchBar/>
        <LoginButton/>
      </div>
  </div>)
}


function LoginButton(){

  return (
    <button
      className="border border-green-700 rounded-sm bg-green-500
        px-4 py-1 hover:bg-green-600">
      Login
    </button>
  )
} 

function SearchBar(){

  return(
    <input 
      placeholder='Search'
      className='bg-white rounded-xl pl-3'/>
  )
}
