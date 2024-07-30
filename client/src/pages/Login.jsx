import { useState } from "react"
import { useNavigate } from "react-router-dom";
import { useLogin } from "../hooks/useLogin"

const Login = () => {
    const [email, setEmail] = useState('')
    const { login, isLoading } = useLogin()
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault()

        await login(email)
        navigate("/")
    }

    return (

        <div className="min-h-screen flex items-center justify-center w-full">
            <div className="bg-white dark:bg-blue-900 shadow-md rounded-lg px-8 py-6 max-w-md">
                <h1 className="text-2xl font-bold text-center mb-4 dark:text-gray-200">Welcome Back!</h1>
                <form className="login" onSubmit={handleSubmit}>
                    <div className="mb-4">
                        <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Email Address</label>
                        <input type="email" id="email" className="shadow-sm rounded-md w-full px-3 py-2 border border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500" placeholder="your@email.com"
                            onChange={(e) => setEmail(e.target.value)}
                            value={email}
                            required />
                    </div>
                    <button disabled={isLoading} type="submit" className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-500 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">Login</button>
                </form>
            </div>
        </div>

    )
}

export default Login