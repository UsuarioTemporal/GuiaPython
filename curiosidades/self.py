class Self():
    def self(self):
        return self

    @classmethod
    def cls(cls):
        return cls
yo = Self()
print(yo.self())
print(Self.self(yo))
Self.cls()
print(isinstance(yo,object))