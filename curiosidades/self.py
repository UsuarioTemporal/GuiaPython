class Self():
    def self(self):
        return self
yo = Self()
print(yo.self())
print(isinstance(yo,object))