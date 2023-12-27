def calculate_team_total_rating(team: list) -> int:
    return sum([player.get_rating() for player in team])


def elves_concert(elves: list) -> None:
    [player.play_elf_song() for player in elves]


def feast_of_the_dwarves(dwarves: list) -> None:
    [player.eat_favourite_dish() for player in dwarves]
