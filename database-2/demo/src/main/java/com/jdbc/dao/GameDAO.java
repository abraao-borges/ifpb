package com.jdbc.dao;

import com.jdbc.entity.Game;
import com.jdbc.helpers.JDBCHelper;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class GameDAO {

    // CREATE (Insert a new Game)
    public void insertGame(Game game) {
        String sql = "INSERT INTO game (name, description, price, release) VALUES (?, ?, ?, ?)";

        try (Connection conn = JDBCHelper.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, game.getName());
            stmt.setString(2, game.getDescription());
            stmt.setDouble(3, game.getPrice());
            stmt.setDate(4, game.getRelease());

            stmt.executeUpdate();
            System.out.println("Game inserted successfully!");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    // READ (Retrieve all Games)
    public List<Game> getAllGames() {
        List<Game> games = new ArrayList<>();
        String sql = "SELECT * FROM game";

        try (Connection conn = JDBCHelper.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql);
             ResultSet rs = stmt.executeQuery()) {

            while (rs.next()) {
                Game game = new Game(
                    rs.getString("name"),
                    rs.getString("description"),
                    rs.getDouble("price"),
                    rs.getDate("release")
                );
                games.add(game);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return games;
    }

    // UPDATE (Modify a Game by Name)
    public void updateGame(String name, Game updatedGame) {
        String sql = "UPDATE game SET description = ?, price = ?, release = ? WHERE name = ?";

        try (Connection conn = JDBCHelper.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, updatedGame.getDescription());
            stmt.setDouble(2, updatedGame.getPrice());
            stmt.setDate(3, updatedGame.getRelease());
            stmt.setString(4, name);

            int rowsUpdated = stmt.executeUpdate();
            if (rowsUpdated > 0) {
                System.out.println("Game updated successfully!");
            } else {
                System.out.println("Game not found!");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    // DELETE (Remove a Game by Name)
    public void deleteGame(String name) {
        String sql = "DELETE FROM game WHERE name = ?";

        try (Connection conn = JDBCHelper.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, name);

            int rowsDeleted = stmt.executeUpdate();
            if (rowsDeleted > 0) {
                System.out.println("Game deleted successfully!");
            } else {
                System.out.println("Game not found!");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
