class Settings:
    """储存游戏《外星人入侵》中所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        self.screen_width = 800
        self.screen_height = 1000
        self.bg_color = (13,52,165)
        self.ship_speed = 3.0
        #子弹设置
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (255,0,0)
        self.bullet_allowed = 3
