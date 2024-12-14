const socket = io();

// Update lobby when a new player joins
socket.on("lobbyUpdate", (lobby) => {
    const lobbyDiv = document.getElementById("lobby");
    lobbyDiv.innerHTML = `<h3>Players (${lobby.length}/8)</h3>` + 
        lobby.map(player => `<p>${player.name}</p>`).join("");
    document.getElementById("startGame").disabled = lobby.length < 8;
});

// Start game button
document.getElementById("startGame").addEventListener("click", () => {
    socket.emit("startGame");
});

// Handle game start
socket.on("gameStart", (lobby) => {
    alert("Game is starting!");
    console.log("Players:", lobby);
    // Redirect to game page or start drafting logic
});

// Display messages
socket.on("message", (msg) => {
    alert(msg);
});
