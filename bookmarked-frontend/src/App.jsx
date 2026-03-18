import { useState } from 'react'
import './index.css'

// Import router for pages
import { HashRouter as Router, Routes, Route } from "react-router-dom"

// Import Pages 

// Import Components
import NavBar from './components/NavBar'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className='font-sans'>
      <NavBar />

      <div
        className='flex w-screen h-screen items-center justify-center'>
        Placeholder
      </div>

    </div>)

}

export default App

