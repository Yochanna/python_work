class GameStats:
    """Track game statistics."""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False  # start inactive until Play is clicked

    def reset_stats(self):
        self.ships_left = 3
