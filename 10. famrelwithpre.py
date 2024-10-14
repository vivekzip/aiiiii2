class FamilyRelations:
    def __init__(self):
        self.facts = {
            'male': ['John', 'Mike', 'Tom'],
            'female': ['Jane', 'Lisa', 'Anna'],
            'parent': {
                'John': ['Mike', 'Anna'],
                'Jane': ['Mike', 'Anna'],
                'Mike': ['Tom'],
                'Lisa': ['Tom']
            }
        }

    def is_father(self, child):
        for father in self.facts['male']:
            if child in self.facts['parent'].get(father, []):
                return father
        return None

    def is_mother(self, child):
        for mother in self.facts['female']:
            if child in self.facts['parent'].get(mother, []):
                return mother
        return None

    def is_grandfather(self, grandchild):
        father = self.is_father(grandchild)
        if father:
            return self.is_father(father)
        return None

    def is_grandmother(self, grandchild):
        mother = self.is_mother(grandchild)
        if mother:
            return self.is_mother(mother)
        return None

    def is_brother(self, sibling):
        father = self.is_father(sibling)
        siblings = self.facts['parent'].get(father, [])
        return [bro for bro in siblings if bro != sibling and bro in self.facts['male']]

    def is_sister(self, sibling):
        father = self.is_father(sibling)
        siblings = self.facts['parent'].get(father, [])
        return [sis for sis in siblings if sis != sibling and sis in self.facts['female']]

family = FamilyRelations()
print("Father of Tom:", family.is_father('Tom'))
print("Mother of Tom:", family.is_mother('Tom'))
print("Grandfather of Tom:", family.is_grandfather('Tom'))
print("Grandmother of Tom:", family.is_grandmother('Tom'))
print("Brothers of Anna:", family.is_brother('Anna'))
print("Sisters of Mike:", family.is_sister('Mike'))
