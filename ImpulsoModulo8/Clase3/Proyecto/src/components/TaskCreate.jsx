import React from 'react'

export const TaskCreate = () => {
  return (
    <div className='m-6'>
      <form className='w-100 flex flex-col p-4 border border-gray-400 rounded-lg'>
        <h2 className='mt-2 text-xl text-center text-blue-400'>Registro de Tareas</h2>
        <label className='mt-2 text-blue-400'>Id</label>
        <input 
          type="number"
          className='px-4 py-2 border border-gray-300 rounded-lg' 
          placeholder='Ingrese el id...'
        />

        <label className='mt-2 text-blue-400'>Título</label>
        <input 
          type="text"
          className='px-4 py-2 border border-gray-300 rounded-lg'
          placeholder='Ingrese el título...'
        />

        <label className='mt-2 text-blue-400'>Descripción</label>
        <input 
          type="text"
          className='px-4 py-2 border border-gray-300 rounded-lg'
          placeholder='Ingrese la descripción...'
        />

        <label className='mt-2 text-blue-400'>Estado</label>
        <select className='px-4 py-2 border border-gray-400 rounded-lg'>
          <option value="">-- Selecciona una opción --</option>
          <option value="pendiente">Pendiente</option>
          <option value="en-proceso">En proceso</option>
          <option value="completado">Completado</option>
        </select>

      </form>
    </div>
  )
}
