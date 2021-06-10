from libqtile.config import Group


def group(group_labels):
    group = []
    group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    for i in range(len(group_names)):
        group.append(Group(
            name=group_names[i],
            label=group_labels[i],
        ))
    return group


groups = group(
    ["Www", "Dev", "Term", "Msg", "Sys", "Doc", "Mus", "Vid", "Img", "Gam"])

# groups = group(["\uf8a4", "\uf8a7", "\uf8aa", "\uf8ad", "\uf8b0",
#                 "\uf8b3", "\uf8b6", "\uf8b9", "\uf8bc", "\uf8a1"])

# groups = group(["", "", "ﲵ", "", "漣", "", "ﱘ", "", "", ""])
