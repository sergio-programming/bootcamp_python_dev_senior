import { useState, useEffect } from "react";
import taskData from '../data/tasks.json';

const useTasks = () => {
    const [task, setTask] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchTasks = async () => {
            try {
                setLoading(true);
                setError(null);
                const response = await fetch('https://mi-fake-api.com/api/tasks');
                if (!response.ok) {
                    throw new Error('Error al cargar las tareas');
                }
                const data = await response.json();
                setTask(data);
            } catch (err) {
                console.log("No se pudieron cargar las tareas, se carga mock data: ", err);
                setTask(taskData);
                setError(null);                                
            }finally{
                setLoading(false)
            }
        }
        fetchTasks();
    }, []);
    return {
        task,
        loading,
        error,
        setTask
    }
}
export default useTasks;