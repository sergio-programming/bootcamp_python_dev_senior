import React from 'react'

export const Footer = () => {
  return (
    <footer className='bg-blue-400 text-white'>
        <div className='mx-auto flex p-6'>
            <div className='w-1/2 text-center font-semibold'>
                <p className='mt-2'>Sistema de Tareas</p>
                <p className='mt-2'>Puedes registrar sus tareas</p>
                <p className='mt-2'>Puedes visualizar sus tareas</p>
            </div>
            <div className='w-1/2 text-center    font semibold'>
                <p className='mt-2'>Tareas</p>
                <p className='mt-2'>Documentación de React</p>
                <p className='mt-2'>Documentación de Python</p>
            </div>

        </div>

    </footer>
  )
}