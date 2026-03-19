import { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function Dashboard() {
    const [tasks, setTasks] = useState([]);
    const [title, setTitle] = useState("");
    const [loading, setLoading] = useState(true);

    const navigate = useNavigate();
    const token = localStorage.getItem("token");

    // redirect if no token
    useEffect(() => {
        if (!token) {
            navigate("/login");
        }
    }, [token, navigate]);

    // fetch tasks
    const fetchTasks = async () => {
        try {
            const res = await axios.get(
                "http://localhost:5000/api/tasks",
                {
                    headers: {
                        Authorization: `Bearer ${token}`,
                    },
                }
            );

            setTasks(res.data);
        } catch (err) {
            console.error(err);

            // if token invalid → logout
            logout();
        } finally {
            setLoading(false);
        }
    };

    // create task
    const createTask = async () => {
        if (!title) return alert("Enter task title");

        try {
            await axios.post(
                "http://localhost:5000/api/tasks",
                { title },
                {
                    headers: {
                        Authorization: `Bearer ${token}`,
                    },
                }
            );

            setTitle("");
            fetchTasks();
        } catch (err) {
            console.error(err);
        }
    };

    // logout (real)
    const logout = () => {
        localStorage.removeItem("token");
        navigate("/login");
    };

    useEffect(() => {
        fetchTasks();
    }, []);

    return (
        <div style={{ padding: 20 }}>
            <h2>Dashboard</h2>

            <button onClick={logout}>Logout</button>

            <br /><br />

            <input
                placeholder="Task title"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
            />

            <button onClick={createTask}>Add Task</button>

            <br /><br />

            {loading ? (
                <p>Loading tasks...</p>
            ) : (
                <ul>
                    {tasks.map((t) => (
                        <li key={t.id}>{t.title}</li>
                    ))}
                </ul>
            )}
        </div>
    );
}

export default Dashboard;