import './App.css'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import { Home } from './components/Home'
import { TaskCreate } from './components/TaskCreate'
import { TaskList } from './components/TaskList'
import { NavBar } from './components/NavBar'
import { Footer } from './components/Footer'

function App() {

  return (
    <>
      <BrowserRouter>
        <div className="min-h-screen flex flex-col">
          
          <NavBar/>

          <div className='flex flex-grow items-center justify-center'>
            <Routes>
              <Route path="/" element={<Home/>} />
              <Route path="/crear-tareas" element={<TaskCreate/>} />
              <Route path="/ver-tareas" element={<TaskList/>} />
            </Routes>
          </div>

          <Footer/>
        </div>
      </BrowserRouter>
    </>
  )
}

export default App
