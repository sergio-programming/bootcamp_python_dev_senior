import React from 'react'

export const NavBar = () => {
  return (
    <header className='bg-blue-400 text-white'>
        <nav className='mx-auto flex items-center justify-between p-6'>
            <div className='text-2xl font-bold'>
                Sistema de Tareas
            </div>
            <div className='flex gap-6 font-semibold'>
                <a href="#">Tareas</a>
                <a href="https://es.react.dev/">Documentacion de React</a>
            </div>
        </nav>
    </header>
  )
}
