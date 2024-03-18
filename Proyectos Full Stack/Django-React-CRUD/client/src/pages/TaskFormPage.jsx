import { useEffect } from "react";
import { useForm } from "react-hook-form";
import { createTask, deleteTask, updateTask, getTask } from "../api/tasks.api";
import { useNavigate, useParams } from "react-router-dom";
import { toast } from "react-hot-toast";


export function TasksFormPage() {

    const {register, 
        handleSubmit, 
        formState: { errors },
        setValue //Poner los valores del formulario
    
    } = useForm()

    const navigate = useNavigate();
    const params = useParams();

    const onSubmit = handleSubmit(async data => {
        //console.log(data)
        if (params.id) {
            console.log("actualizando");
            await updateTask(params.id, data)
            toast.success('Tarea actualizada exitosamente...',{
                position: "bottom-right",
                style: {
                    background: "#101010",
                    color: "#FFFFFF"
                }
            })

        }else{
            await createTask(data)
            toast.success('Tarea creada exitosamente...',{
                position: "bottom-right",
                style: {
                    background: "#101010",
                    color: "#FFFFFF"
                }
            })
        }

        navigate("/tasks");
        
        
    });

    //yup
    //zod //librerias para validaciones complejas 

    useEffect(() => {
    
        async function loadTask() {
            if (params.id){
                console.log('obteniendo datos');
                const { data} = await getTask(params.id);
                setValue('title', data.title)
                setValue('description', data.description)
            }
        }
        loadTask();
    }, [])

    return (
        <div className="max-w-xl mx-auto">
            <form onSubmit={onSubmit}>
                <input type="text" placeholder="title" 
                    {...register("title", { required: true })}
                    className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
                />
                {errors.title && <span>Este campo es requerido</span>}
                <textarea placeholder="Description" rows="3"
                    {...register("description", { required: true })}
                    className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
                ></textarea>
                {errors.description && <span>Este campo es requerido</span>}
                <button className="bg-indigo-500 p-3 rounded-lg block w-full mt-3">Save</button>
            </form>

            {params.id && (
            <div className="flex justify-end">
                <button className="bg-red-500 p-3 rounded-lg w-48 mt-3"
                onClick = { async () => {
                const accepted = window.confirm("estas seguro?");
                if (accepted) {
                    await deleteTask(params.id);
                    toast.success('Tarea eliminada exitosamente...',{
                        position: "bottom-right",
                        style: {
                            background: "#101010",
                            color: "#FFFFFF"
                        }
                    })
                    navigate("/tasks");
                }
                }}
                >
                Delete
                </button>
                
            </div>

            )}
            
        </div>
    );
}