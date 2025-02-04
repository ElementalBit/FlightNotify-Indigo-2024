import { LockClosedIcon, ClockIcon, PaintBrushIcon, ChatBubbleLeftRightIcon } from '@heroicons/react/24/outline'

const features = [
    {
        name: 'Timely Updates',
        description:
            'Get instant alerts about delays, gate changes, cancellations, and more.',
        icon: ClockIcon,
    },
    {
        name: 'Multiple Channels:',
        description:
            "Whether you prefer email, SMS, or app notifications, we've got you covered.",
        icon: ChatBubbleLeftRightIcon,
    },
    {
        name: 'Reliable Information:',
        description:
            'We source data directly from airlines and airports to ensure accuracy.',
        icon: LockClosedIcon,
    },
    {
        name: 'Customizable Alerts:',
        description:
            'Tailor your notifications to include only the information that matters most to you.',
        icon: PaintBrushIcon,
    },
]

const Home = () => {
    return (
        <div>
            <section id="banner">
                <div className="bg-white py-24 sm:py-32">
                    <div className="mx-auto max-w-7xl px-6 lg:px-8">
                        <div className="mx-auto max-w-2xl lg:text-center">
                            <h2 className="text-base font-semibold leading-7 text-indigo-600">Welcome to FlightNotify</h2>
                            <p className="mt-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
                                Stay Updated with Real-Time Flight Status Alerts!
                            </p>
                            <p className="mt-6 text-lg leading-8 text-gray-600">
                                Quis tellus eget adipiscing convallis sit sit eget aliquet quis. Suspendisse eget egestas a elementum
                                pulvinar et feugiat blandit at. In mi viverra elit nunc.
                            </p>
                        </div>
                        <div className="mx-auto mt-16 max-w-2xl sm:mt-20 lg:mt-24 lg:max-w-4xl">
                            <dl className="grid max-w-xl grid-cols-1 gap-x-8 gap-y-10 lg:max-w-none lg:grid-cols-2 lg:gap-y-16">
                                {features.map((feature) => (
                                    <div key={feature.name} className="relative pl-16">
                                        <dt className="text-base font-semibold leading-7 text-gray-900">
                                            <div className="absolute left-0 top-0 flex h-10 w-10 items-center justify-center rounded-lg bg-indigo-600">
                                                <feature.icon aria-hidden="true" className="h-6 w-6 text-white" />
                                            </div>
                                            {feature.name}
                                        </dt>
                                        <dd className="mt-2 text-base leading-7 text-gray-600">{feature.description}</dd>
                                    </div>
                                ))}
                            </dl>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    )
}

export default Home;