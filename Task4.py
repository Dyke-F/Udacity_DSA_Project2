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


def is_user_in_group(user, group):
    """
        Return True if user is in the group, False otherwise.
        
        Args:
        user(str): user name/id
        group(class:Group): group to check user membership against
        """
    
    if user in group.users:
        return True
    
    else:
        subgroups = [c for c in group.groups]
        for subgroup in subgroups:
            return is_user_in_group(user, subgroup)
        return False


### Official test cases ###
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

### Own testing on test
print("Non-edge cases:")
print(is_user_in_group(user = "sub_child_user", group=sub_child))
# True
print(is_user_in_group(user = "child", group=parent))
# False (only child group exists but no child as user)
print(is_user_in_group(user = "sub_child_user", group=parent))
# True

print("====================")

print("Edge case testing:")
print(is_user_in_group(user = "SebastianThrun", group=child))
# False
print(is_user_in_group(user = "parent", group=sub_child))
# False



