import { useState, useEffect } from "react";

const NotificationList = () => {
    // State for Page Details
    const [notifications, setnotifications] = useState([]);

    useEffect(() => {
        const fetchInfo = async () => {
            const response = await fetch('http://localhost:5050/api/get/notifications/all', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(JSON.parse(localStorage.getItem('user')))
            })
            const notificationsJSON = await response.json();

            if (response.ok) {
                setnotifications(notificationsJSON.notifications)
            }
        }

        fetchInfo();
    }, []);


    return (
        <div>
            <div className="flex flex-wrap justify-between items-center">
                <div className="w-3/5 inline-flex items-center gap-4">
                    <span className="text-emerald-950 text-2xl lg:text-4xl font-bold">
                        All Notifications
                    </span>
                </div>
            </div>
            <hr className="my-4 lg:my-6" />
            <div>
                <table className="w-full min-w-max table-fixed">
                    <thead className="border-2 text-lg border-b h-14 p-4 text-left bg-emerald-800/10">
                        <tr>
                            <th className="w-30 px-4">Title</th>
                            <th className="w-70 px-4">Content</th>
                        </tr>
                    </thead>
                    <tbody>
                        {notifications.map((notification) => (
                            <tr key= {notification} className="border-b h-12 transition-colors hover:bg-emerald-100/10 hover:shadow-md">
                                <td className="w-30 text-left px-4">
                                    
                                </td>
                                <td className="w-70 text-left px-4">
                                    {notification}
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>

        </div>
    )
}

export default NotificationList;