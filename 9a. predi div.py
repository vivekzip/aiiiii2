class PredicateDeriver:
    def __init__(self):
        self.relationships = {}

    def add_relationship(self, subject, relation, obj):
        self.relationships[(subject, relation)] = obj

    def derive(self, subject, relation):
        if (subject, relation) in self.relationships:
            obj = self.relationships[(subject, relation)]
            if relation in self.relationships:
                return self.derive(obj, self.relationships[(obj, relation)])
            return obj
        return None

deriver = PredicateDeriver()
deriver.add_relationship('Sachin', 'is', 'batsman')
deriver.add_relationship('batsman', 'is', 'cricketer')

result = deriver.derive('Sachin', 'is')
print(f"Sachin is Cricketer: {result}")
