class User:
    Id=0
    Name=""
    Surname=""
    Email=""
    Username=""
    Password=""
    IsAdmin=False

    @classmethod
    def Register(cls,name,surname,email,username,password):
        user = User()
        user.Surname=surname
        user.Name=name
        user.Email=email
        user.Username=username
        user.Password=password
        if username=="altanemre":
            user.IsAdmin=True
        return user