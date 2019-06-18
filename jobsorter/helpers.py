from collections import UserList


class UniqueList(UserList):
    """ List wrapper that only allows new values to be added.
    """
    
    def append(self, item):
        if item not in self.data:
            self.data.append(item)

    def extend(self, new_list):
        [self.append(item) for item in new_list]