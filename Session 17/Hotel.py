# Sistem simplu de rezervări pentru hotel
# •	Clasa Room cu număr și disponibilitate.
# •	Clasa Hotel cu listă de camere și metode:
# o	check_in(room_number)
# o	check_out(room_number)
# o	available_rooms()

class Room:
    def __init__(self, numar):
        self.numar = numar
        self.disponibila = True

    def check_in(self):
        if self.disponibila:
            self.disponibila = False
        else:
            raise Exception("Camera nu este disponibila")

    def check_out(self):
        if not self.disponibila:
            self.disponibila = True
        else:
            raise Exception("Camera nu este ocupata")

    def __str__(self):
        return f"Camera {self.numar} {'nu ' if not self.disponibila else ''}este valabila"


class Hotel:
    def __init__(self, rooms=None):
        # self.rooms = rooms if rooms is not None else []
        if rooms is None:
            self.rooms = []
        else:
            self.rooms = rooms

    def add_room(self, numar):
        for room in self.rooms:
            if room.numar == numar:
                raise Exception("Deja exista o camera cu acest numar")
        self.rooms.append(Room(numar))

    def available_rooms(self):
        return [room for room in self.rooms if room.disponibila]

    def all_roms(self):
        return self.rooms

    def check_in(self, numar):
        for room in self.rooms:
            if room.numar == numar:
                room.check_in()
                return

        raise Exception("Nu am gasit nicio camera cu numarul specificat")

    def check_out(self, numar):
        for room in self.rooms:
            if room.numar == numar:
                room.check_out()
                return

        raise Exception("Nu am gasit nicio camera cu numarul specificat")



if __name__ == "__main__":
    hotel = Hotel()
    hotel.add_room(1)
    hotel.add_room(2)
    hotel.add_room(3)
    hotel.add_room(4)
    hotel.add_room(5)
    hotel.add_room(6)

    hotel.check_out(5)
    hotel.check_in(6)

    for room in hotel.available_rooms():
        print(room)

    hotel.check_out(6)
    print("##############################")

    for room in hotel.available_rooms():
        print(room)
