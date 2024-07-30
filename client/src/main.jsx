import React from 'react'
import ReactDOM from 'react-dom/client'
import {
	createBrowserRouter,
	RouterProvider,
} from 'react-router-dom'

import App from './App.jsx'

// Pages and Components
import Home from './pages/Home'
import Trips from './pages/Trips'

import './index.css'
import Login from './pages/Login.jsx'
import Notifications from './pages/Notifications.jsx'

const router = createBrowserRouter([
	{
		path: "/",
		element: <App />,
		children: [
			{
				path: "/",
				element: <Home />,
			}
		]
	},
	{
		path: "/my-trips",
		element: <App />,
		children: [
			{
				path: "/my-trips",
				element: <Trips />
			}
		],
	},
	{
		path: "/login",
		element: <App />,
		children: [
			{
				path: "/login",
				element: <Login />
			},
		]
	},
	{
		path: "/notifications",
		element: <App />,
		children: [
			{
				path: "/notifications/all",
				element: <Notifications />
			}
		]
	}
]);

console.log("inside main.jsx")
ReactDOM.createRoot(document.getElementById('root')).render(
	<React.StrictMode>
		<RouterProvider router={router} />
	</React.StrictMode>,
)
