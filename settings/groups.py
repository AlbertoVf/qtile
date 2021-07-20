from libqtile.config import Group


def group(group_labels):
    group = []
    group_names = ["1", "2", "3", "4", "5", "6", "7"]
    for i in range(len(group_names)):
        group.append(Group(
            name=group_names[i],
            label=group_labels[i],
        ))
    return group


groups = group(
    ["Web", "Developer", "Terminal", "Vbox", "Planning", "System", "Media"],
)
