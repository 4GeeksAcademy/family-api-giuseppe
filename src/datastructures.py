from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = []

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member["id"] = member.get("id", self._generateId())
        self._members.append(member)

    def delete_member(self, member_id):
        self._members = [member for member in self._members if member["id"] != member_id]

    def update_member(self, member_id, updated_member):
        for i, member in enumerate(self._members):
            if member["id"] == member_id:
                self._members[i] = updated_member

    def get_member(self, member_id):
        for member in self._members:
            if member["id"] == member_id:
                return member

    def get_all_members(self):
        return self._members
