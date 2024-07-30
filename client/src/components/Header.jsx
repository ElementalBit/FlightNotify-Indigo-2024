import { NavLink } from 'react-router-dom';
import { Dialog } from '@headlessui/react'
import { Bars3Icon, XMarkIcon } from '@heroicons/react/24/outline'
import { useState } from 'react';

const navigation = [
  { name: 'About', href: '/#About' },
  { name: 'My Trips', href: '/my-trips' },
  { name: 'Notifications', href: '/notifications/all' },
  { name: 'Contact Us', href: '/#Contact' },
]

const Header = () => {
    const [mobileMenuOpen, setMobileMenuOpen] = useState(false)
    
    return (
        <header className="top-0">
            <nav className="flex justify-between items-center p-6" aria-label="Smriti">
                <div className="flex lg:flex-1">
                    <NavLink href="/" className="h-10 -m-1.5 p-1.5 flex gap-x-4">
                        <img className="h-8 w-auto" src="/images/logo.jpeg" alt="FlightNotify Logo" />
                        <span className="text-indigo-800 text-3xl font-bold">FlightNotify</span>
                    </NavLink>
                </div>

                <div className="flex lg:hidden">
                    <button
                        type="button"
                        className="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-gray-700"
                        onClick={() => setMobileMenuOpen(true)}
                    >
                        <span className="sr-only">Open main menu</span>
                        <Bars3Icon className="h-6 w-6" aria-hidden="true" />
                    </button>
                </div>
                <div className="hidden lg:flex lg:gap-x-12">
                    {navigation.map((item) => (
                        <NavLink key={item.name} to={item.href} className="text-sm font-semibold leading-6 text-gray-900">
                            {item.name}
                        </NavLink>
                    ))}
                </div>
                <div className="hidden lg:flex lg:flex-1 lg:justify-end">
                    <NavLink to="/login" className="text-sm font-semibold leading-6 text-gray-900">
                        Log in <span aria-hidden="true">&rarr;</span>
                    </NavLink>
                </div>
            </nav>
            <Dialog as="div" className="lg:hidden" open={mobileMenuOpen} onClose={setMobileMenuOpen}>
                <div className="fixed inset-0 z-50" />
                <Dialog.Panel className="fixed inset-y-0 right-0 z-50 w-full overflow-y-auto bg-white px-6 py-6 sm:max-w-sm sm:ring-1 sm:ring-gray-900/10">
                    <div className="flex items-center justify-between">
                        <NavLink to="/#" className="-m-1.5 p-1.5">
                            <span className="sr-only">FlightNotify</span>
                            <img
                                className="h-8 w-auto"
                                src="/images/logo.jpeg"
                                alt="FlightNotify Logo"
                            />
                        </NavLink>
                        <button
                            type="button"
                            className="-m-2.5 rounded-md p-2.5 text-gray-700"
                            onClick={() => setMobileMenuOpen(false)}
                        >
                            <span className="sr-only">Close menu</span>
                            <XMarkIcon className="h-6 w-6" aria-hidden="true" />
                        </button>
                    </div>
                    <div className="mt-6 flow-root">
                        <div className="-my-6 divide-y divide-gray-500/10">
                            <div className="space-y-2 py-6">
                                {navigation.map((item) => (
                                    <NavLink
                                        key={item.name}
                                        to={item.href}
                                        className="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50"
                                    >
                                        {item.name}
                                    </NavLink>
                                ))}
                            </div>
                            <div className="py-6">
                                <NavLink
                                    href="/login"
                                    className="-mx-3 block rounded-lg px-3 py-2.5 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50"
                                >
                                    Log in
                                </NavLink>
                            </div>
                        </div>
                    </div>
                </Dialog.Panel>
            </Dialog>
        </header>
    )
}

export default Header