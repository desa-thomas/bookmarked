// Import icons
import {AiFillAliwangwang} from 'react-icons/ai'

export default function NavBar() {

  return (
    <div
      className="flex flex-row w-screen items-center justify-between border-2 border-black border-md p-4 mb-1">

      <div className="justify-self-start text-2xl hover:underline">
        Bookmarked
      </div>

      <div className="justify-self-end flex flex-row gap-5 items-center">
        <p className="hover:underline">My Books</p>
        <p className="hover:underline">Community</p> 
        <p className="hover:underline">Lists</p>
        <SearchBar/>
        <LoginButton/>
      </div>
  </div>)
}


function LoginButton(){

  return (
    <button
      className="border border-black px-4 py-1 hover:bg-blue-500">
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
