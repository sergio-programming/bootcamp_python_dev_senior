import React from 'react'
import { Link } from 'react-router-dom'

export const NavBar = () => {
  return (
    <header className='bg-blue-400 text-white'>
        <nav className='mx-auto flex items-center justify-between p-6'>
            <div className='text-2xl font-bold'>
                Sistema de Tareas
            </div>
            <div className='flex gap-6 font-semibold'>
                <Link to="/">Inicio</Link>
                <Link to="/crear-tareas">Crear Tareas</Link>
                <Link to="/ver-tareas">Ver Tareas</Link>
            </div>
        </nav>
    </header>
  )
}