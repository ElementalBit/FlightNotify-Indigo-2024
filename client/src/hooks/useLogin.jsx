import { useState } from 'react'

export const useLogin = () => {
    const [isLoading, setIsLoading] = useState(null)

    const login = async (email) => {
        setIsLoading(true)

        const response = await fetch('http://localhost:5050/api/user/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email })
        })
        const json = await response.json()

        if (!response.ok) {
            setIsLoading(false)
        }
        if (response.ok) {
            // save the user to local storage
            localStorage.setItem('user', JSON.stringify(json))

            // update loading state
            setIsLoading(false)
        }
    }

    return { login, isLoading }
}