import React from 'react'

export const TaskList = () => {

    const tareas = [
        { id: 1, titulo: "Estudiar React", descripcion: "Estudiar los fundamentos de React como useState, props y eventos", estado: "En proceso" },
        { id: 2, titulo: "Practicar JavaScript", descripcion: "Resolver ejercicios de funciones, arreglos y objetos", estado: "Pendiente" },
        { id: 3, titulo: "Avanzar en Django", descripcion: "Implementar vistas y modelos para el proyecto de cursos", estado: "En proceso" },
        { id: 4, titulo: "Hacer ejercicio", descripcion: "Entrenamiento de 45 minutos para perder grasa", estado: "Completado" },
        { id: 5, titulo: "Leer sobre Transformada de Laplace", descripcion: "Revisar ejemplos y ejercicios típicos", estado: "Pendiente" },
        { id: 6, titulo: "Crear Navbar en React", descripcion: "Diseñar un navbar usando Tailwind CSS y componentes", estado: "Pendiente" },
        { id: 7, titulo: "Práctica de POO en JavaScript", descripcion: "Crear clases y objetos para afianzar conceptos", estado: "En proceso" },
        { id: 8, titulo: "Organizar archivo camisetas.js", descripcion: "Optimizar la carga y visualización de camisetas", estado: "Pendiente" },
        { id: 9, titulo: "Estudiar análisis y diseño de sistemas", descripcion: "Revisar diagramas UML y casos de uso", estado: "Pendiente" },
        { id: 10, titulo: "Aprender Tailwind Layout", descripcion: "Practicar grid y flexbox para diseños responsivos", estado: "Completado" }
    ];


  return (

    
    <div className='m-6 flex flex-col'>
        <table className='border border-cyan-600'>
            <thead className='bg-cyan-700 text-white'>
                <tr>
                    <th className='px-6 py-3 text-left font-semibold'>ID</th>
                    <th className='px-6 py-3 text-left font-semibold'>Titulo</th>
                    <th className='px-6 py-3 text-left font-semibold'>Descripción</th>
                    <th className='px-6 py-3 text-left font-semibold'>Estado</th>
                </tr>
            </thead>
            <tbody>
                {
                    tareas.map(tarea => {
                        return (
                            <tr className='hover:bg-cyan-800 transition-colors duration-200'>
                                <td className='px-6 py-3 text-gray-500'>{tarea.id}</td>
                                <td className='px-6 py-3 text-gray-500'>{tarea.titulo}</td>
                                <td className='px-6 py-3 text-gray-500'>{tarea.descripcion}</td>
                                <td className='px-6 py-3 text-gray-500'>{tarea.estado}</td>
                            </tr>
                        )
                    })
                }
            </tbody>
        </table>
    </div>
  )
}
