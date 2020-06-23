import sys
import address_getter
import pygame
import time
import random


def super_main(last_file=None):
    if last_file is None:
        mode = False
    else:
        mode = True

    edge_li = ["P", "G", "R", "S", "H", "C", "F", "E", "N"]
    edges = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M", 'N', 'O', 'P', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
    C = "Comms/Corners A-Z/Comms D.txt"
    E = f"Comms/Edges A-Z/Comms {random.choice(edge_li)}.txt"

    # make an interface with buttons to load specific comm stickers

    if mode:
        address_getter.return_address(E)
    elif not mode:
        address_getter.return_address(E)

    # TODO make a settings file to read comm address
    # TODO have a button to reload comms,
    #  so you don't have to close and reopen it each time
    # print(count)

    alg_data = open("alg_data.txt", "r+")
    f = open("sys_admin_X6hW%rD!pYM9h7%.txt", "r")

    file_address_comms = f.readline()
    index = open(file_address_comms, "r")
    f.close()

    address_getter.remove_file("sys_admin_X6hW%rD!pYM9h7%.txt")

    count = 0
    with open(file_address_comms, 'r') as f:
        for _ in f:
            count += 1

    pairs = []
    graph_li = []

    for i in range(count):
        pair = index.readline(count)
        if "=" in pair:
            pair = pair.split('=')
            pairs.append(pair[0])

    pairs_rand = []
    for i in range(count):
        if len(pairs) != 0:
            rnd = random.choice(pairs)

            pairs_rand.append(rnd)
            pairs.remove(rnd)

    pairs_rand.append("")

    # Monkey
    # Window
    pygame.init()
    pygame.font.init()
    Width, Height = 600, 400
    Win = pygame.display.set_mode((Width, Height))
    pygame.display.set_caption("Alg Timer v1.0")

    class Display:
        def __init__(self, x, y, text, color=None, size=50, font="arial"):
            self.x = x
            self.y = y
            self.text = text
            if color is None:
                color = [0, 0, 0]
                self.r = color[0]
                self.g = color[1]
                self.b = color[2]
            #     TODO make color var split into rgb
            self.color = color
            self.size = size
            self.font = font

            self.font_obj = pygame.font.SysFont(font, size)
            self.label = self.font_obj.render(text, 1, (self.r, self.g, self.b))

        def draw(self, window):
            window.blit(self.label, (self.x, self.y))

        def change_text(self, newtext):
            self.label = self.font_obj.render(str(newtext), 1, (0, 0, 0))
            self.text = newtext

        def change_timer_text(self, newtext):
            newtext = str(round(newtext, 3))
            self.label = self.font_obj.render(newtext, 1, (0, 0, 0))
            self.text = newtext

        def center_text(self, width, height):
            self.x = width // 2 - self.label.get_width() // 2
            self.y = height // 2 - self.label.get_height() // 2

    def main():
        run = True
        FPS = 100
        timer = 0
        times = []
        num = 1
        clock = pygame.time.Clock()
        words = Display(0, 0, "Hello World")
        alg_count = Display(100, 100, "Alg count", size=30)
        count_v2 = 0
        times_v2 = 0
        cool_knight = False
        pair_obj = Display(Width // 2, Height // 2, pairs_rand[0])
        pair_obj.center_text(Width, Height)
        happy_pink_bunny = False
        space_down = False
        update = False

        def redraw_window():
            if space_down:
                Win.fill((52, 235, 232))
            elif not space_down:
                Win.fill((0, 255, 0))
            words.draw(Win)
            alg_count.draw(Win)
            pair_obj.draw(Win)
            pygame.display.update()
            return False

        timer = 0
        while run:
            clock.tick(FPS)
            down = redraw_window()
            space_down = down

            alg_count.change_timer_text(timer)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                timer = 0

            if keys[pygame.K_SPACE]:
                space_down = True
                if timer > .1 and len(pairs_rand) > 1:

                    update = True
                    graph_li.append(pairs_rand[num - 1])

                    if len(pairs_rand) > 1:
                        pair_obj.change_text(pairs_rand[num])
                    timer = round(timer, 5)
                    times.append(timer)
                    num += 1
                if count == num - 1:
                    happy_pink_bunny = True
                timer = 0

            if keys[pygame.K_r]:
                super_main()
            if keys[pygame.K_ESCAPE]:
                pygame.display.quit()
                pygame.quit()
                sys.exit(0)
                quit()

            if happy_pink_bunny:
                pygame.display.quit()

                return super_main(index)
                while True:

                    clock.tick(FPS)
                    redraw_window()
                    keys = pygame.key.get_pressed()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                    if keys[pygame.K_ESCAPE]:
                        pass
                    if keys[pygame.K_r]:
                        super_main()
                    if keys[pygame.K_ESCAPE]:
                        pass

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            timer += .01

    def main_menu():
        title_font = pygame.font.SysFont("arial", 45)

        def fill_scr():
            Win.fill((0, 255, 0))
            pygame.display.update()

        run = True
        while run:
            Win.fill((52, 235, 232))
            title_label = title_font.render("Press space to begin...", 1, (0, 0, 0))
            Win.blit(title_label,
                     (Width // 2 - title_label.get_width() // 2, Height // 2 - title_label.get_height() // 2))
            pygame.display.update()
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if keys[pygame.K_SPACE]:
                    for i in range(3, 0, -1):
                        fill_scr()
                        title_label = title_font.render(str(i), 1, (0, 0, 0))
                        Win.blit(title_label,
                                 (Width // 2 - title_label.get_width() // 2,
                                  Height // 2 - title_label.get_height() // 2))
                        pygame.display.update()
                        time.sleep(1)
                        cool_knight = True
                    main()

    main_menu()


if __name__ == '__main__':
    super_main()
