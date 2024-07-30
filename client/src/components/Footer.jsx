import { Link } from "react-router-dom"

const navigation = [
    { name: 'Home', href: '/#' },
    { name: 'About', href: '/#About' },
    { name: 'Contact Us', href: '/#Contact' },
    { name: 'FAQs', href: '/#' }
]

const currentYear = new Date().getFullYear();

const Footer = () => {
    return (
        <footer className="bottom-0 w-full bg-white p-6">
            <div className="flex flex-row flex-wrap items-center justify-center gap-y-6 gap-x-12 bg-white text-center md:justify-between">
                <img src="/images/logo.jpeg" alt="FlightNotify Logo" className="w-10" />
                <ul className="flex flex-wrap items-center gap-y-1 gap-x-8">
                    {navigation.map((item) => (
                        <li key={item.name}>
                            <Link to={item.href}
                                className="font-normal transition-colors hover:text-blue-500 focus:text-blue-500">
                                {item.name}
                            </Link>
                        </li>
                    ))}
                </ul>
            </div>
            <hr className="my-4 border-blue-gray-50" />
            <p className="text-center font-normal">
                &copy; FlightNotify {currentYear}
            </p>
        </footer>
    )
}

export default Footer;