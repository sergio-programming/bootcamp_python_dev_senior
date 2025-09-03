import React from "react";
import { useState } from "react";

const TaskItem = ({ task, onDelete, onToogle, onEdit }) => {

    const priorityText = {
        high: "Alta",
        medium: "Media",
        low: "Baja"
    }

    const [IsEditing, setIsEditing] = useState(false);
    const [editText, setEditText] = useState(task.text);

    const handleSave = () => {
        onEdit(task.id, editText);
        setIsEditing(false);
    }
    const handleCancel = () => {
        setEditText(task.text);
        setIsEditing(false);
    }

    return (
        <>
        <div className="bg-white rounded-lg shadow-md p-4 mb-3 border border-gray-200 hover:shadow-lg transition-shadow duration-300 ">
            <div className="flex items-center justify-between">
                <input 
                type="checkbox" 
                checked={task.completed}
                onChange={() => onToogle(task.id)} 
                className="h-5 w-5 text-blue-600 border-gray-300 focus:ring-blue:500 focus:ring-offset-0" 
                />

                {IsEditing ? (
                    <input
                        type="text"
                        value={editText}
                        onChange={(e) => setEditText(e.target.value)}
                        placeholder="Ingresa una nueva tarea..."
                        className="flex-1 px-4 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />

                ): (
                    <span 
                        className={task.completed ? "ml-1 text-green-500 font-bold": "ml-3 text-red-500 font-bold"}
                    >{task.text}
                    </span>
                )}
                
            </div>

            <div className="flex items-center space-x-2 m-4">
                {IsEditing ? (
                    <>

                    <button
                        onClick={handleSave} 
                        className="text-blue-600 hover:bg-blue-100 rounded-lg p-1 sm:p-2 transition-colors duration-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 cursor-pointer" title="Guardar tarea">
                            Guardar Tarea
                    </button>

                    <button 
                        onClick={handleCancel}
                        className="text-red-600 hover:bg-red-100 rounded-lg p-1 sm:p-2 transition-colors duration-300 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2 cursor-pointer" title="Cancelar edicion">
                            Cancelar Edicion
                    </button>
                    </>                
                        
                ): (
                <>
                <button
                onClick={() => setIsEditing(true)} 
                className="text-blue-600 hover:bg-blue-100 rounded-lg p-1 sm:p-2 transition-colors duration-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 cursor-pointer" title="Editar tarea">
                    Editar
                </button>

                <button 
                onClick={() => onDelete(task.id)}
                className="text-red-600 hover:bg-red-100 rounded-lg p-1 sm:p-2 transition-colors duration-300 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2 cursor-pointer" title="Eliminar tarea">
                    Eliminar
                </button>
                </>
                )}
            </div>

            {
                task.priority && (
                    <div className="mt-2">
                        <span className={`inline-flex px-2 py-1 text-xs font-semibold rounded-full
                            ${task.priority === 'high' ? 'bg-red-100 text-red-800' :
                            task.priority === 'medium' ? 'bg-yellow-100 text-yellow-800' :
                            'bg-green-100 text-green-800'}`}>

                            Prioridad: {priorityText[task.priority]}

                        </span>

                    </div>
                )
            }

        </div>

        </>
    )
}

export default TaskItem