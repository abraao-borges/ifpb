package com.jdbc;

import com.jdbc.dao.GameDAO;
import com.jdbc.entity.Game;

import java.sql.Date;

public class Main {
    public static void main(String[] args) {
        GameDAO gameDAO = new GameDAO();

        // Insert a new Game
        Game newGame = new Game("Cyberpunk 2077", "Futuristic RPG", 59.99, Date.valueOf("2020-12-10"));
        gameDAO.insertGame(newGame);

        // Retrieve and print all games
        System.out.println("All Games:");
        gameDAO.getAllGames().forEach(System.out::println);

        // Update a Game
        Game updatedGame = new Game("Cyberpunk 2077", "Updated description", 49.99, Date.valueOf("2021-01-01"));
        gameDAO.updateGame("Cyberpunk 2077", updatedGame);

        // Delete a Game
        gameDAO.deleteGame("Cyberpunk 2077");
    }
}
