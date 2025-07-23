import './App.css'
import Footer from './components/Footer'
import Header from './components/Header'
import TaskList from './components/TaskList'

function App() { 

  return (
    <>
      <div className='min-h-screen flex flex-col'>
        <Header></Header>
        <main className='flex-1 py-8'>
          <TaskList></TaskList>
        </main>
        <Footer></Footer>
      </div>
      
    </>
  )
}

export default App
