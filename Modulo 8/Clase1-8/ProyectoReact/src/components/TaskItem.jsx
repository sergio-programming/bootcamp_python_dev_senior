import React from "react";

const TaskItem = ({ task }) => {
    return (
        <>
        <div className="bg-white rounded-lg shadow-md p-4 mb-3 border border-gray-200 hover:shadow-lg transition-shadow duration-300 ">
            <div className="flex items-center justify-between">
                <input type="checkbox" checked={task.completed} className="h-5 w-5 text-blue-600 border-gray-300 focus:ring-blue:500 focus:ring-offset-0" />
                <span className="ml-3 flex-1 text-sm">
                    {task.text}
                </span>
            </div>

            <div className="flex items-center space-x-2 ml-4">
                <>
                <button className="text-blue-600 hover:bg-blue-100 rounded-lg p-1 sm:p-2 transition-colors duration-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2" title="Editar tarea">
                    Editar
                </button>

                <button className="text-red-600 hover:bg-red-100 rounded-lg p-1 sm:p-2 transition-colors duration-300 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2" title="Eliminar tarea">
                    Eliminar
                </button>
                </>
            </div>

        </div>

        </>
    )
}

export default TaskItem