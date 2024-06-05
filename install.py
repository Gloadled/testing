import curses
import subprocess

def run_command(command):
    subprocess.run(command, shell=True)

def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    
    menu = ['Update Package List', 'Upgrade Packages', 'Upgrade Pip', 'Exit']
    selected = 0
    
    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        
        for i, item in enumerate(menu):
            x = w//2 - len(item)//2
            y = h//2 - len(menu)//2 + i
            if i == selected:
                stdscr.addstr(y, x, item, curses.A_REVERSE)
            else:
                stdscr.addstr(y, x, item)
        
        stdscr.refresh()
        
        key = stdscr.getch()
        
        if key == curses.KEY_UP and selected > 0:
            selected -= 1
        elif key == curses.KEY_DOWN and selected < len(menu) - 1:
            selected += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if selected == 0:
                run_command('sudo apt update')
            elif selected == 1:
                run_command('sudo apt upgrade -y')
            elif selected == 2:
                run_command('pip install --upgrade pip')
            elif selected == 3:
                break

if __name__ == '__main__':
    curses.wrapper(main)
