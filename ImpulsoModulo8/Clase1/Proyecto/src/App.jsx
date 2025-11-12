import { useState } from 'react'
import './App.css'

function App() {

  const [contador, setContador] = useState(0);

  const incrementar = () => {
    setContador(contador + 1);
  }

  const decrementar = () => {
    if (contador > 0) {
      setContador(contador - 1);
    } else {
      return contador;
    }
    
  }

  return (
    <>
      <div className='flex flex-col justify-center items-center min-h-screen'>
        <div className='flex flex-col p-4 bg-gray-100 w-3/4 items-center border border-blue-400 rounded-lg'>
          <h1 className=' mt-2 text-center text-blue-600 font-bold'>Hola Programadores</h1>
          <h3 className='mt-2 text-center text-blue-500 font-semibold'>Contador</h3>
          <p className='mt-2 text-xl text-center text-blue-400 '>{ contador }</p>
          <button onClick={incrementar} className='mt-2 bg-blue-400 py-2 px-4 rounded-lg text-white cursor-pointer'>Incrementar</button>
          <button onClick={decrementar} className='mt-2 bg-blue-400 py-2 px-4 rounded-lg text-white cursor-pointer'>Decrementar</button>
        </div>
      </div>
    </>
  )
}

export default App
