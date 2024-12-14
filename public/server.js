const express = require("express");
const http = require("http");
const { Server } = require("socket.io");
const dbConfig = require("./dbConfig");

const app = express();
const server = http.createServer(app);
const io = new Server(server);

let lobby = [];
let gameStarted = false;

// Serve static files (your frontend)
app.use(express.static("public"));

// Handle socket connections
io.on("connection", (socket) => {
    console.log("A player connected:", socket.id);

    if (lobby.length < 8 && !gameStarted) {
        // Add the player to the lobby
        lobby.push({ id: socket.id, name: `Player ${lobby.length + 1}` });
        io.emit("lobbyUpdate", lobby);
        console.log("Player joined:", socket.id);
    } else {
        socket.emit("message", "Lobby full or game already started.");
    }

    // Handle player disconnection
    socket.on("disconnect", () => {
        console.log("A player disconnected:", socket.id);
        lobby = lobby.filter((player) => player.id !== socket.id);
        io.emit("lobbyUpdate", lobby);
    });

    // Start the draft when 8 players are ready
    socket.on("startGame", () => {
        if (lobby.length === 8) {
            gameStarted = true;
            io.emit("gameStart", lobby);
        } else {
            socket.emit("message", "Need 8 players to start the game.");
        }
    });
});

server.listen(3000, () => {
    console.log("Server is running on http://localhost:3000");
});
