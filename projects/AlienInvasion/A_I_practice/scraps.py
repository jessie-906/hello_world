"""Below are two methods for arranged stars neatly"""

#METHOD 1
def create_stars(self):
    """ This follows the book's example,
    but it leaves too much white space on the right,
    so I've discarded it. """

    star = Star(self)
    star_width, star_height = star.rect.width, star.rect.height
    current_x, current_y = star_width, star_height
            
    while current_x <= (self.screen_rect.width - star_width * 2):
        new_star = Star(self)
        new_star.x = current_x
        new_star.rect.x = new_star.x
        self.stars.add(new_star)
        current_x += star_width * 2

#METHOD 2
def calculate_spacing(self):
    """ This was my own experimental method, 
        but it ended up being hard-coded,
        so I've abandoned it. """
    star = Star(self)
    star_width = star.rect.width
    current_x = star_width
    draw_width = self.screen_rect.width - current_x
    a_group = current_x * 2
    alien_count, remaining_space = divmod(draw_width, a_group) 
    #drse = Distribute the remaining space evenly
    drse = remaining_space / alien_count + 1
    
    while len(self.stars) < alien_count:
        new_star = Star(self)
        new_star.x = current_x + drse
        new_star.rect.x = new_star.x
        self.stars.add(new_star)
        current_x += star_width * 2 
        current_x += drse