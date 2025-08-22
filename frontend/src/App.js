import React, { useEffect, useRef, useState } from 'react'

const BACKEND_URL =
    import.meta.env.VITE_BACKEND_URL || 'http://127.0.0.1:5000'

export default function App() {
    const [messages, setMessages] = useState([])
    const [input, setInput] = useState('')
    const [loading, setLoading] = useState(false)
    const [error, setError] = useState('')
    const listEndRef = useRef(null)

    useEffect(() => {
        listEndRef.current ? .scrollIntoView({ behavior: 'smooth' })
    }, [messages])

    async function sendMessage(e) {
        e.preventDefault()
        if (!input.trim()) return
        setError('')
        const userMessage = { role: 'user', content: input.trim(), timestamp: new Date().toISOString() }
        setMessages(prev => [...prev, userMessage])
        setInput('')
        setLoading(true)
        try {
            const res = await fetch(`${BACKEND_URL}/chat`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: userMessage.content })
            })
            if (!res.ok) {
                const text = await res.text()
                throw new Error(text || `HTTP ${res.status}`)
            }
            const data = await res.json()
            const botMessage = { role: 'assistant', content: data.reply, timestamp: data.timestamp }
            setMessages(prev => [...prev, botMessage])
        } catch (err) {
            setError('Failed to get response from backend')
            console.error(err)
        } finally {
            setLoading(false)
        }
    }

    return ( <
        div className = "min-h-screen flex flex-col" >
        <
        header className = "sticky top-0 bg-white border-b z-10" >
        <
        div className = "max-w-3xl mx-auto px-4 py-4 flex items-center justify-between" >
        <
        h1 className = "text-xl font-semibold" > SITCOE College Chatbot < /h1> <
        span className = "text-xs text-gray-500" > Backend: { BACKEND_URL } < /span> <
        /div> <
        /header>

        <
        main className = "flex-1" >
        <
        div className = "max-w-3xl mx-auto px-4 py-4" >
        <
        div className = "bg-white rounded-lg border h-[70vh] overflow-y-auto p-4 space-y-4" > {
            messages.length === 0 && ( <
                div className = "text-center text-gray-500 mt-20" >
                <
                p > Ask me about admissions, courses, fees, placements, and more. < /p> <
                /div>
            )
        }

        {
            messages.map((m, idx) => ( <
                div key = { idx }
                className = { m.role === 'user' ? 'text-right' : 'text-left' } >
                <
                div className = { `inline-block px-3 py-2 rounded-lg max-w-[80%] whitespace-pre-wrap ${m.role === 'user' ? 'bg-blue-600 text-white' : 'bg-gray-100 text-gray-900'}` } > { m.content } <
                /div> <
                /div>
            ))
        } <
        div ref = { listEndRef }
        /> <
        /div>

        {
            error && ( <
                p className = "text-red-600 text-sm mt-2" > { error } < /p>
            )
        }

        <
        form onSubmit = { sendMessage }
        className = "mt-4 flex gap-2" >
        <
        input type = "text"
        value = { input }
        onChange = { e => setInput(e.target.value) }
        placeholder = "Type your message..."
        className = "flex-1 border rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500" /
        >
        <
        button type = "submit"
        disabled = { loading }
        className = "px-4 py-2 rounded-md bg-blue-600 text-white disabled:opacity-60" >
        { loading ? 'Sending...' : 'Send' } <
        /button> <
        /form> <
        /div> <
        /main>

        <
        footer className = "border-t bg-white" >
        <
        div className = "max-w-3xl mx-auto px-4 py-3 text-xs text-gray-500" >
        Built with React + Vite + Tailwind <
        /div> <
        /footer> <
        /div>
    )
}