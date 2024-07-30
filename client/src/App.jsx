import { Outlet } from "react-router-dom";

// Pages and Components
import Header from "./components/Header";
import Footer from "./components/Footer";

const App = () => {
	return (
		<div className="w-full flex flex-col h-screen">
			<Header />
			<div className="flex-grow p-6">
				<Outlet />
			</div>
			<Footer />
		</div>
	)
}

export default App;
