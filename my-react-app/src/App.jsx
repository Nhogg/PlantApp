import { Routes, Route } from 'react-router-dom'
import HomePage from './pages/homepage'
import About from './pages/About'
import Quiz from './pages/Quiz'

import './App.css'

function App() {
  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/about" element={<About />} />
      <Route path="/quiz" element={<Quiz />} />
    </Routes>
  )
}

export default App
