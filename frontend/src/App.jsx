import React, { useState } from 'react'

export default function App() {
	const [message, setMessage] = useState('')
	const [reply, setReply] = useState('')
	const [isLoading, setIsLoading] = useState(false)
	const [error, setError] = useState('')

	async function sendMessage(event) {
		event.preventDefault()
		setIsLoading(true)
		setError('')
		setReply('')
		try {
			const response = await fetch('http://localhost:5000/chat', {
				method: 'POST',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify({ message })
			})
			const data = await response.json()
			if (!response.ok) {
				throw new Error(data?.error || 'Request failed')
			}
			setReply(data?.reply || '')
		} catch (err) {
			setError(err.message)
		} finally {
			setIsLoading(false)
		}
	}

	return (
		<div className="min-h-screen p-6 flex flex-col gap-4">
			<h1 className="text-2xl font-semibold">SITCOE College Chatbot</h1>
			<form onSubmit={sendMessage} className="flex gap-2">
				<input
					className="flex-1 border rounded px-3 py-2"
					placeholder="Ask something about admissions, courses, fees..."
					value={message}
					onChange={(e) => setMessage(e.target.value)}
				/>
				<button
					type="submit"
					className="bg-blue-600 text-white px-4 py-2 rounded disabled:opacity-50"
					disabled={!message || isLoading}
				>
					{isLoading ? 'Sending...' : 'Send'}
				</button>
			</form>
			{error && (
				<div className="border rounded p-3 bg-red-50 text-red-700">{error}</div>
			)}
			{reply && !error && (
				<div className="border rounded p-3 bg-white whitespace-pre-wrap">{reply}</div>
			)}
		</div>
	)
}



