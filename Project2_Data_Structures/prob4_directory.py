# @Author: otrejo
# @Date:   2020-03-05T00:12:05-05:00
# @Last modified by:   otrejo
# @Last modified time: 2020-03-24T20:45:44-04:00



class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    return (user in group.get_users())

print(is_user_in_group(sub_child_user, sub_child))
print(is_user_in_group(sub_child_user, parent))
print(is_user_in_group(child, sub_child))
