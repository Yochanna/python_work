import os

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False

        # Load high score from file if present
        self.high_score_file = "high_score.txt"
        self.high_score = 0
        if os.path.exists(self.high_score_file):
            try:
                with open(self.high_score_file, "r", encoding="utf-8") as f:
                    self.high_score = int(f.read().strip() or 0)
            except Exception:
                self.high_score = 0

    def reset_stats(self):
        """Stats that change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def save_high_score(self):
        try:
            with open(self.high_score_file, "w", encoding="utf-8") as f:
                f.write(str(self.high_score))
        except Exception:
            pass
