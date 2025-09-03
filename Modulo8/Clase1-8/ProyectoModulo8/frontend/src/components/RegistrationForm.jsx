import useFormValidation from "../hooks/useFormValidation";

const RegistrationForm = ( {onSwitchToLogin} ) => {

    const { values, getFieldProps, errors, validateAll, reset } = useFormValidation({
        username: '',
        email: '',
        password: '',
        confirmPassword: ''
    })

    const handleSubmit = (e) => {
        e.prevenDefault();
        if (validateAll()) {
            alert('Registro exitoso');
            reset();
        }else{
            alert('Por favor corrige los errores antes de enviar el formulario');
        }

    }

    const usernameProps = getFieldProps('username');
    const emailProps = getFieldProps('email');
    const passwordProps = getFieldProps('password');
    const confirmPasswordProps = getFieldProps('confirmPassword');

    return (
        <div className="w-full max-w-md mx-auto">
            <div className="bg-white shadow-lg rounded-lg p-6">
                <div className="text-center mb-6">
                    <h2 className="text-2xl font-bold text-gray-900">Crea tu cuenta</h2>
                    <p className="text-gray-600 mt-2"></p>
                </div>

                <form onSubmit={handleSubmit} className="space-y-4">

                    <div>
                        <label htmlFor="username" className="block text-sm font-medium text-gray-700 mb-1">Usuario:</label>
                        <input
                            id="username" 
                            type="text"
                            placeholder="Ingresa tu usuario..."
                            { ...usernameProps }   
                        />
                        {usernameProps.hasError && (
                            <p className="mt-1 text-sm text-red-600 flex items-center">
                                <svg className="w-4 h-4 mr-1" fill="currentColor" viewBox="0 0 20 20">
                                    <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clipRule="evenodd" />
                                </svg>
                                {usernameProps.error}
                            </p>
                        )}
                        {
                            usernameProps.isValid && (
                                <p className="mt-1 text-sm text-green-600 flex items-center">
                                    <svg className="w-4 h-4 mr-1" fill="currentColor" viewBox="0 0 20 20">
                                        <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clipRule="evenodd" />
                                    </svg>
                                    Usuario valido                                  
                                </p>
                            )
                        }  
                    </div>

                    <div>
                        <label htmlFor="email" className="block text-sm font-medium text-gray-700 mb-1">Email:</label>
                        <input
                            id="email" 
                            type="email"
                            placeholder="Ingresa tu correo..."
                            {...emailProps}   
                        />
                        {emailProps.hasError && (
                            <p className="mt-1 text-sm text-red-600 flex items-center">
                                <svg className="w-4 h-4 mr-1" fill="currentColor" viewBox="0 0 20 20">
                                    <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clipRule="evenodd" />
                                </svg>
                                {emailProps.error}
                            </p>
                        )}
                        {
                            emailProps.isValid && (
                                <p className="mt-1 text-sm text-green-600 flex items-center">
                                    <svg className="w-4 h-4 mr-1" fill="currentColor" viewBox="0 0 20 20">
                                        <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clipRule="evenodd" />
                                    </svg>
                                    Email valido                                  
                                </p>
                            )
                        }
                    </div>

                    <div>
                        <label htmlFor="password" className="block text-sm font-medium text-gray-700 mb-1">Contraseña:</label>
                        <input
                            id="password" 
                            type="password"
                            placeholder="Ingresa tu contraseña..."
                            {...passwordProps}   
                        />
                        {passwordProps.hasError && (
                            <p className="mt-1 text-sm text-red-600 flex items-center">
                                <svg className="w-4 h-4 mr-1" fill="currentColor" viewBox="0 0 20 20">
                                    <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clipRule="evenodd" />
                                </svg>
                                {passwordProps.error}
                            </p>
                        )}
                        {
                            passwordProps.isValid && (
                                <p className="mt-1 text-sm text-green-600 flex items-center">
                                    <svg className="w-4 h-4 mr-1" fill="currentColor" viewBox="0 0 20 20">
                                        <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clipRule="evenodd" />
                                    </svg>
                                    Password valido                                  
                                </p>
                            )
                        }
                        {
                            !passwordProps.hasError && !passwordProps.isValid && (
                                <div className="mt-1 text-xs text-gray-500">
                                    La contraseña debe tener: 8+ caracteres, una mayuscula, minuscula y un número.
                                </div>
                            )
                        }
                    </div>

                    <div>
                        <label htmlFor="confirmPassword" className="block text-sm font-medium text-gray-700 mb-1">Confirmar Contraseña:</label>
                        <input
                            id="confirmPassword" 
                            type="password"
                            placeholder="Confirma tu contraseña..."
                            {...confirmPasswordProps}   
                        />
                        {confirmPasswordProps.hasError && (
                            <p className="mt-1 text-sm text-red-600 flex items-center">
                                <svg className="w-4 h-4 mr-1" fill="currentColor" viewBox="0 0 20 20">
                                    <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clipRule="evenodd" />
                                </svg>
                                {confirmPasswordProps.error}
                            </p>
                        )}
                        {
                            confirmPasswordProps.isValid && (
                                <p className="mt-1 text-sm text-green-600 flex items-center">
                                    <svg className="w-4 h-4 mr-1" fill="currentColor" viewBox="0 0 20 20">
                                        <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clipRule="evenodd" />
                                    </svg>
                                    Email valido                                  
                                </p>
                            )
                        }
                    </div>

                    <button 
                        type="submit"

                        className="mt-5 w-full bg-blue-600 text-white py-2 px-4 rounde-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition-colors duration-300 cursor-pointer"
                    >
                        Crear Cuenta
                    </button>

                </form>

                <div className="mt-6 text-center">
                    <p className="text-gray-600">
                        ¿Ya tienes una cuenta?
                    </p>
                    <button
                        onClick={onSwitchToLogin}
                        className="ml-2 text-blue-600 hover:text-blue-700 font-medium cursor-pointer focus:underline transition-colors duration-300"
                    >
                        Iniciar Sesión
                    </button>
                </div>

            </div>
        </div>
    )
} 

export default RegistrationForm;