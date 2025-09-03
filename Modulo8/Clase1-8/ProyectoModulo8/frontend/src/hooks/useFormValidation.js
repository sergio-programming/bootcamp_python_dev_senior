import { useState, useCallback } from "react";

const validationRules = {
    username: (value) => {
        if(!value || value.trim() === '') {
            return "El nombre del usuario es obligatorio";
        }
        return '';
    },
    email: (value) => {
        if(!value || value.trim() === '') {
            return "El email es obligatorio";
        }
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
            return "El email no es valido";
        }
        return '';

    },
    password: (value) => {
        if(!value) {
            return "La contraseña es obligatoria";
        }
        if (value.length < 8) {
            return "La contraseña debe tener un minimo de 8 caracteres";
        }
        if (!/(?=.*[a-z])/.test(value)) {
            return "La contraseña debe contener al menos una minúscula";
        }
        if (!/(?=.*[A-Z])/.test(value)) {
            return "La contraseña debe contener al menos una mayúscula";
        }
        if (!/(?=.*\d)/.test(value)) {
            return "La contraseña debe contener al menos un número";
        }
        return '';
    },
    confirmPassword: (value, originalPassword) => {
        if (!value) {
            return "La confirmación de contraseña es obligatoria";
        }
        if (value !== originalPassword) {
            return "Las contraseñas deben coincidir";
        }
        return '';

    }

}

const useFormValidation = (initialValues = {}) => {
    const [values, setValues] = useState({});
    const [errors, setErrors] = useState({});
    const [touched, setTouched] = useState({});

    const validateField = useCallback((name, value, allValues=values) => {
        let error = '';

        if (validationRules[name]) {
            if (name === 'confirmPassword') {
                error = validationRules[name](value, allValues.password);
            } else {
                error = validationRules[name](value);
            }
        }

        return error;       

    }, [values])

    const handleChange = useCallback((name, value) => {
        setValues(prev => ({
            ...prev,
            [name]: value
        }))

        if (touched[name]) {
            const newValues = {...values, [name]: value};
            const error = validateField(name, value, newValues);
            setErrors(prev => ({
                ...prev,
                [name]: error
            }))
        }
    }, [touched, values, validateField])

    const handleBlur = useCallback((name) => {
        setTouched(prev => ({
            ...prev,
            [name]: true
        }))

        const error = validateField(name, values[name]);
        setErrors(prev => ({
            ...prev,
            [name]: error
        }))
    }, [values, validateField])

    const validateAll = useCallback(() => {
        const newErrors = {}
        let isValid = true;

        Object.keys(values).forEach(name => {
            const error = validateField(name, values[name]);
            newErrors[name] = error;
            if (error) {
                isValid = false;
            }
        })
        setErrors(newErrors);
        setTouched(Object.keys(values).reduce((acc, key) => {
            acc[key] = true;
            return acc;
        }, {}));
        return isValid;
    }, [values, validateField]);

    const reset = useCallback(() => {
        setValues(initialValues);
        setErrors({});
        setTouched({});
    }, [initialValues])

    const getFieldProps = useCallback((name) => {
        const hasError = touched[name] && errors[name];
        const isValid = touched[name] && !errors[name] && values[name];
        const isPristine = !touched[name];

        return {
            value: values[name] || '',
            onChange: (e) => handleChange(name, e.target.value),
            onBlur: () => handleBlur(name),
            className: `w-full px-4 py-2 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 
                        ${hasError ? 'border-red-500 focus:ring-red-500 focus:border-red-500'
                          : isValid ? 'border-green-500 focus:ring-green-500 focus:border-green-500'
                           : 'border-blue-100 focus:ring-blue-500 focus:border-blue-500'}`,
            error: hasError ? errors[name]: '',
            isValid,
            isPristine,
            hasError,
        }
    }, [values, errors, touched, handleChange, handleBlur])

    return {
        values,
        errors,
        touched,
        handleChange,
        handleBlur,
        validateAll,
        reset,
        getFieldProps,
    }

    
}
export default useFormValidation;