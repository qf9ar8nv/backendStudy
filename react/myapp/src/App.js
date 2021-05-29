
function App() {
	function printHello(callback) {
		setTimeout(() => {
			console.log("hello")
			callback()
		}, 1000);
	}

	function printDelete() {
		console.log("delete")
	}
	function click() {
		console.log("create")
		printHello(printDelete)
	}

	return (
		<div className="App">
			<button onClick={click}>button</button>
		</div>
	);
}

export default App;
