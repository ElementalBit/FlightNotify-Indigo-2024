import { useState, useEffect } from "react";

const Trips = () => {
    // State for Page Details
    const [trips, settrips] = useState([]);

    useEffect(() => {
        const fetchInfo = async () => {
            const response = await fetch('http://localhost:5050/api/get/trips/all', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(JSON.parse(localStorage.getItem('user')))
            })
            const tripsJSON = await response.json();

            if (response.ok) {
                settrips(tripsJSON)
            }
        }

        fetchInfo();
    }, []);


    return (
        <div>
            <div className="flex flex-wrap justify-between items-center">
                <div className="w-3/5 inline-flex items-center gap-4">
                    <span className="text-emerald-950 text-2xl lg:text-4xl font-bold">
                        All trips
                    </span>
                </div>
            </div>
            <hr className="my-4 lg:my-6" />
            <div>
                <table className="w-full min-w-max table-fixed">
                    <thead className="border-2 text-lg border-b h-14 p-4 text-left bg-emerald-800/10">
                        <tr>
                            <th className="w-25 px-4">PNR</th>
                            <th className="w-25 px-4">Status</th>
                            <th className="w-25 px-4">Departure</th>
                            <th className="w-25 px-4">Arrival</th>
                        </tr>
                    </thead>
                    <tbody>
                        {trips.map((trip) => (
                            <tr key= {trip._id} className="border-b h-12 transition-colors hover:bg-emerald-100/10 hover:shadow-md">
                                <td className="w-25 text-left px-4">
                                    {trip.PNR}
                                </td>
                                <td className="w-25 text-left px-4">
                                    {trip.status}
                                </td>
                                <td className="w-25 text-left px-4">
                                    {trip.flight_details[0].departure_airport}
                                </td>
                                <td className="w-25 text-left px-4">
                                    {trip.flight_details[0].arrival_airport}
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>

        </div>
    )
}

export default Trips;