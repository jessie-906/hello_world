class GameStats:
    """Track statistics for the game."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settigns = ai_game.settings
        self.reset_stats()
    
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settigns.ship_limit - 1