# from app.players.elves.elf_ranger import ElfRanger
# from app.players.elves.druid import Druid
# from app.players.dwarves.dwarf_warrior import DwarfWarrior
# from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
# Comented because of test flake8 app, or it is possible to add examples

def calculate_team_total_rating(team: list) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
