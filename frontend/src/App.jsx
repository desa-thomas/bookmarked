import { useState } from 'react'
import './index.css'

// Import router for pages
import { HashRouter as Router, Routes, Route } from "react-router-dom"

// Import Pages 
import HomePage from './pages/HomePage'
import BookshelfPage from './pages/BookshelfPage'
import CommunityPage from './pages/CommunityPage'
// Import Components


import NavBar from './components/NavBar'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className='font-sans'>
      <NavBar/>
      
      <Router>
        <Routes>
          <Route path="/" element={<HomePage/>}/>
          <Route path="/bookshelf" element = {<BookshelfPage/>}/>
          <Route path="/community" element = {<CommunityPage/>}/>
        </Routes>
      </Router>
    </div>)

}

export default App

