class Schema:
    def __init__(self, **kwargs):
        self.Name = kwargs
        self.Description = kwargs
        self.Presentation = kwargs
        self.Address = kwargs
        self.PhoneNumber = kwargs
        self.Email = kwargs
        self.WebSite = kwargs

    @classmethod
    def get_schema(cls):
        return cls
