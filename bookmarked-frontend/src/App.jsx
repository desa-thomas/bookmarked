import { useState } from 'react'
import './index.css'

// Import router for pages
import { HashRouter as Router, Routes, Route} from "react-router-dom"


function App() {
  const [count, setCount] = useState(0)

  return(
    <>
     <div  
    className='mx-auto flwx max-w-sm item-center gap-x-4 rounded-xl bg-blue p-6 shadow-lg outline outline-black/5'>
      Hello world 
     </div>

    </>)

}

export default App

