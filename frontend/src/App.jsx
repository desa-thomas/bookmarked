import { useState } from 'react'
import './index.css'

// Import router for pages
import { HashRouter as Router, Routes, Route } from "react-router-dom"

// Import Pages 
import HomePage from './pages/HomePage'
import BookshelfPage from './pages/BookshelfPage'
import CommunityPage from './pages/CommunityPage'
import SearchResultsPage from './pages/SearchResultsPage'
// Import Components


import NavBar from './components/NavBar'

function App() {
  const [count, setCount] = useState(0)

  return (

    <div className='flex font-open-sans flex flex-col min-w-screen min-h-screen bg-bgprimary'>

      <Router>
        <NavBar  />
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/search" element={<SearchResultsPage />} />
          <Route path="/bookshelf" element={<BookshelfPage />} />
          <Route path="/community" element={<CommunityPage />} />
        </Routes>
      </Router>
    </div>)

}

export default App

