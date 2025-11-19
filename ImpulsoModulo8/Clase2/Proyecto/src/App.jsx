import { NavBar } from "./components/NavBar"
import { Footer } from "./components/Footer"
import { TaskList } from "./components/TaskList"


function App() {

  return (
    <>
      <div className="min-h-screen flex flex-col">
        <NavBar></NavBar>
        <div className="flex-grow">
          <TaskList></TaskList>
        </div>
        <Footer></Footer>
      </div>
      
    </>
  )
}

export default App
