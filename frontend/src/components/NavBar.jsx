// Import icons
import { IoBookmark } from "react-icons/io5";

import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function NavBar() {

  const [query, setQuery] = useState("");

  return (
    <div
      className="flex flex-row items-center justify-between
                w-screen border-2 border-black border-md p-4">

      <div className="justify-self-start flex flex-row items-center gap-1
                      text-3xl font-bold tracking-tighter">
        <a className="" href='#/'>Bookmarked</a>
        <IoBookmark />
      </div>

      <div className="justify-self-end flex flex-row gap-5 items-center font-semibold">
        <a href="#/bookshelf" className="hover:underline">Bookshelf</a>
        <a href="#/community" className="hover:underline">Community</a>
        <a href="#/lists" className="hover:underline">Lists</a>
        <SearchBar query={query} setQuery={setQuery} />
        <LoginButton />
      </div>
    </div>)
}


function LoginButton() {

  return (
    <button
      className="border border-green-800 rounded-sm 
        bg-green-600 hover:bg-green-700
        px-4 py-1 text-white">
      Login
    </button>
  )
}

function SearchBar({ setQuery, query }) {
  
  const navigate = useNavigate()
  const handleKey = (e) => {
    if (e.key === "Enter") {
      navigate(`/search?query=${query}`)
    }
  }
  return (
    <input
      placeholder='Search'
      className='bg-white rounded-xl pl-3 focus:outline-none font-medium'
      onChange={(e) => setQuery(e.target.value)}
      onKeyDown={handleKey}
    />
  )
}
